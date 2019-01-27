import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

"""
The pygame module contains the functionality needed to make a game.
"""

def run_game():
    # Initializes pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Make ship
    ship = Ship(screen)
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

run_game()
