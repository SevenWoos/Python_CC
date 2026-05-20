import sys

import pygame

class BlueSky:
  """Make a Pygame window with a blue background"""

  def __init__(self):
    """Initialize the game and create a screen object."""
    pygame.init()

    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Sky")

    self.bg_color = (135, 206, 235)

  def run_game(self):
    """Start the main loop for the game."""
    while True:
      self._check_events()
      self._update_screen()
  
  def _check_events(self):
    """Respond to keypresses and mouse event."""
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

  def _update_screen(self):
    """Update images on the screen, and flip to the new screen."""
    self.screen.fill(self.bg_color)
    pygame.display.flip()

if __name__ == '__main__':
  # Make a game instance, and run the game.
  bs = BlueSky()
  bs.run_game()
