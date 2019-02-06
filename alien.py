import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """A class used to represent a single alien in the fleet."""
    
    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its rect attribute."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen.
        
        # Adding a space to the origin (0, 0) equal to the width of the ship.
        self.rect.x = self.rect.width
        # Adding a space to the origin (0, 0) equal to the height of the ship.
        self.rect.y = self.rect.height
        
        # Store the alien's exact position.
        self.x = float(self.rect.x)
    
    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
    
    
