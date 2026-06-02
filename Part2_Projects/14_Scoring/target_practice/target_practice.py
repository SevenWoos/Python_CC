import sys
from time import sleep
import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from block import Block
from enemy_block import EnemyBlock
from bullet import Bullet

class TargetPractice:
  """Overall class to manage game assets and behavior."""
  
  def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()
    
    # Start Target Practice in an inactive state.
    self.game_active = False
    
    self.clock = pygame.time.Clock()
    self.settings = Settings()
    
    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    self.screen_rect = self.screen.get_rect()
    pygame.display.set_caption("Target Practice")
    
    # Make the Play button.
    self.play_button = Button(self, "Play")
    
    # Create an instance to store game statistics.
    self.stats = GameStats(self)
    
    # Create an instance of the Block class.
    self.block = Block(self)
    
    # Create an instance of the EnemyBlock class.
    self.enemy_block = EnemyBlock(self)
    
    # Group that holds the bullets.
    self.bullets = pygame.sprite.Group()
    
    # Create a group to hold the enemy block.
    self.enemy_block_group = pygame.sprite.Group()
    self.enemy_block_group.add(self.enemy_block)
  
  def run_game(self):
    """Start the main loop for the game."""
    while True:
      self._check_events()
      if self.game_active:
        self.block.update()
        self._update_enemy_block()
        self._update_bullets()
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
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        self._check_play_button(mouse_pos)
  
  def _check_play_button(self, mouse_pos):
    """Start a new game when the player clicks Play."""
    button_clicked = self.play_button.rect.collidepoint(mouse_pos)
    if button_clicked and not self.game_active:
      # Reset the game statistics.
      self.stats.reset_stats()
      self.game_active = True
      
      # Get rid of any remaining bullets and enemy blocks.
      self.bullets.empty()
      self.enemy_block_group.empty()
      
      # Create a new enemy block and add it to the enemy_block_group.
      self._create_enemy_block()
      
      # Hide the mouse cursor.
      pygame.mouse.set_visible(False)
  
  def _check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_q:
      sys.exit()
    elif event.key == pygame.K_UP:
      self.block.moving_up = True
    elif event.key == pygame.K_DOWN:
      self.block.moving_down = True
    elif event.key == pygame.K_SPACE:
      self._fire_bullet()
  
  def _check_keyup_events(self, event):
    if event.key == pygame.K_UP:
      self.block.moving_up = False
    elif event.key == pygame.K_DOWN:
      self.block.moving_down = False
      
  def _fire_bullet(self):
    """Create a new bullet and add it to the bullets group."""
    if len(self.bullets) < self.settings.bullets_allowed:
      new_bullet = Bullet(self)
      self.bullets.add(new_bullet)
  
  def _update_bullets(self):
    """Update position of bullets and get rid of old bullets"""
    # Apply update() method on all bullets to update their positions.
    self.bullets.update()
    # Get rid of bullets that have disappeared.
    for bullet in self.bullets.copy():
      if bullet.rect.left >= self.screen_rect.right:
        self.bullets.remove(bullet)
    
    # Check for any bullets that have hit the enemy block.
    self._check_bullet_enemy_block_collisions()
    
  def _check_bullet_enemy_block_collisions(self):
    """Respond to bullet and enemy block collisions."""
    collisions = pygame.sprite.groupcollide(self.bullets, self.enemy_block_group, True, True)
    # Respawn the enemy block if it is hit.
    if not self.enemy_block_group:
      # Destroy existing bullets and create a new enemy block.
      self.bullets.empty()
      sleep(1)
      self._create_enemy_block()
  
  def _create_enemy_block(self):
    """Create a new enemy block and add it to the enemy_block_group."""
    self.enemy_block = EnemyBlock(self)
    self.enemy_block_group.add(self.enemy_block)
        
  def _update_enemy_block(self):
    """Check if the enemy block has hit an edge, and update its position."""
    if self.enemy_block.check_edges():
      self._change_enemy_block_direction()
    self.enemy_block.update()
    
  def _change_enemy_block_direction(self):
    """Change the enemy block's direction."""
    self.settings.enemy_block_direction *= -1
      
  def _update_screen(self):
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill(self.settings.bg_color)
    
    # Draw the bullets.
    for bullet in self.bullets.sprites():
      bullet.draw_bullet()
    
    # Redraw the block at its current location.
    self.block.draw_block()
    
    # Redraw the enemy block at its current location ONLY if it is still in the enemy_block_group.
    if self.enemy_block in self.enemy_block_group:
      self.enemy_block.draw_enemy_block()
      
    # Draw the play button if the game is inactive.
    if not self.game_active:
      self.play_button.draw_button()
      pygame.mouse.set_visible(True)
    
    # Make the most recently drawn screen visible.
    pygame.display.flip()


if __name__ == '__main__':
  # Make a game instance, and run the game.
  tp = TargetPractice()
  tp.run_game()