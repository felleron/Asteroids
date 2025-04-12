import sys
import pygame
from asteroidfield import AsteroidField
from constants import *
from asteroid import Asteroid
from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    #background
    #background_image = pygame.image.load("background.jpg").convert()

    #score
    score = 0 
    font = pygame.font.SysFont(None, 36)

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)


    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2)

    dt = 0
    while True:
        for event in  pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateable.update(dt)
        #collision check after update
        for asteroid in asteroids: 
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    score += 1
                    asteroid.split()
                    shot.kill()
                    
        screen.fill((0,0,0))
        #screen.blit(background_image, (0,0))
        for obj in drawable:
            obj.draw(screen)
        
        score_text = font.render(f"Score: {score}", True, (255,255,255))
        screen.blit(score_text, (10,10))

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()