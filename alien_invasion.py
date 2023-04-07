import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

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

        # Runs the game in windowed mode.
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # # Runs the game in fullscreen mode.
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Alien Invasion")

        # Creates a Ship. The instance of AlienInvasion is 'self'.
        self.ship = Ship(self)

        # Creates the bullets that the Ship will fire.
        self.bullets = pygame.sprite.Group()

        # Sets the background color of the screen.
        self.bg_color = (230, 230, 230)


    def run_game(self):
        """
        Starts the main loop for the game.
        """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)


    def _check_events(self):
        """
        Responds to keyboard presses and events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    
    def _check_keydown_events(self, event):
        """
        Responds to keypresses.
        """
        if event.key == pygame.K_RIGHT:
            # Moves the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Moves the ship to the left.
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            # Quits the game when the 'q' button is pressed.
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """
        Responds to key releases.
        """
        if event.key == pygame.K_RIGHT:
            # Stops the ship from moving to the right.
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Stops the ship from moving to the left.
            self.ship.moving_left = False


    def _fire_bullet(self):
        """
        Creates a new bullet and adds it to the bullets group.
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    
    def _update_bullets(self):
        """
        Updates position of bullets and gets rid of old bullets.
        """
        # Updates bullet positions.
        self.bullets.update()

        # Gets rid of bullets that have disappeared from the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # # Test to see if the bullets are indeed removed.
        # print(len(self.bullets))


    def _update_screen(self):
        """
        Updates images on the screen, and flips them to the new screen.
        """
        # Redraws the screen during each pass of the loop.
        self.screen.fill(self.settings.bg_color)

        # Adds the bullets into the bullets group.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draws the Ship.
        self.ship.blitme()

        # Makes the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Makes a game instance and runs the game.
    ai = AlienInvasion()
    ai.run_game()
