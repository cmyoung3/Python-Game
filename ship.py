import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load the ship image and get its rect.
        #what is rect representative? -> rectangle all objects in pygame are treated as rectangles
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)
        

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed
        #we are updating the position of the ship by using the ship_speed variable
        #defined in settings, instead of doing self.rect.x += 1

        #Update the rect object from self.x
        self.rect.x = self.x
            
    def blitme(self):
        """Draw the ship at its current location."""
        #blitme takes the image and draws it to the screen at the specificed location set above.
        self.screen.blit(self.image, self.rect)