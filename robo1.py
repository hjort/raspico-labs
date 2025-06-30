from neopixel2 import Neopixel

# número de LEDs na fita
num_pixels = 10

# cor no formato RGB (red, green, blue) => de 0 a 255
color = (250, 250, 15)

# fita de LED ligada no pino 28 do RaspBerry Pi
my_strip = Neopixel(num_pixels, 0, 28, "GRB")

# preencher todos com a mesma cor
my_strip.fill(color)

# efetivar mudança de cor
my_strip.show()