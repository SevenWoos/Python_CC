import sys

import pygame
from settings import Settings
from rocket import Rocket

class DeleteWindow:
  
  def __init__(self):
    pygame.init()
    
    self.clock = pygame.time.Clock()
    self.settings = Settings()
    
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Delete Window")
    
    self.rocket = Rocket(self)
    self.bg_color = (135, 206, 255)
    
  def run_game(self):
    while True:
      self._check_events()
      self.rocket.update()
      self._update_screen()
      self.clock.tick(60)
      
  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
        
      elif event.type == pygame.KEYDOWN:
        self._check_events_keydown(event)
      
      elif event.type == pygame.KEYUP:
        self._check_events_keyup(event)
        
  def _check_events_keydown(self, event):
    if event.key == pygame.K_RIGHT:
      self.rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
      self.rocket.moving_left = True
    elif event.key == pygame.K_q:
      sys.exit()
      
  def _check_events_keyup(self, event):
    if event.key == pygame.K_RIGHT:
      self.rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
      self.rocket.moving_left = False
      
  def _update_screen(self):
    self.screen.fill(self.bg_color)
    self.rocket.blitme()
    pygame.display.flip()

if __name__ == '__main__':
  delete_window = DeleteWindow()
  delete_window.run_game()