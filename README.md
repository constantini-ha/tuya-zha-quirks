<h1 align="center">Tuya ZHA Quirks</h1>

<p align="center">
  Zigbee quirks for Tuya devices that <code>zha-device-handlers</code> does not<br>
  cover yet, packaged so Home Assistant picks them up on its own.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Home_Assistant-2024.1+-41BDF5?style=flat-square" alt="Home Assistant">
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="MIT">
</p>

<p align="center">
  <b>English</b> · <a href="README.pt-BR.md">Português</a> · <a href="README.es.md">Español</a>
</p>

---

## Why this exists

ZHA recognises a Zigbee device by its manufacturer string. Tuya ships the same
hardware under new module prefixes every few months, and each new prefix matches
nothing — the device pairs, reports battery, and exposes not one switch.

A quirk is the small file that tells ZHA "this is the device you already know".
Upstream carries hundreds of them, but a brand new prefix takes a release cycle
to arrive. This pack carries the ones we needed in the meantime.

## Devices covered

| Device | Manufacturer string | What it gains |
| --- | --- | --- |
| Nova Digital SA-6 Safira, six gang wall switch | `_TZE28C1000000_gxbdnfrh` | all six gangs as switch entities |

## Installation

1. **HACS** (or Marketplace from 2026.11) → ⋮ → **Custom repositories**
2. URL `https://github.com/constantini-ha/tuya-zha-quirks`, category *Integration*
3. Install, restart, then **Settings → Devices & services → Add integration → Tuya ZHA Quirks**

There is nothing to configure. Adding it is what loads the quirks.

**Re-pair the device afterwards**, or restart once more. ZHA matches a quirk when
it interviews a device, so one that was already paired keeps the shape it was
interviewed with until it is interviewed again.

## Writing one

Drop a module in `custom_components/tuya_zha_quirks/quirks/`. Anything there is
imported at setup, and a quirk registers itself with zigpy on import. Read the
one that ships here: it is twenty lines, and most of them are the six gangs.

## Sending them home

These belong upstream. If a quirk here starts working for you, consider opening
it at [zigpy/zha-device-handlers](https://github.com/zigpy/zha-device-handlers)
so the next person never needs this repository. When one lands there, it comes
out of here.

## License

[MIT](LICENSE).
