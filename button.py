import pygame.font


class Button:
    """
    A class to build buttons for the game.
    """
    def __init__(self, ai_game, msg):
        """
        Initializes button attributes.
        """
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Sets the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Builds the button's rect object and centers it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Preps the button's message.
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """
        Turns msg into a rendered image and centers text on the button.
        """
        self.msg_image = self.font.render(msg, 
                                          True, 
                                          self.text_color, 
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        """
        Draws a blank button and then draws the message.
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
