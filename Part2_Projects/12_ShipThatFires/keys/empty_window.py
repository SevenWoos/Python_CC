import sys

import pygame
from settings import Settings

class Window:
  
  def __init__(self):
    pygame.init()
    
    self.clock = pygame.time.Clock()
    self.settings = Settings()
    
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Empty Pygame Window")
    
  def run_game(self):
    while True:
      self._check_events()
      self.clock.tick(60)
      
  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      
      elif event.type == pygame.KEYDOWN:
        self._check_keydown_events(event)
  
  def _check_keydown_events(self, event):
    print(f"Key {event.key} pressed")


if __name__ == '__main__':
  window = Window()
  window.run_game()
