class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1250
        self.screen_height = 600
        self.bg_color = (230,230,230)

        # Ship settings
        # This speed can be updated later as the game progresses
        self.ship_speed = 1.5

