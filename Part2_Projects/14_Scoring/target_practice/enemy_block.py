import pygame

class EnemyBlock:
  """A class to manage the enemy block."""
  
  def __init__(self, tp_game):
    """Initialize the enemy block and set its starting position."""
    self.screen = tp_game.screen
    self.settings = tp_game.settings
    self.color = self.settings.enemy_block_color
  
    # Draw the block at the middle right of the screen.
    self.screen_rect = tp_game.screen.get_rect()
    self.rect = pygame.Rect(0, 0, self.settings.enemy_block_width, self.settings.enemy_block_height)
    self.rect.midright = self.screen_rect.midright
    
    # Store the enemy block's vertical position.
    self.y = float(self.rect.y)
    
  def draw_enemy_block(self):
    """Draw the enemy block to the screen."""
    pygame.draw.rect(self.screen, self.color, self.rect)