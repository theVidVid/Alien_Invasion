import sys

import pygame

"""
The sys module is used to exit the game when the quits.
The pygame module contains the functionality needed to make a game.
"""

def run_game():
    # Initializes game and creates a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    
    # Set the background color.
    bg_color = (74, 52, 145)
    
    # Start the main loop for the game.
    while True:
        
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        # Redraw the screen during each pass through the loop.
        screen.fill(bg_color)
        
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
run_game()
