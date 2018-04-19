import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf

def run_game():
    pygame.init()
    ai_seetings = Settings()
    screen = pygame.display.set_mode((ai_seetings.screen_width,ai_seetings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_seetings,screen)
    bullets = Group()
#    alien = Alien(ai_seetings,screen)
    aliens = Group()
    gf.create_fleet(ai_seetings,screen,aliens)

    while True:
        gf.check_events(ai_seetings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_seetings, screen, ship, aliens, bullets)

run_game()

