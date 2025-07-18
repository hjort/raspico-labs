import time
from time import sleep
from neopixel2 import Neopixel

numpix = 10
pixels = Neopixel(numpix, 0, 28, "GRB")
purple = (255, 0, 255)
yellow = (255, 100, 0)
orange = (255, 50, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
color0 = red

pixels.brightness(50)
# pixels.fill(orange)
# pixels.set_pixel_line_gradient(0, 9, green, blue)

# pixels.set_pixel_line_gradient(0, 3, red, yellow)
# pixels.set_pixel_line_gradient(4, 7, blue, green)
# pixels.set_pixel_line_gradient(8, 9, orange, purple )

pixels.set_pixel_line_gradient(0, 3, red, yellow)

# pixels.set_pixel_line(4, 5, yellow)
# pixels.set_pixel(9, (255, 255, 255))
pixels.show()

while True:
    
    for i in range(0, numpix - 3):
        pixels.fill((0,0,0))
        pixels.set_pixel_line_gradient(i, i+3, red, yellow)
        pixels.show()
        time.sleep(.1)

    for i in range(numpix - 3, 2, -1):
        pixels.fill((0,0,0))
        pixels.set_pixel_line_gradient(i-3, i, red, yellow)
        pixels.show()
        time.sleep(.1)

    break
    if color0 == red:
       color0 = yellow
       color1 = red
    else:
        color0 = red
        color1 = yellow
    pixels.set_pixel(0, color0)
    pixels.set_pixel(1, color1)
    pixels.show()
    time.sleep(1)
