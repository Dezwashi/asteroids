# from <file> import <variable> -> import varuable or function from <file>.py (no extension)

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock() #create Clock object, not visible
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0.0

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black") # screen is a variable, '.fill' is a method for applying color
        player.draw(screen)
        player.update(dt)
        pygame.display.flip() # update the display to the screen, it's what makes animations possible
        dt = clock.tick(60) / 1000 # Clock is a variable, method is for defining FPS

if __name__ == "__main__":
    main()
