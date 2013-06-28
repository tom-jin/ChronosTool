# ChronosTool.py
_Tool for programming TI eZ430-Chronos watches_

Features:

- Wireless firmware updates `rfbsl <txt file>`

- Sync time with local clock `sync`

- Read current watch status `status`

- Download watch memory `download`

- Erase watch memory `erase

- End communications `goodbye`

Changelog:

- public preview version `0.1`

- import rewritten `0.2`

- sync time accuracy fix

- verbosity option `0.3`

- noreset option

- acceleration data streaming

Example:
```	./ChronosTool.py -d /dev/ttyACM3 rfbsl eZChronos.txt```

Ressources:

- More info on the TI eZ430-Chronos:
  http://processors.wiki.ti.com/index.php/EZ430-Chronos

- OpenChronos, msp430-gcc-friendly TI firmware clone:
  https://github.com/poelzi/OpenChronos

- mspdebug, open-source debugger and programmer for the eZ430U:
  http://mspdebug.sourceforge.net/

- How to install the MSP430 toolchain under MAC OS X:
  http://www.senslab.info/?p=425
  (MacPorts version works fine for me.)
