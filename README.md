# Foot Pedal Driven Sheet Music

Created to deal with changing pages when serving sheet music via a laptop/monitor.

Follows the [Adafruit Usb Foot Switch](https://learn.adafruit.com/usb-foot-switch/overview) build, with a custom written viewer that loads sheet music via image file or pdf, and scrolls through them with each foot press.

## Video
[Click here to see it working](https://streamable.com/wvg2b)

## Build log

Components with disassembled pedal
![](./images/IMG_20190209_164436.jpg)

Trinket 5V 8MHz
![](./images/IMG_20190209_164449.jpg)

Closeup of foot pedal switch and original cabling
![](./images/IMG_20190209_164455.jpg)

Stripped original cable
![](./images/IMG_20190209_164950.jpg)

Original hole and usb cable connector size. Used dremmel with router head to carve the hole big enough to fit the cable in
![](./images/IMG_20190209_165616.jpg)

Soldering the cables using a cheap amazon soldering kit (following instructions in the Adafruit tutorial)
![](./images/IMG_20190209_171650.jpg)

Excuse the terrible soldering job; but it works!
![](./images/IMG_20190209_173211.jpg)

Cable snaked in and screwed into place, and connected
![](./images/IMG_20190209_181230.jpg)

Programming the trinket based on some example code from the tutorial, with minor modifications to prevent button spam. I chose `n` as the key for "next". Also note board and programmer settings per the tutorial.
![](./images/programming-trinket.png)

Sloppily hot glueing everything into place
![](./images/IMG_20190209_183126.jpg)

Completed Switch
![](./images/IMG_20190209_183640.jpg)

Piano setup with monitor and macbook driving it; any cheap comp could work, but I had this macbook available which is honestly way overkill
![](./images/IMG_20190210_013937.jpg)

Sheet music pedal, and sustain pedal. Also shows macbook with usb-c/hdmi adapter driving the monitor, which also connects to a usb hub for mouse/keyboard/pedal
![](./images/IMG_20190210_013953.jpg)