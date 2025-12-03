'''

   Subtask I: Create a screen and display, player,coin,NPC, and the screen.
        Subtast I.A: Load an image of a sprite for the player, NPC, and coin(could just draw a yellow circle)
            Subtask I.A.1: Import turtle,pygames, and random.*
            Subtask I.A.2: Choose an image or create one.*
            Subtask I.A.3: Display them on screen.*
            Subtask I.A.4: Use turtle.screen to create a screen.*
            Subtask I.A.5: Set screen width and height.*
'''


import pygame, time, random

class Game:
    def __init__(self):
        pygame.init()  # Initializes all pygame modules.


        self.size = 800, 600
        # Creates the game window with width 800 and height 600.
        self.screen = pygame.display.set_mode(self.size)

        # Sets the title text that appears at the top of the window.
        pygame.display.set_caption("NPC Movement Game")

        # Boolean that controls whether the game loop is running.
        self.run = True

        # Creates an player object (defined below).
        self.player = Player()

        self.timer = Timer(15)
        #Creates the timer object

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

            # Moves the player based on the pressed keys.
            self.player.move(keys)
            self.timer.update()

            # Fills the screen with white (resets background each frame).
            self.screen.fill((255, 255, 255))

            # Draws the player image at its current (x, y) position.
            self.screen.blit(self.player.surf, (self.player.x, self.player.y))

            #Displays the timer over the screen
            self.timer.display(self.screen)

            # Updates the display so the player sees changes.
            pygame.display.update()



        # When the loop ends, pygame shuts down.
        pygame.quit()

class Player(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        # Loads the image file and keeps transparency.
        self.surf = pygame.image.load("pygames_character.png").convert_alpha()
        self.rect = self.surf.get_rect()
        #self.rect.move_ip(100,100)

        # Starting x and y position of the player.
        self.x = 250
        self.y = 250

        # How many pixels the player moves each frame.
        self.speed = 0.5

    # Movement function for player
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

        if self.x < -60:
            self.x += self.speed
        if self.x > 680:
            self.x -= self.speed
        if self.y > -70:
            self.y -= self.speed
        if self.y < 420:
            self.y += self.speed
        #Keeps the player within the walls of the game.

class Timer:
     def __init__(self, start):
        self.time_left = start
        #Makes the start the value listed when calling this class in the game(right now 30)
        self.time = time.time()
        #Saves the current number of seconds passing
     def update(self):
        current_time = time.time()
        #Records the current time it actually is, which is why the countdown works.
        if current_time - self.time >= 1:
            self.time_left -= 1
            self.time = current_time
            #This keeps the clock going down as long as the two values arnt the same and keeps updating the time.
        if self.time_left < 0:
           self.time_left = 0
           #This stops it from ever being negative
     def display(self, screen):
         font = pygame.font.SysFont("arial", 30)
         #Gives the clock a font
         timer_screen = font.render(str(self.time_left), True, (0, 0, 0))
         # Gives the font a color, makes it true, and gives it the string to put at the top in this case being the timer
         screen.blit(timer_screen, (10, 10))
         # Puts it onto the screen with 10,10 being the size.




def main():
    game = Game()   # Creates the Game object.
    game.game_time()  # Starts the main game loop.

# Makes sure the game only runs if this file is executed directly.
if __name__ == "__main__":
    main()
