import sys
import pygame

from settings import Settings

class TargetPractice:
  """Overall class to manage game assets and behavior."""
  
  def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()
    
    self.clock = pygame.time.Clock()
    self.settings = Settings()
    
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    self.screen_rect = self.screen.get_rect()
    pygame.display.set_caption("Target Practice")
  
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      self._check_events()
      self._update_screen()
      self.clock.tick(60)
      
  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
      elif event.type == pygame.KEYUP:
        self._check_keyup_events(event)
  
  def _check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_q:
      sys.exit()
  
  def _check_keyup_events(self, event):
    return
  
  def _update_screen(self):
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill(self.settings.bg_color)
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()


if __name__ == '__main__':
  # Make a game instance, and run the game.
  tp = TargetPractice()
  tp.run_game()