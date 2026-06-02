class Settings:
  
  def __init__(self):
    """Initialize the game's settings."""
    # Screen Settings.
    self.screen_width = 800
    self.screen_height = 800
    self.bg_color = (92, 148, 252)
    
    # Block Settings.
    self.block_width = 50
    self.block_height = 50
    self.block_color = (106, 190, 80)
    
    # Bullet Settings.
    self.bullet_width = 15
    self.bullet_height = 3
    self.bullet_color = (255, 103, 0)
    self.bullets_allowed = 5
    
    # Enemy Block Settings.
    self.enemy_block_width = 50
    self.enemy_block_height = 50
    self.enemy_block_color = (220, 50, 50)
    self.enemy_blocks_limit = 3
    
    # How quickly the game speeds up.
    self.speedup_scale = 1.1
    
    self.initialize_dynamic_settings()
    
  def initialize_dynamic_settings(self):
    """Initialize settings that change throughoyt thhe game."""
    # Block Settings.
    self.block_speed = 2.5
    
    # Bullet Settings.
    self.bullet_speed = 3.0
    
    # Enemy Block Settings.
    self.enemy_block_speed = 2.5
    self.enemy_block_direction = -1
  
  def increase_speed(self):
    """Increase speed settings as we level up."""
    self.block_speed *= self.speedup_scale
    self.bullet_speed *= self.speedup_scale
    self.enemy_block_speed *= self.speedup_scale
  