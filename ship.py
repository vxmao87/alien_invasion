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
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loads the ship image and gets its rect.
        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        # Starts each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Stores a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # The movement flag: starts with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    
    def update(self):
        """
        Updates the ship's position (x-value) based on the movement flag.
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Updates the rect object from self.x.
        self.rect.x = self.x


    def center_ship(self):
        """
        Centers the ship on the screen.
        """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


    def blitme(self):
        """
        Draws the ship at its current location.
        """
        self.screen.blit(self.image, self.rect)