import pygame
from pygame.sprite import Sprite

class Star(Sprite):
  """A class to represent a single star in the galaxy."""
  
  def __init__(self, sg_game):
    """Initialize the star and set its starting position."""
    super().__init__()
    self.screen = sg_game.screen
    
    # Load the star image and get its rect.
    self.image = pygame.image.load('images/star.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (40, 40))
    # self.image = pygame.image.load('images/rocket.png').convert_alpha()
    self.rect = self.image.get_rect()
    
    # self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
    # pygame.draw.circle(self.image, (255, 255, 255), (5, 5), 5)
    # self.rect = self.image.get_rect()
    
    # Start each new star near the top left of the screen.
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height
    
    # Store the star's exact horizontal position.
    self.x = float(self.rect.x)
