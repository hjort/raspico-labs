# import neopixel
# from machine import Pin
from neopixel2 import Neopixel
import time

pixPin=28
pixSize = 10

# pix=neopixel.NeoPixel(Pin(pixPin),pixSize)
# fita de LED ligada no pino 28 do RaspBerry Pi
pix = Neopixel(pixSize, 0, pixPin, "GRB")

def getRGB(deg):
    m=1/60
    if deg>=0 and deg<60:
       R=1
       G=0
       B=m*deg
    if deg>=60 and deg<120:
       R=1-m*(deg-60)
       G=0
       B=0
    if deg>=120 and deg<180:
       R=0
       G=m*(deg-120)
       B=1
    if deg>=180 and deg<240:
       R=0
       G=1
       B=1-m*(deg-180)
    if deg>=240 and deg<300:
       R=m*(deg-240)
       G=1
       B=0
    if deg>=300 and deg<360:
       R=1
       G=1-m*(deg-300)
       B=0
    myColor=(int(R*255),int(G*255),int(B*255))
    return myColor

while True:
    for deg in range(0,360,1):
        color=getRGB(deg)
        pix.fill(color)
#         pix.write()
        pix.show()
        time.sleep(.1/2)
        