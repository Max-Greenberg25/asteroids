import pygame as gm
from constants import *

def main():
    gm.init()
    screen = gm.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in gm.event.get():
            if event.type == gm.QUIT:
                return
        screen.fill((0,0,0))


        gm.display.flip()


if __name__ == "__main__":
    main()