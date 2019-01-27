import sys

import pygame

from settings import Settings

from ship import Ship

"""
The sys module is used to exit the game when the quits.
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
        
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # Redraw the screen during each pass through the loop.
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
run_game()
