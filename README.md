# Foot Pedal Driven Sheet Music

Created to deal with changing pages when serving sheet music via a laptop/monitor.

Only really supports image files, so here's a pdf to image conversion using ghostscript/imagemagick
`FOR /R %G IN (*.pdf) DO magick -verbose -density 150 "%G" -quality 100 -background white -alpha off "%~dpnG"-%d.png`

## Version 2
First version was too loud. Imagine playing a quiet piano piece punctuated by loud **clicks** at page turns.

This new version uses a much quieter arcade button. I didn't like the size of the enclosure that I ordered, however any enclosure size will be dictated by the height of the button, which is too tall from a foot-usable perspective. Not sure how to deal with that.

So I slapped it into a very efficient and recycling friendly cardboard enclosure. Until I can replace it one day (maybe) or somehow sound dampen the first version. It has an ugly charm to it...

Really though, I just got tired of drilling ports into the plastic enclosure.

It also uses a [trinket M0](https://adafruit.com/product/3500) instead of the original trinket. Also runs on [python](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/circuitpython) instead.  
 

### Build log
![](./images/v2/IMG_20190526_172515.jpg)

![](./images/v2/IMG_20190526_172545.jpg)

![](./images/v2/IMG_20190526_172610.jpg)

![](./images/v2/IMG_20190526_182730.jpg)

![](./images/v2/IMG_20190526_182739.jpg)





## Version 1
Follows the [Adafruit Usb Foot Switch](https://learn.adafruit.com/usb-foot-switch/overview) build, with a custom written viewer that loads sheet music via image file, and scrolls through them with each foot press.

### Video
[Click here to see it working](https://streamable.com/wvg2b)

### Build log
Components with disassembled pedal
![](./images/v1/IMG_20190209_164436.jpg)

Trinket 5V 8MHz
![](./images/v1/IMG_20190209_164449.jpg)

Closeup of foot pedal switch and original cabling
![](./images/v1/IMG_20190209_164455.jpg)

Stripped original cable
![](./images/v1/IMG_20190209_164950.jpg)

Original hole and usb cable connector size. Used dremmel with router head to carve the hole big enough to fit the cable in
![](./images/v1/IMG_20190209_165616.jpg)

Soldering the cables using a cheap amazon soldering kit (following instructions in the Adafruit tutorial)
![](./images/v1/IMG_20190209_171650.jpg)

Excuse the terrible soldering job; but it works!
![](./images/v1/IMG_20190209_173211.jpg)

Cable snaked in and screwed into place, and connected
![](./images/v1/IMG_20190209_181230.jpg)

Programming the trinket based on some example code from the tutorial, with minor modifications to prevent button spam. I chose `n` as the key for "next". Also note board and programmer settings per the tutorial.
![](./images/v1/programming-trinket.png)

Sloppily hot glueing everything into place
![](./images/v1/IMG_20190209_183126.jpg)

Completed Switch
![](./images/v1/IMG_20190209_183640.jpg)

Piano setup with monitor and macbook driving it; any cheap comp could work, but I had this macbook available which is honestly way overkill
![](./images/v1/IMG_20190210_013937.jpg)

Sheet music pedal, and sustain pedal. Also shows macbook with usb-c/hdmi adapter driving the monitor, which also connects to a usb hub for mouse/keyboard/pedal
![](./images/v1/IMG_20190210_013953.jpg)
