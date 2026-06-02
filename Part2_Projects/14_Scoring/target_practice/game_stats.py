class GameStats:
  """Track statistics for Target Practice."""
  
  def __init__(self, tp_game):
    """Initialize statistics."""
    self.settings = tp_game.settings
    self.reset_stats()
    self.misses = 0
    self.max_misses = 3
  
  def reset_stats(self):
    """Initialize statistics that can change during the game."""
    self.enemy_blocks_left = self.settings.enemy_blocks_limit
    self.misses = 0