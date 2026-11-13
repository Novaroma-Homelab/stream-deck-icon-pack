# Naming scheme

Everything in this pack follows one pattern, so you can find, sort and script icons without opening the browser.

## File names

```
<season>-<mode>-<symbol>[-<state>][-clear].png
```

- `season`: `standard`, `fruehling` (spring), `sommer` (summer), `herbst` (autumn), `winter`.
- `mode`: `light`, `dark`, `burgundy`.
- `symbol`: lower-case English id with hyphens, for example `gear`, `soundboard`, `cabinet-light`.
- `state`: only on toggle icons, `off` or `on` (see below).
- `clear`: optional suffix. The icon has no tile and no frame, just the symbol on transparency.

Examples: `sommer-dark-gear.png`, `herbst-light-cabinet-light-on.png`, `winter-burgundy-spot-light-off-clear.png`.

Every icon is 144 x 144 px PNG.

## Symbol ids

- Lower case, words separated by hyphens, English, no umlauts.
- A badge on a symbol is a suffix: `-plus`, `-minus`, `-check`, `-up`, `-down`, `-out` (arrow out). Example: `camera-photo-check`, `chat-up`.
- A crossed-out symbol ends in `-slash`: `bell-slash`, `microphone-slash`, `wifi-signal-slash`.
- Where an id would collide with an older on/off pair, the library id is more specific: `camera-photo` (library) and `camera` (older device on/off pair).

## Three kinds of icons

1. **Single icons** (about 120 symbols, no state): the original line icons. File name has no state.
2. **Device on/off pairs** (older pairs: bulb, camera, ceiling-light, eye, lamp, mic, moon, plug, speaker, switch, thermostat, toggle, tv, wifi): `-off` and `-on` mean the device is off or on, for Home Assistant style keys.
3. **Library pairs** (`Library` tag): every symbol exists as `-off` = outline and `-on` = filled. For light symbols the On version also glows (accent coloured rays or beam). Use them as the two states of a toggle key.

## Display names and tags (Stream Deck icon browser)

Display name: `<Symbol name> [Off|On] (<Season> <Mode>[, no background])`, for example `Cabinet light On (Autumn Dark)`.

Tags always include: symbol name, id, season (English and German), mode (English and German), `Season`. Library icons also carry `Library`, `Toggle`, `Off`/`On`, `Aus`/`An`, `Outline`/`Filled`, the group name and German search words. Icons without background carry `No background`, `Transparent`, `Ohne Hintergrund`.

Search tips: type `light` for all lights, `Toggle` for all pairs, `Filled` for On states, `No background` for transparent ones.

## Groups

Light, Arrows & signs, Shapes, Objects, Files & folders, Devices & layout. The full list per group is in [LIBRARY.md](LIBRARY.md).

## Colours

Each season has light, dark and burgundy tiles with a symbol colour, a frame and an accent underline. Light symbols suit dark wallpapers and the other way round.
