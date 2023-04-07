import pygame

class Ship:
    """
    A class to manage our Ship.
    """

    def __init__(self, ai_game):
        """
        Initializes the ship and sets its starting position.
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Loads the ship image and gets its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Starts each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """
        Draws the ship at its current location.
        """
        self.screen.blit(self.image, self.rect)