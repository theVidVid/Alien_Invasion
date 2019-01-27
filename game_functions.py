import sys

import pygame

"""
The sys module is used to exit the game when the quits.
The pygame module contains the functionality needed to make a game.
"""

def check_events(ship):
    """Respond to keypresses and mouse events."""
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        # KEYDOWN signifies the pressing of a key    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right.
                ship.moving_right = True
                
            elif event.key == pygame.K_LEFT:
                # Move the ship to the left.
                ship.moving_left = True
            
        # KEYUP signifies the release of a pressed key    
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # The ship stops moving to the right.
                ship.moving_right = False
                
            elif event.key == pygame.K_LEFT:
                # The ship stops moving to the left.
                ship.moving_left = False

            
def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
        
    # Make the most recently drawn screen visible.
    pygame.display.flip()    
