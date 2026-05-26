class Settings:
  """A class to store all settings for raindrops Pygame."""
  
  def __init__(self):
    """Initialize the game's settings."""
    # Screen Settings.
    self.screen_width = 1200
    self.screen_height = 800
    self.bg_color = (169, 169, 180)
    
    # Raindrop Settings
    self.raindrop_speed = 3.0