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
    self.block_speed = 2.5
    
    # Bullet Settings.
    self.bullet_speed = 2.0
    self.bullet_width = 15
    self.bullet_height = 3
    self.bullet_color = (255, 103, 0)
    self.bullets_allowed = 3
    
    # Enemy Block Settings.
    