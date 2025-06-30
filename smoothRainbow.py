# Example showing use of HSV colors
import time
from neopixel2 import Neopixel

numpix = 10
strip = Neopixel(numpix, 0, 28, "GRB")

hue = 0
while(True):
    color = strip.colorHSV(hue, 255, 150)
    strip.fill(color)
    strip.show()
    time.sleep(.0125)
    hue += 150