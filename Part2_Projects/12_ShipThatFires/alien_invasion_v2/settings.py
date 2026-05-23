class Settings:
  """A class to store all settnins for Alien Invasion V2."""
  
  def __init__(self):
    """Initialize the game's settings."""
    # Screen settings.
    self.screen_width = 500
    self.screen_height = 500
    self.bg_color = (230, 230, 230)
    self.ship_speed = 1.5
    
    # Bullet Settings
    self.bullet_speed = 2.0
    self.bullet_width = 15
    self.bullet_height = 3
    self.bullet_color = (60, 60, 60)
    self.bullets_allowed = 3
    