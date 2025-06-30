# Biblioteca time
import time
# Biblioteca instalada neopixel
from neopixel2 import Neopixel
 
# número de pixels
numpix = 10
# objeto strip com quantidade de pixels, máquina de estado, número GPIO e modo de cor
strip = Neopixel(numpix, 0, 28, "GRB")
 
# Cores com índices R, B e B em cada uma
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
pink = (255, 102, 178)
cyan = (0, 204, 204)
colors_rgb = (red, orange, yellow, green, blue, indigo, violet, pink, cyan)
 
# Índice de cores RGB, se houver a W adiciona mais um índice ou deixa 0
colors_rgbw = [color+tuple([0]) for color in colors_rgb]
colors_rgbw.append((0, 0, 0, 255))
 
# Remova o comentário emm colors_rgbw se a sua fita for RGBW
colors = colors_rgb
# colors = colors_rgbw
 
# Brilho da fita
strip.brightness(60)
 
# Laço de repetição
while True:
    for color in colors:
        for i in range(numpix):
            # Acende pixel do loop com cor vigente
            strip.set_pixel(i, color)
            # intervalo entre um pixel e outro
            time.sleep(0.02)
            strip.show()
