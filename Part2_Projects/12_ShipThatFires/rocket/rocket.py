import pygame

class Rocket:
  """A class to maange the rocket."""
  
  def __init__(self, rw_game):
    """Initialize the rocket and set its starting position."""
    self.screen = rw_game.screen
    self.screen_rect = rw_game.screen.get_rect()
    self.settings = rw_game.settings
    
    self.image = pygame.image.load('rocket.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (100, 100))
    self.rect = self.image.get_rect()
    
    self.rect.midbottom = self.screen_rect.midbottom
    
    self.x = float(self.rect.x)
    
    self.moving_left = False
    self.moving_right = False
    
  def update(self):
    if self.moving_left and self.rect.left > 0:
      self.x -= self.settings.rocket_speed
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.x += self.settings.rocket_speed
      
    self.rect.x = self.x
  
  def blitme(self):
    self.screen.blit(self.image, self.rect)
