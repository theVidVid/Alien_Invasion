import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A Class to manage bullets fired from the ship."""
    
    # Attributes required to create a bullet instance in alien_invasion.py
    def __init__(self, ai_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        # By calling super(), bullet inherits from Sprite class.
        super().__init__()
        self.screen = screen
        
        # Create a bullet rect at (0,0) and then set correct position.
        """
        The pygame.Rect() class is used when creating a rect from scratch,
            rather than working with an existing image.
        """
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, 
            ai_settings.bullet_height)
        # Sets the bullet's position to exactly match the ship's position.
        self.rect.centerx = ship.rect.centerx
        # Set the bullet rect on top of the ship.
        self.rect.top = ship.rect.top
        
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        
        # Store bullet color by calling ai_settings
        self.color = ai_settings.bullet_color
        
        # Store bullet speed by calling ai_settings 
        self.speed_factor = ai_settings.bullet_speed_factor
        
    
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position
        self.rect.y = self.y
        
        
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
