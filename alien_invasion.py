import pygame

from pygame.sprite import Group

from settings import Settings

from ship import Ship

import game_functions as gf


"""The pygame module contains the functionality needed to make a game."""

def run_game():
    # Initializes pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make ship instance
    ship = Ship(ai_settings, screen)
    
    # Make a group to store bullets in.
    bullets = Group()
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
