# Midnight Keys — Windows downloads

Midnight Keys is a virtual piano for Windows with MIDI keyboard support. This repository holds the installer downloads only. The source code is kept in a separate private repository.

## Install

1. Open the [latest release](https://github.com/DOCCode24/midnight-keys-releases/releases/latest) and download `MidnightKeys-Setup-<version>.exe`.
2. Run it. The installer is not code-signed, so Windows SmartScreen may show a warning: choose **More info → Run anyway**.
3. It installs for your Windows user only (no admin needed) and adds Desktop and Start menu shortcuts.

## Updates

Installed copies check this repository when they open and every 6 hours. New versions download in the background, and the app asks to restart when one is ready. Settings are kept. You can also go to Diagnostics → Check for updates.

## Sound packs

The full concert grand (Accurate-Salamander, 16 layers, 247 MB) and the recorded Rhodes (22 MB) download once, the first time you pick them in the app, from the [packs-v1 release](https://github.com/DOCCode24/midnight-keys-releases/releases/tag/packs-v1). Each file is checked against its SHA-256 before use. `packs/build_packs.py` rebuilds them from the original downloads.

## Sounds and licenses

- Full grand: Accurate-Salamander Grand Piano V6.2a by Chisato Yamauchi, from the Salamander Grand Piano by Alexander Holm, [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).
- Built-in grand: Salamander Grand Piano V3 by Alexander Holm, [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).
- Rhodes: jRhodes3d by Jeff Learman, [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) (non-commercial).
- Symphony Hall: OpenAIR (University of York), Usina del Arte Symphony Hall, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- Orchestra: VSCO 2 Community Edition, CC0. Organ, Reed EP, clav, strings and pads are synthesized.

Midnight Keys is for personal, non-commercial use. See [LICENSES.md](LICENSES.md).
