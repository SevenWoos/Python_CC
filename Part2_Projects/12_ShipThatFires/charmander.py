import pygame

class Charmander:
  """A class to manage the Charmander."""

  def __init__(self, bs_game):
    """Initialize the Charmander and set its starting position."""
    self.screen = bs_game.screen
    self.screen_rect = bs_game.screen.get_rect()

    # Load the ship image and get its rect.
    self.image = pygame.image.load('charmander.png')
    self.image = pygame.transform.scale(self.image, (100, 100))  # (width, height)

    self.rect = self.image.get_rect()

    # Start each new ship at the bottom center of the screen.
    self.rect.midbottom = self.screen_rect.midbottom

  def blitme(self):
    """Draw the ship at its current location."""
    self.screen.blit(self.image, self.rect)