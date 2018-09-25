from pygame.locals import QUIT
import pygame as pg

import random
import math

WHITE = "#FFFFFF"
GREEN = "#00FF00"

FPS = 90
CLOCK = pg.time.Clock()

X, Y = 1700, 990

ORIG_X, ORIG_Y = 600, 600
GRAVITY = 0.01
BACKGROUND = pg.image.load('bg.png')
VELOCITY = 0.004

def hex2rgb(hexstr: str) -> tuple:
    """convert hex code to RGB tuple."""
    hexstr = hexstr.strip('#')
    # convert codes into a list of strings
    codes = map(lambda x: hexstr[x:x + 2], (0, 2, 4))
    # convert hex numbers to decimal
    decimal_codes = map(lambda x: int(x, 16), codes)
    return tuple(decimal_codes)


def main() -> None:
    display = pg.display.set_mode((X, Y))
    display.blit(BACKGROUND, (0, 0))

    pg.display.set_caption('HI.')

    run(display)

def run(display: pg.Surface) -> None:

    surf = pg.Surface((10, 10))
    surf.fill(hex2rgb(GREEN))

    start = (ORIG_X, ORIG_Y)
    target = (800, 400)

    display.blit(surf, target)
    
    triangle_a = start[1] - target[1]
    triangle_o = start[0] - target[0]
    
    
    x = ORIG_X
    y = ORIG_Y
    time = 0

    angle = math.atan(triangle_o / triangle_a)
    # trianlge_h = triangle_a / math.cos(angle)
    print(angle)

    vox = VELOCITY * math.cos(angle)
    voy = VELOCITY * math.sin(angle)
    
    
    print(angle)
    
    while True:
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                raise SystemExit
            
        time += 1
        
        x = ORIG_X + (vox * ORIG_X * time)
        y = ORIG_Y - (voy * ORIG_Y * time) + (angle * GRAVITY) * time ** 2

        print(x, y)

        display.blit(surf, (x, y))
        pg.display.update()
        # display.fill(hex2rgb(WHITE))
        CLOCK.tick(FPS)

if __name__ == '__main__':
    main()
