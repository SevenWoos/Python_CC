import sys

import pygame
from random import randint 

from settings import Settings
from star import Star

class StarryGalaxy:
  """Overall class to manage game assets and behavior."""
  
  def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()
    
    self.clock = pygame.time.Clock()
    self.settings = Settings()
    
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Starry Galaxy")
    
    self.stars = pygame.sprite.Group()
    
    self._create_stars()
    
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      self._check_events()
      self._update_screen()
      self.clock.tick(60)
      
  def _check_events(self):
    """Respond to keypresses and mouse events."""
    # Watch for keyboard and mouse events.
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
  
  def _check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_q:
      sys.exit()

  def _create_star(self, x_position, y_position):
    """Create a star and place it on the row."""
    new_star = Star(self)
    # Random x offset.
    new_star.x = x_position + randint(-10, 10)
    new_star.rect.x = new_star.x
    # Random y offset.
    new_star.rect.y = y_position + randint(-10, 10)
    self.stars.add(new_star)
    
  def _create_stars(self):
    """Create a galaxy of stars randomly dispersed."""
    # Create a star and keep adding stars until there is no more space in the row. Use the random() method.
    star = Star(self)
    star_width, star_height = star.rect.size
    
    current_x, current_y = star_width, star_height
    while current_y < (self.settings.screen_height - star_height):
      while current_x < (self.settings.screen_width - 2 * star_width):
        self._create_star(current_x, current_y)
        current_x += 2 * star_width
      
      # Finished a row; reset x value, and increment y value to start next row.
      current_x = star_width
      current_y += 2 * star_height
      
  def _update_screen(self):
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill(self.settings.bg_color)
    
    self.stars.draw(self.screen)
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()
    

if __name__ == '__main__':
  sg = StarryGalaxy()
  sg.run_game()