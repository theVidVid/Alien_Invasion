import sys

import pygame

from bullet import Bullet

"""
The sys module is used to exit the game when the quits.
The pygame module contains the functionality needed to make a game.
"""


def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        # KEYDOWN signifies the pressing of a key    
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            
        # KEYUP signifies the release of a pressed key    
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        # Move the ship to the right.
        ship.moving_right = True
                
    elif event.key == pygame.K_LEFT:
        # Move the ship to the left.
        ship.moving_left = True
        
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to bullets group.
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

        
def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        # The ship stops moving to the right.
        ship.moving_right = False
        
    elif event.key == pygame.K_LEFT:
        # The ship stops moving to the left.
        ship.moving_left = False    


def update_screen(ai_settings, screen, ship, bullets):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)
    
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
        
    # Make the most recently drawn screen visible.
    pygame.display.flip()    
