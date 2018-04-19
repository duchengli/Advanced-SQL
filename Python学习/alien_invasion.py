import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    pygame.init()
    ai_seetings = Settings()
    screen = pygame.display.set_mode((ai_seetings.screen_width,ai_seetings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_seetings.bg_color)
        ship.blitme()
        pygame.display.flip()

run_game()

