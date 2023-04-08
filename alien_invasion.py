import sys
from time import sleep

import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien

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
        pygame.display.set_caption("Alien Invasion")

        # Creates an instance to store game statistics.
        self.stats = GameStats(self)

        # Creates a Ship. The instance of AlienInvasion is 'self'.
        self.ship = Ship(self)

        # Creates the bullets that the Ship will fire.
        self.bullets = pygame.sprite.Group()

        # Creates the Aliens!
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Sets the background color of the screen.
        self.bg_color = (230, 230, 230)

        # Starts Alien Invasion in an active state.
        self.game_active = True


    def run_game(self):
        """
        Starts the main loop for the game.
        """
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
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

        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """
        Responds to bullet-alien collisions.
        """
        # Removes any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            # Destroys existing bullets and creates new fleet.
            self.bullets.empty()
            self._create_fleet()


    def _update_aliens(self):
        """
        Checks if the fleet is at an edge, then updates positions.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Looks for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Looks for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    
    def _create_alien(self, x_position, y_position):
        """
        Creates an alien and places it in the row.
        """
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)


    def _check_fleet_edges(self):
        """
        Responds appropriately if any aliens have reached an edge.
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break


    def _check_aliens_bottom(self):
        """
        Checks if any aliens have reached the bottom of the screen.
        """
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treats this the same as if the ship got hit.
                self._ship_hit()
                break


    def _change_fleet_direction(self):
        """
        Drops the entire fleet and changes the fleet's direction.
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def _create_fleet(self):
        """
        Creates the fleet of aliens.
        """
        # Creates an alien and keeps adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row: resets x value and increments y value.
            current_x = alien_width
            current_y += 2 * alien_height


    def _ship_hit(self):
        """
        Responds to the ship being hit by an alien.
        """
        if self.stats.ships_left > 0:
            # Decrements ships left.
            self.stats.ships_left -= 1

            # Gets rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Creates a new fleet and centers the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pauses.
            sleep(0.5)

        else:
            self.game_active = False


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

        # Draws the aliens.
        self.aliens.draw(self.screen)

        # Makes the most recently drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # Makes a game instance and runs the game.
    ai = AlienInvasion()
    ai.run_game()
