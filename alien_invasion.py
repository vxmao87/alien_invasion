import sys

import pygame

class AlienInvasion:
    """
    Overall class to manage game assets and behavior.
    """
    def __init__(self):
        """
        Initializes the game and creates game resources.
        """
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """
        Starts the main loop for the game.
        """
        while True:
            # Watches for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Makes the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # Makes a game instance and runs the game.
    ai = AlienInvasion()
    ai.run_game()
