from neopixel2 import Neopixel
from time import sleep

# número de LEDs na fita
num_pixels = 10

# cor no formato RGB (red, green, blue) => de 0 a 255
color = (250, 0, 0)

# fita de LED ligada no pino 28 do RaspBerry Pi
my_strip = Neopixel(num_pixels, 0, 28, "GRB")

while True:
    for i in range(0, num_pixels):
        my_strip.fill((0,0,0))
        my_strip[i] = color
#         my_strip.set_pixel(i, color)
        my_strip.show()
        sleep(.1)

