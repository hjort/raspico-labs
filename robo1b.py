from machine import Pin
from neopixel import NeoPixel
# from neopixel2 import Neopixel
import time

# número de LEDs na fita
num_pixels = 10

# cor no formato RGB (red, green, blue) => de 0 a 255
color = (255, 0, 0)
# color = (250, 250, 15)

# fita de LED ligada no pino 28 do RaspBerry Pi
my_strip = NeoPixel(Pin(28), num_pixels)
# my_strip = NeoPixel(num_pixels, 0, 28, "GRB")

# preencher todos com a mesma cor
my_strip.fill(color)

# efetivar mudança de cor
my_strip.write()
# my_strip.show()
