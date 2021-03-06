import pygame

class Settings():
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1440
        self.screen_height = 900
        self.bg_color = (74, 52, 145)
        
        # Ship settings
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = 178, 34, 34
        self.bullets_allowed = 3
        
        # Game song settings
        self.game_song = pygame.mixer.music.set_volume(0.5)
        self.game_song = pygame.mixer.music.load("GameSong/Grind.ogg")
        
        # Sound settings
        self.bullet_sound = pygame.mixer.Sound("Sounds/laser_2.wav")
        self.bullet_sound.set_volume(0.2)
        
        self.destroyed_alien = pygame.mixer.Sound("Sounds/explosion.wav")
        self.destroyed_alien.set_volume(0.2)
        
        self.ship_collision = pygame.mixer.Sound("Sounds/destroyed_ship.wav")
        self.ship_collision.set_volume(1)
        
        self.pause_in = pygame.mixer.Sound("Sounds/pause_in.wav")
        # ~ self.pause_in = pygame.set_volume(0.5)
        
        self.pause_out = pygame.mixer.Sound("Sounds/pause_out.wav")
        # ~ self.pause_out = pygame.set_volume(0.5)        
        
        self.level_refresh = pygame.mixer.Sound("Sounds/level_refresh.wav")
        self.level_refresh.set_volume(0.1)
        
        self.new_level = pygame.mixer.Sound("Sounds/new_level.wav")
        self.game_over = pygame.mixer.Sound("Sounds/game_over.wav")
        
        # Alien settings
        self.fleet_drop_speed = 10
        
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        
        # How quickly the alien point values increase
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5        
        self.bullet_speed_factor = 3        
        self.alien_speed_factor = 1
        
        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # Scoring
        self.alien_points = 50
        
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        # ~ print(self.alien_points)
