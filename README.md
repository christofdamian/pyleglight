# pyleglight

A Python module designed to control the [Elgato](https://www.elgato.com/en) brand Lights. For use in automation or in lieu of their [Control Center app](https://www.elgato.com/en/gaming/downloads) (when on a non-supported platform).

## Badges
[![Code on GitLab](https://img.shields.io/badge/Code-On%20Gitlab-green)](https://gitlab.com/obviate.io/pyleglight/)
[![PyPI - License](https://img.shields.io/pypi/l/leglight)](https://pypi.python.org/pypi/leglight/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/leglight.svg)](https://pypi.python.org/pypi/leglight/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/leglight)](https://pypi.python.org/pypi/leglight/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/leglight.svg)](https://pypi.python.org/pypi/leglight/)
[![PyPI status](https://img.shields.io/pypi/status/leglight.svg)](https://pypi.python.org/pypi/leglight/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)

## About the lights
As of this writing, the only compatible hardware is the [Elgato Key Light](https://www.elgato.com/en/gaming/key-light). This hardware operates on Wifi only, anounces itself on the network via [mDNS](https://en.wikipedia.org/wiki/Multicast_DNS) and is controllable via JSON [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). As the lights are not-multicolored the only available controls are on/off, brightness (0-100), and [color temperature](https://en.wikipedia.org/wiki/Color_temperature#Categorizing_different_lighting) (from 3000k to 7000k)

## Examples
When you know the IP, you can do things manually:
```
>>> import leglight
>>> myLight = leglight.LegLight('10.244.244.139',9123)
>>> print(myLight)
Elgato Light ABC12345689 @ 10.244.244.139:9123
>>> vars(myLight)
{'address': '10.244.244.139', 'port': 9123, 'name': '', 'server': '', 'productName': 'Elgato Key Light', 'hardwareBoardType': 53, 'firmwareBuildNumber': 192, 'firmwareVersion': '1.0.3', 'serialNumber': 'ABC12345689', 'display': 'Key Light One'}
>>> myLight.on()
>>> myLight.brightness(14)
>>> myLight.color(3500)
>>> myLight.off()
>>> 
```

Or you can use the discovery module:

```
>>> import leglight
>>> allLights = leglight.discover(2)
>>> print(allLights)
[Elgato Light ABC987654321 @ 10.244.244.142:9123, Elgato Light ABC12345689 @ 10.244.244.139:9123]
>>> for light in allLights:
...     light.on()
...     light.brightness(5)
...     light.color(3400)
```

## License
MIT

## Copyright
Elgato, Key Light and other product names are copyright of their owner, CORSAIR. 