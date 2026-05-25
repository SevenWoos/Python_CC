import sys

import pygame
from random import randint

from settings import Settings
from raindrop import Raindrop

class RainyDay:
  """Overall class to manage game assets and behavior."""
  
  def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()
    
    self.clock = pygame.time.Clock()
    self.settings = Settings()
    
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Rainy Day")
    
    self.raindrops = pygame.sprite.Group()
    
    self._create_raindrops()
    
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      self._check_events()
      self._update_raindrops()
      self._update_screen()
      self.clock.tick(60)
      
  def _check_events(self):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
  
  def _check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_q:
      sys.exit()
      
  def _create_raindrop(self, x_position, y_position):
    """Create a raindrop and place it on the row."""
    new_raindrop = Raindrop(self)
    # Random x offset
    new_raindrop.x = x_position + randint(-10, 10)
    new_raindrop.rect.x = new_raindrop.x
    # Random y offset
    new_raindrop.rect.y = y_position + randint(0, self.settings.screen_height)
    new_raindrop.y = float(new_raindrop.rect.y)
    self.raindrops.add(new_raindrop)
    
  def _create_raindrops(self):
    """Create a scatter of raindrops."""
    # Create a raindrop and keep adding raindrops until there is no more space in the row.
    raindrop = Raindrop(self)
    raindrop_width, raindrop_height = raindrop.rect.size
    
    current_x, current_y = raindrop_width, raindrop_height
    while current_y < (self.settings.screen_height - raindrop_height):
      while current_x < (self.settings.screen_width - 2 * raindrop_width):
        self._create_raindrop(current_x, current_y)
        current_x += 2 * raindrop_width
      
      current_x = raindrop_width
      current_y += 2 * raindrop_height
      
      
  def _update_raindrops(self):
    """Update position of raindrops and remove the ones that have fallen off screen."""
    self.raindrops.update()
    for raindrop in self.raindrops.copy():
      if raindrop.rect.top >= self.settings.screen_height:
        self.raindrops.remove(raindrop)
    
    # Replenish raindrops when they've all fallen off
    if not self.raindrops:
      self._create_raindrops()
      
  def _update_screen(self):
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill(self.settings.bg_color)
    
    self.raindrops.draw(self.screen)
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()
    

if __name__ == '__main__':
  rd = RainyDay()
  rd.run_game()
