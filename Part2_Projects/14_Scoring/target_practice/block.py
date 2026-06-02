import pygame

from settings import Settings

class Block:
  """A class to manage the user block."""
  
  def __init__(self, tp_game):
    """Initialize the user block and set its starting position."""
    self.screen = tp_game.screen
    self.settings = tp_game.settings
    self.color = self.settings.block_color
    
    # Draw the block at the middle left of the screen.
    self.screen_rect = tp_game.screen.get_rect()
    self.rect = pygame.Rect(0, 0, self.settings.block_width, self.settings.block_height)
    self.rect.midleft = self.screen_rect.midleft
    
    # Store the block's vertical position.
    self.y = float(self.rect.y)
    
    # Movement flags.
    self.moving_up = False
    self.moving_down = False
  
  def update(self):
    """Update the block's position based on the movement flag."""
    if self.moving_up and self.rect.top > 0:
      self.y -= self.settings.block_speed
    elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
      self.y += self.settings.block_speed
    
    # Update rect object from self.y.
    self.rect.y = self.y
    
  def draw_block(self):
    """Draw the block to the screen."""
    pygame.draw.rect(self.screen, self.color, self.rect)
  