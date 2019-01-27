import pygame

class Ship():
    """Models a class representing a spaceship for the Alien Invader game."""
    
    def __init__(self, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        
        # Load the ship and get its rectangles.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        """
        Movement flag in its default state means the ship doesn't move either
        to the right or left side.
        """
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the ship's position based on the movement flag."""
        # While KEYDOWN press event is held, self.moving_right is True
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
