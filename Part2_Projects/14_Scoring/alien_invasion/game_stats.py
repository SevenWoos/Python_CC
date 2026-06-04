import json
from pathlib import Path

class GameStats:
  """Track statistics for Alien Invasion.
  """
  
  def __init__(self, ai_game):
    """Initialize statistics."""
    self.settings = ai_game.settings
    self.reset_stats()
    
    # Load high score from file.
    path = Path('high_score.json')
    if path.exists():
      self.high_score = json.loads(path.read_text())
    else:
      self.high_score = 0
    self.level = 1
    
  def reset_stats(self):
    """Initialize statistics that can change during the game."""
    self.ships_left = self.settings.ship_limit
    self.score = 0