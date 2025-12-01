'''

   Subtask I: Create a screen and display, player,coin,NPC, and the screen.
        Subtast I.A: Load an image of a sprite for the player, NPC, and coin(could just draw a yellow circle)
            Subtask I.A.1: Import turtle,pygames, and random.*
            Subtask I.A.2: Choose an image or create one.*
            Subtask I.A.3: Display them on screen.*
            Subtask I.A.4: Use turtle.screen to create a screen.*
            Subtask I.A.5: Set screen width and height.*
'''


import pygame

class Game:
    def __init__(self):
        pygame.init()  # Initializes all pygame modules.

        # Creates the game window with width 800 and height 600.
        self.screen = pygame.display.set_mode((800, 600))

        # Sets the title text that appears at the top of the window.
        pygame.display.set_caption("NPC Movement Game")

        # Boolean that controls whether the game loop is running.
        self.run = True

        # Creates an NPC object (defined below).
        self.npc1 = NPC()

    def game_time(self):
        # The loop keeps running as long as self.run is True.
        while self.run:
            # This processes all events (keyboard, mouse, close button, etc.)
            for event in pygame.event.get():
                # If the player clicks the X button, stop the loop.
                if event.type == pygame.QUIT:
                    self.run = False

            # Detects which keys are currently being pressed.
            keys = pygame.key.get_pressed()

            # Moves the NPC based on the pressed keys.
            self.npc1.move(keys)

            # Fills the screen with white (resets background each frame).
            self.screen.fill((255, 255, 255))

            # Draws the NPC image at its current (x, y) position.
            self.screen.blit(self.npc1.surf, (self.npc1.x, self.npc1.y))

            # Updates the display so the player sees changes.
            pygame.display.update()

        # When the loop ends, pygame shuts down.
        pygame.quit()

class NPC:
    def __init__(self):
        # Loads the image file and keeps transparency.
        self.surf = pygame.image.load("pygames_character.png").convert_alpha()

        # Starting x and y position of the NPC.
        self.x = 250
        self.y = 250

        # How many pixels the NPC moves each frame.
        self.speed = 0.2

    # Movement function for NPC
    def move(self, keys):
        # Move left when the LEFT arrow key is pressed.
        if keys[pygame.K_LEFT]:
            self.x -= self.speed

        # Move right when RIGHT arrow key is pressed.
        if keys[pygame.K_RIGHT]:
            self.x += self.speed

        # Move up when UP arrow key is pressed.
        if keys[pygame.K_UP]:
            self.y -= self.speed

        # Move down when DOWN arrow key is pressed.
        if keys[pygame.K_DOWN]:
            self.y += self.speed

def main():
    game = Game()   # Creates the Game object.
    game.game_time()  # Starts the main game loop.

# Makes sure the game only runs if this file is executed directly.
if __name__ == "__main__":
    main()
