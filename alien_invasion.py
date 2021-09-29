import sys
from typing import Set

import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """This will help initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # set the background color
        self.bg_color = (230,230,230)

#This sets the display size of the screen and caption
#self.screen is called a "surface." A surface in Pygame is a part of the screen where a game element can be displayed
        self.screen = pygame.display.set_mode(self.settings.screen_width, self.settings.screen_height)
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    # this is the method that controls the game. 
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            #this for loop is considerded an "event loop" which is why we have to define the event.type later
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()

