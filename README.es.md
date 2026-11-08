<h1 align="center">Tuya ZHA Quirks</h1>

<p align="center">
  Quirks Zigbee para dispositivos Tuya que <code>zha-device-handlers</code> aún<br>
  no cubre, empaquetados para que Home Assistant los cargue solo.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Home_Assistant-2024.1+-41BDF5?style=flat-square" alt="Home Assistant">
  <img src="https://img.shields.io/badge/licencia-MIT-green?style=flat-square" alt="MIT">
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.pt-BR.md">Português</a> · <b>Español</b>
</p>

---

## Por qué existe

ZHA reconoce un dispositivo Zigbee por la cadena del fabricante. Tuya saca el
mismo hardware con un prefijo de módulo nuevo cada pocos meses, y cada prefijo
nuevo no coincide con nada: el aparato se empareja, informa batería y no expone
ni un interruptor.

Un quirk es el archivito que le dice a ZHA "este es el aparato que ya conoces".
Upstream lleva cientos, pero un prefijo recién salido tarda un ciclo de
publicación en llegar. Este paquete lleva los que necesitamos mientras tanto.

## Dispositivos cubiertos

| Dispositivo | Cadena del fabricante | Qué gana |
| --- | --- | --- |
| Nova Digital SA-6 Safira, interruptor de 6 teclas | `_TZE28C1000000_gxbdnfrh` | las seis teclas como entidades switch |

## Instalación

1. **HACS** (o Marketplace desde 2026.11) → ⋮ → **Repositorios personalizados**
2. URL `https://github.com/constantini-ha/tuya-zha-quirks`, categoría *Integración*
3. Instala, reinicia y ve a **Ajustes → Dispositivos y servicios → Añadir integración → Tuya ZHA Quirks**

No hay nada que configurar. Añadirlo es lo que carga los quirks.

**Vuelve a emparejar el dispositivo después**, o reinicia una vez más. ZHA asocia
el quirk cuando entrevista al aparato, así que uno ya emparejado conserva la
forma con la que fue entrevistado hasta que se le entreviste de nuevo.

## Escribir uno

Deja un módulo en `custom_components/tuya_zha_quirks/quirks/`. Todo lo que esté
ahí se importa en el arranque, y un quirk se registra en zigpy al importarse.
Lee el que ya viene: son veinte líneas, y la mayoría son las seis teclas.

## Enviarlos a casa

Su sitio es upstream. Si un quirk de aquí te funciona, plantéate abrirlo en
[zigpy/zha-device-handlers](https://github.com/zigpy/zha-device-handlers) para
que la siguiente persona nunca necesite este repositorio. Cuando uno entre allí,
sale de aquí.

## Licencia

[MIT](LICENSE).
