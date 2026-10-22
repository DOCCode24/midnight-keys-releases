# Sound assets, licenses and attribution

## Salamander Grand Piano V3 (the only sampled instrument)

- Author: Alexander Holm. Instrument: Yamaha C5 concert grand.
- License: Creative Commons Attribution 3.0 (CC BY 3.0) — https://creativecommons.org/licenses/by/3.0/
- Original release: https://archive.org/details/SalamanderGrandPianoV3
- Files used from: https://github.com/sfzinstruments/SalamanderGrandPiano (Samples folder)
- Changes made by Midnight Keys: 5 of the 16 velocity layers (v2, v6, v10, v13, v16) at 30 pitches (A0 to C8, every minor third), plus pedal-down/up noises; converted from FLAC to 128 kbps MP3; trimmed to 14 seconds with a 2-second fade. Reproducible with `assets-src/fetch.sh`.

## Synthesized sounds (no samples)

Studio Tine EP, Tine EP Tremolo, Reed EP, Reed EP Tremolo, the four tonewheel organ presets (drawbars, percussion, key click, drive, rotary speaker), Funk Clav, Ensemble Strings and Warm Pad are generated in real time by Midnight Keys' own code (`src/audio/engine.ts`). They are original sounds in those instrument families. No audio from Nord, Clavia, Spectrasonics, Hammond, Leslie, Rhodes, Wurlitzer, Hohner or any other commercial product is used, sampled or imitated from recordings. Those names are trademarks of their owners and appear nowhere in the app.

Nord Stage 4 sounds were requested. They come from Nord's proprietary Nord Piano Library and Nord Sample Library, licensed only for use on Nord hardware, so none are included.

## Not included

- Upright piano: no free upright sample set with a verified redistribution license was bundled, so it is listed as unavailable in the app.

## Other assets

- Fonts: Cormorant Garamond and Manrope, SIL Open Font License 1.1, via @fontsource packages.
- Artwork (`public/art/grand.webp`, `organ.webp`, `epiano.webp`): AI-generated for Midnight Keys, unbranded, no logos.
- Desktop shell: Electron (MIT). Build tooling: Vite, TypeScript, Vitest, electron-builder (MIT/Apache-2.0).
