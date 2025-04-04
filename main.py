import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    dt = 0
    score = 0
  
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides(player1):
                sys.exit("\n\nGame over! \t \t Final Score: " + str(score) + "\n\n")
            for shot in shots:
                if asteroid.collides(shot):
                    shot.kill()
                    asteroid.split()
                    score += 1

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        

        pygame.display.flip()
        
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()