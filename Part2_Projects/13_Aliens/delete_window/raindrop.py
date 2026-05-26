import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):
  """A class to represent a single raindrop in the game."""
  
  def __init__(self, rd_game):
    """Initialize the raindrop and set its starting position."""
    super().__init__()
    self.screen = rd_game.screen
    self.settings = rd_game.settings
    
    # Load the raindrop image and get its rect.
    self.image = pygame.image.load('images/raindrop.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (20, 20))
    self.rect = self.image.get_rect()
    
    # Start each new raindrop near the top left of the screen.
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height
    
    # Store the raindrop's exact vertical position.
    self.y = float(self.rect.y)
    
  def update(self):
    """Move the raindrop down the screen."""
    self.y += self.settings.raindrop_speed
    self.rect.y = self.y