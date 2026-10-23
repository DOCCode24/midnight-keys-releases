# Sound assets, licenses and attribution

## Personal, non-commercial use

Midnight Keys is built for personal, non-commercial use. No licence key, account or copy protection is used or needed. The recorded Rhodes pack (below) is licensed for non-commercial use only. Selling or commercially distributing Midnight Keys with that pack would need a commercial licence from its author, or the pack replaced. Everything else is CC BY, CC0 or original code.

## Accurate-Salamander Grand Piano V6.2a (download pack "grand")

- Remastered by Chisato Yamauchi (Accurate-Salamander Project), from the Salamander Grand Piano by Alexander Holm (Yamaha C5).
- License: Creative Commons Attribution 3.0 (CC BY 3.0) — https://creativecommons.org/licenses/by/3.0/
- Project page: https://www.ir.isas.jaxa.jp/~cyamauch/AccurateSalamander/
- Source file: https://archive.org/download/httpswww.ir.isas.jaxa.jpcyamauchaccuratesalamander/AccurateSalamanderGrandPianoV6.2a_48khz24bit_flac.zip
- Used: all 16 velocity layers on all 88 keys, full length, plus string-release, hammer-release, sympathetic resonance and pedal samples, mapped from `sfz_live/Accurate-SalamanderGrandPiano_flat.Recommended.sfz`.
- Changes made by Midnight Keys: 24-bit FLAC converted to 16-bit FLAC with TPDF dither and packed into one file (`grand.bin`, 247 MB). Reproducible with `assets-src/packs/build_packs.py`. Downloaded once from https://github.com/DOCCode24/midnight-keys-releases/releases/tag/packs-v1 the first time a grand preset is picked (Windows app).

## jRhodes3d (download pack "rhodes")

- Author: Jeff Learman. Recorded Rhodes Mark I electric piano.
- Source: https://github.com/sfzinstruments/jlearman.jRhodes3d
- License for the samples: Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0) — https://creativecommons.org/licenses/by-nc/4.0/ . Commercial licences are available from the author (jjlearman@gmail.com).
- Used for: Stage Rhodes, Rhodes Tremolo, Rhodes + Pad.
- Changes made by Midnight Keys: mono mapping (`jRhodes3d-mono.sfz`) packed into one file (`rhodes.bin`, 22 MB); velocity crossfades as in the SFZ. Downloaded once on first use (Windows app).

## Symphony Hall impulse response

- Source: OpenAIR library, University of York — Usina del Arte Symphony Hall (Buenos Aires), source 1 / position 4, stereo. https://www.openair.hosted.york.ac.uk/
- License: Creative Commons Attribution 4.0 (CC BY 4.0) — https://creativecommons.org/licenses/by/4.0/
- Changes made by Midnight Keys: direct sound removed (first 7 ms, so the piano's own attack is not doubled), shortened to 1.82 s with a 150 ms fade, saved as `public/ir/symphony-hall.flac`. Used by the "Symphony Hall" room and the "Grand Piano – Symphony Hall" preset.

## Salamander Grand Piano V3 (built-in grand)

- Author: Alexander Holm. Instrument: Yamaha C5 concert grand.
- License: Creative Commons Attribution 3.0 (CC BY 3.0) — https://creativecommons.org/licenses/by/3.0/
- Original release: https://archive.org/details/SalamanderGrandPianoV3
- Files used from: https://github.com/sfzinstruments/SalamanderGrandPiano (Samples folder)
- Changes made by Midnight Keys: 5 of the 16 velocity layers (v2, v6, v10, v13, v16) at 30 pitches (A0 to C8, every minor third), plus pedal-down/up noises; converted from FLAC to 128 kbps MP3; trimmed to 14 seconds with a 2-second fade. Reproducible with `assets-src/fetch.sh`. Plays while the full grand pack downloads, and in the browser version.

## VSCO 2 Community Edition (orchestra)

- Author: Versilian Studios (Sam Gossner and contributors).
- License: Creative Commons Zero 1.0 (CC0, public domain dedication) — https://creativecommons.org/publicdomain/zero/1.0/ . No attribution is required; it is given here anyway.
- Source: https://github.com/sgossner/VSCO-2-CE (samples from the master branch, key mapping from the SFZ branch)
- Used for: String Section (violin, viola and cello sections, sustained with vibrato), Pizzicato Strings, French Horn, Brass Section (tuba, tenor trombone, trumpet), Flute, Oboe, Clarinet, Concert Harp, Timpani, Glockenspiel.
- Changes made by Midnight Keys: first round-robin only, one or two velocity layers per instrument; silent lead-in trimmed; sustained samples cut to at most 6 seconds with a crossfaded loop so notes hold as long as the key is down; per-instrument level normalisation; converted from WAV to 128 kbps MP3. Reproducible with `assets-src/orchestra.py`.

## Synthesized sounds (no samples)

Reed EP, Reed EP Tremolo, FM EP (older saved presets only), the four tonewheel organ presets (drawbars, percussion, key click, drive, rotary speaker), Funk Clav, Ensemble Strings and Warm Pad are generated in real time by Midnight Keys' own code (`src/audio/engine.ts`). They are original sounds in those instrument families. No audio from Nord, Clavia, Spectrasonics, Hammond, Leslie, Wurlitzer, Hohner or any other commercial product is used, sampled or imitated from recordings. The recorded Rhodes sounds come only from the jRhodes3d pack above. Rhodes is a trademark of its owner, used here only to describe the recorded instrument.

Nord Stage 4 sounds were requested. They come from Nord's proprietary Nord Piano Library and Nord Sample Library, licensed only for use on Nord hardware, so none are included.

## Not included

- Upright piano: not bundled yet, so it is listed as unavailable in the app. (VSCO 2 CE includes a CC0 upright piano that could be added later.)

## Other assets

- Fonts: Cormorant Garamond and Manrope, SIL Open Font License 1.1, via @fontsource packages.
- Artwork (`public/art/grand.webp`, `organ.webp`, `epiano.webp`, `orchestra.webp`): AI-generated for Midnight Keys, unbranded, no logos.
- Desktop shell: Electron (MIT). Build tooling: Vite, TypeScript, Vitest, electron-builder (MIT/Apache-2.0).
