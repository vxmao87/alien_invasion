import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """
    Overall class to manage game assets and behavior.
    """
    def __init__(self):
        """
        Initializes the game and creates game resources.
        """
        pygame.init()

        # Initiates the Clock so that the game runs at the same frame rate on
        # all systems.
        self.clock = pygame.time.Clock()

        # Use the Settings provided.
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Creates a Ship. The instance of AlienInvasion is 'self'.
        self.ship = Ship(self)

        # Sets the background color of the screen.
        self.bg_color = (230, 230, 230)


    def run_game(self):
        """
        Starts the main loop for the game.
        """
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """
        Responds to keyboard presses and events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def _update_screen(self):
        """
        Updates images on the screen, and flips them to the new screen.
        """
        # Redraws the screen during each pass of the loop.
        self.screen.fill(self.settings.bg_color)
        # Draws the Ship.
        self.ship.blitme()

        # Makes the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Makes a game instance and runs the game.
    ai = AlienInvasion()
    ai.run_game()
