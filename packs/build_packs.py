#!/usr/bin/env python3
"""Build Midnight Keys sound packs from the original free sample sets.

Each pack is two files: <id>.json (mapping + file index) and <id>.bin (all
samples concatenated). Samples are stored as lossless FLAC. The grand is
re-quantized from 24-bit to 16-bit with TPDF dither (the recordings' own
noise floor is far above the 16-bit floor), which cuts the download to ~1/3.

Usage: build_packs.py <asgp_dir> <rhodes_dir> <rhodes_sfz> <out_dir>
  asgp_dir   = unzipped AccurateSalamanderGrandPianoV6.2a_48khz24bit_flac
  rhodes_dir = folder with jRhodes3d-mono/*.flac
"""
import hashlib, io, json, os, re, sys
import numpy as np, soundfile as sf

NOTE = {'c': 0, 'd': 2, 'e': 4, 'f': 5, 'g': 7, 'a': 9, 'b': 11}

def key_num(v: str) -> int:
    v = v.strip()
    if re.fullmatch(r'-?\d+', v): return int(v)
    m = re.fullmatch(r'([A-Ga-g])([#b]?)(-?\d+)', v)
    if not m: raise ValueError(v)
    n = NOTE[m.group(1).lower()] + (1 if m.group(2) == '#' else -1 if m.group(2) == 'b' else 0)
    return (int(m.group(3)) + 1) * 12 + n

def parse_sfz(text: str):
    """Return a list of (section_label, opcodes) for every region, with global/master/group opcodes merged in."""
    text = re.sub(r'//[^\n]*', '', text)
    toks = re.split(r'(<\w+>)', text)
    glob, master, group, out, cur, header = {}, {}, {}, [], None, None
    label = ''
    def ops(s):
        return dict(re.findall(r'(\w+)=(\S+)', s))
    for t in toks:
        if re.fullmatch(r'<\w+>', t): header = t[1:-1]; continue
        if header is None: continue
        o = ops(t)
        if header == 'global': glob = o
        elif header == 'master': master = o; group = {}; label = ','.join(f'{k}={v}' for k, v in o.items())
        elif header == 'group': group = o
        elif header == 'region':
            merged = {**glob, **master, **group, **o}
            merged['_group_volume'] = float(group.get('group_volume', 0))
            out.append((label, merged))
    return out

def sha(b: bytes) -> str: return hashlib.sha256(b).hexdigest()

class Bundle:
    def __init__(self): self.buf = io.BytesIO(); self.index = {}
    def add(self, name: str, data: bytes):
        if name in self.index: return
        off = self.buf.tell(); self.buf.write(data); self.index[name] = [off, len(data)]
    def write(self, out_dir: str, pid: str, meta: dict):
        data = self.buf.getvalue()
        with open(os.path.join(out_dir, f'{pid}.bin'), 'wb') as f: f.write(data)
        meta = {**meta, 'bin': f'{pid}.bin', 'size': len(data), 'sha256': sha(data), 'files': self.index}
        with open(os.path.join(out_dir, f'{pid}.json'), 'w') as f: json.dump(meta, f, separators=(',', ':'))
        print(pid, len(self.index), 'files', round(len(data) / 1e6, 1), 'MB')

def to_flac16(path: str, seed: int) -> tuple[bytes, int]:
    d, sr = sf.read(path, dtype='float64', always_2d=True)
    info = sf.info(path)
    if info.subtype != 'PCM_16':
        rng = np.random.default_rng(seed)
        d = d + (rng.random(d.shape) - rng.random(d.shape)) / 32768.0  # TPDF dither, 1 LSB
    d = np.clip(d, -1.0, 32767 / 32768)
    b = io.BytesIO(); sf.write(b, d, sr, format='FLAC', subtype='PCM_16')
    return b.getvalue(), sr

def build_grand(src: str, out_dir: str):
    sfz = os.path.join(src, 'sfz_live', 'Accurate-SalamanderGrandPiano_flat.Recommended.sfz')
    regions = parse_sfz(open(sfz, encoding='utf-8', errors='replace').read())
    wav = os.path.join(src, '48khz24bit')
    bundle = Bundle(); rates = {}
    def add(fname: str) -> str:
        if fname not in bundle.index:
            data, sr = to_flac16(os.path.join(wav, fname), len(bundle.index) + 1)
            bundle.add(fname, data); rates[fname] = sr
        return fname
    notes, res, rel, ham, pedal = [], [], [], [], {'down': [], 'up': []}
    for label, o in regions:
        f = o['sample'].replace('\\', '/').split('/')[-1]
        vol = float(o.get('volume', 0)) + o['_group_volume']
        lo, hi = key_num(o.get('lokey', o.get('key', '-1'))), key_num(o.get('hikey', o.get('key', '-1')))
        lv, hv = int(o.get('lovel', 1)), int(o.get('hivel', 127))
        kc = key_num(o['pitch_keycenter']) if 'pitch_keycenter' in o else lo
        tune = float(o.get('tune', 0))
        if 'locc23' in label:
            res.append({'key': lo, 'file': add(f), 'vol': vol, 'tune': tune, 'kc': kc})
        elif 'locc20' in label:
            rel.append({'lo': lo, 'hi': hi, 'lovel': lv, 'hivel': hv, 'file': add(f), 'kc': kc, 'vol': vol, 'decay': float(o.get('rt_decay', 0))})
        elif 'locc21' in label:
            ham.append({'key': lo, 'file': add(f), 'vol': vol, 'decay': float(o.get('rt_decay', 0))})
        elif 'locc22' in label:
            pedal['down' if f.startswith('pedalD') else 'up'].append(add(f))
            pedal['downVol' if f.startswith('pedalD') else 'upVol'] = vol
        else:
            off = int(o.get('offset', 0))
            add(f)
            notes.append({'key': lo, 'file': f, 'vol': vol, 'lovel': lv, 'hivel': hv, 'tune': tune, 'kc': kc, 'offset': off / rates[f]})
    print('grand regions: notes', len(notes), 'resonance', len(res), 'release', len(rel), 'hammer', len(ham), 'pedal', pedal)
    assert len(notes) == 88 * 16, len(notes)
    assert len({n['file'] for n in notes}) == 480
    meta = {
        'id': 'grand', 'version': 1, 'name': 'Accurate-Salamander Grand Piano V6.2a',
        'credit': 'Accurate-Salamander by Chisato Yamauchi (remaster), from Salamander Grand Piano by Alexander Holm. Yamaha C5.',
        'license': 'CC BY (see https://www.ir.isas.jaxa.jp/~cyamauch/AccurateSalamander/)',
        'veltrack': 0.985, 'noteRelease': 0.5, 'resAttack': 0.05,
        'notes': notes, 'resonance': res, 'release': rel, 'hammer': ham, 'pedal': pedal,
    }
    bundle.write(out_dir, 'grand', meta)

def build_rhodes(src: str, sfz_path: str, out_dir: str):
    regions = parse_sfz(open(sfz_path, encoding='utf-8').read())
    bundle = Bundle(); layers = []
    for _, o in regions:
        f = o['sample'].split('/')[-1]
        if f not in bundle.index:
            data, _ = to_flac16(os.path.join(src, f), 1)
            bundle.add(f, data)
        layers.append({'lo': key_num(o['lokey']), 'hi': key_num(o['hikey']), 'kc': key_num(o['pitch_keycenter']), 'file': f,
                       'lovel': int(o['lovel']), 'hivel': int(o['hivel']),
                       'xfin': [int(o['xfin_lovel']), int(o['xfin_hivel'])] if 'xfin_lovel' in o else None,
                       'xfout': [int(o['xfout_lovel']), int(o['xfout_hivel'])] if 'xfout_lovel' in o else None,
                       'release': float(o.get('ampeg_release', 0.4))})
    print('rhodes regions', len(layers))
    meta = {
        'id': 'rhodes', 'version': 1, 'name': 'jRhodes3d (1977 Rhodes Mark I Stage 73)',
        'credit': 'jRhodes3d by Jeff Learman, https://github.com/sfzinstruments/jlearman.jRhodes3d',
        'license': 'Samples CC BY-NC 4.0 (non-commercial). Commercial licence available from the author.',
        'gainDb': 6, 'regions': layers,
    }
    bundle.write(out_dir, 'rhodes', meta)

if __name__ == '__main__':
    asgp, rh, rh_sfz, out = sys.argv[1:5]
    os.makedirs(out, exist_ok=True)
    which = sys.argv[5] if len(sys.argv) > 5 else 'all'
    if which in ('all', 'rhodes'): build_rhodes(rh, rh_sfz, out)
    if which in ('all', 'grand'): build_grand(asgp, out)
