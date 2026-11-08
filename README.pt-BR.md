<h1 align="center">Tuya ZHA Quirks</h1>

<p align="center">
  Quirks Zigbee para aparelhos Tuya que o <code>zha-device-handlers</code> ainda<br>
  não cobre, empacotados para o Home Assistant carregar sozinho.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Home_Assistant-2024.1+-41BDF5?style=flat-square" alt="Home Assistant">
  <img src="https://img.shields.io/badge/licença-MIT-green?style=flat-square" alt="MIT">
</p>

<p align="center">
  <a href="README.md">English</a> · <b>Português</b> · <a href="README.es.md">Español</a>
</p>

---

## Por que isto existe

O ZHA reconhece um aparelho Zigbee pela string do fabricante. A Tuya lança o
mesmo hardware com prefixo de módulo novo a cada poucos meses, e cada prefixo
novo não casa com nada — o aparelho pareia, reporta bateria, e não expõe um
único interruptor.

Um quirk é o arquivinho que diz ao ZHA "este é aquele aparelho que você já
conhece". O upstream carrega centenas deles, mas um prefixo recém-saído leva um
ciclo de release para chegar lá. Este pacote carrega os que precisamos enquanto
isso.

## Aparelhos cobertos

| Aparelho | String do fabricante | O que ganha |
| --- | --- | --- |
| Nova Digital SA-6 Safira, interruptor de 6 teclas | `_TZE28C1000000_gxbdnfrh` | as seis teclas como entidades de switch |

## Instalação

1. **HACS** (ou Marketplace, a partir do 2026.11) → ⋮ → **Repositórios personalizados**
2. URL `https://github.com/constantini-ha/tuya-zha-quirks`, categoria *Integração*
3. Instale, reinicie, e vá em **Configurações → Dispositivos e serviços → Adicionar integração → Tuya ZHA Quirks**

Não há nada a configurar. Adicionar é o que carrega os quirks.

**Pareie o aparelho de novo depois**, ou reinicie mais uma vez. O ZHA casa o
quirk no momento em que entrevista o aparelho, então um que já estava pareado
mantém o formato com que foi entrevistado até ser entrevistado de novo.

## Escrevendo um

Solte um módulo em `custom_components/tuya_zha_quirks/quirks/`. Tudo que estiver
lá é importado no setup, e um quirk se registra no zigpy ao ser importado. Leia
o que já vem aqui: são vinte linhas, e a maioria delas são as seis teclas.

## Mandando para casa

O lugar deles é no upstream. Se um quirk daqui passar a funcionar para você,
considere abri-lo no [zigpy/zha-device-handlers](https://github.com/zigpy/zha-device-handlers)
para que a próxima pessoa nunca precise deste repositório. Quando um for
aceito lá, ele sai daqui.

## Licença

[MIT](LICENSE).
