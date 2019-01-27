import sys

import pygame

"""
The sys module is used to exit the game when the quits.
The pygame module contains the functionality needed to make a game.
"""

def check_events():
    """Respond to keypresses and mouse events."""
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
        
    # Make the most recently drawn screen visible.
    pygame.display.flip()    
