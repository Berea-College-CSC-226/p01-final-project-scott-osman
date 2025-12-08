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

        # Creates an player object .
        self.player = Player()

        # creating coin and player objects
        self.coin = Coin()
        self.npc = NPC()


        self.timer = Timer(30)
        #Creates the timer object

        # Creates the score
        self.score = Score()

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

            #NPC movement call
            self.npc.movement()

            if self.timer.time_left == 0:
                self.run = False

            # Fills the screen with white (resets background each frame).
            self.screen.fill((255, 255, 255))

            # Draws the player image at its current (x, y) position. Also updates the rectangle with it.
            self.screen.blit(self.player.surf, (self.player.x, self.player.y))
            #Also updating the rectangle with it.
            self.player.rect.topleft = (self.player.x, self.player.y)

            #NPC
            self.screen.blit(self.npc.surf, (self.npc.x, self.npc.y))
            self.npc.rect.topleft = (self.npc.x, self.npc.y)

            #Coin
            self.screen.blit(self.coin.surf, (self.coin.x, self.coin.y))
            self.coin.rect.topleft = (self.coin.x, self.coin.y)

            #Tests to see if collisions are working
            if pygame.sprite.collide_rect(self.player, self.npc):
                font = pygame.font.SysFont("arial", 30)
                txt = font.render("oooohhh", True, (0, 0, 0))
                self.screen.blit(txt, (self.size[0]//2-50, self.size[1]-50))
            elif pygame.sprite.collide_rect(self.player, self.coin):
                self.score.add_point()
                #Moves it to a new random location
                self.coin.x = random.randint(0,770)
                self.coin.y = random.randint(0,570)
                self.coin.rect.topleft = (self.coin.x, self.coin.y)


            #Displays the timer and score over the screen
            self.timer.display(self.screen)
            self.score.display(self.screen)

            # Updates the display so the player sees changes.
            pygame.display.update()



        # When the loop ends, pygame shuts down.
        pygame.quit()

class Player(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        # Loads the image file and keeps transparency.
        original_image = pygame.image.load("pygames_character.png").convert_alpha()
        self.surf = pygame.transform.scale(original_image, (135, 135))

        self.rect = self.surf.get_rect()
        #self.rect.move_ip(100,100)


        # Starting x and y position of the player.
        self.x = 250
        self.y = 250

        # How many pixels the player moves each frame.
        self.speed = 3


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

        if self.x < -50:
            self.x += self.speed
        if self.x > 710:
            self.x -= self.speed
        if self.y > -40:
            self.y -= self.speed
        if self.y < 500:
            self.y += self.speed
        #Keeps the player within the walls of the game.

class NPC(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Load image
        original_image = pygame.image.load("RealNPC.png.png").convert_alpha()
        ## Reduce size of original image
        self.surf = pygame.transform.scale(original_image, (40, 60))
        # Get rect
        self.rect = self.surf.get_rect()

        # Starting position
        self.x = 400
        self.y = 100
        self.speed = .8

        self.directions = ['north', 'south', 'east', 'west']
        self.path = random.choice(self.directions)

    def get_direction(self):
        #Send in the other direction if on the wall to keep character confined within the screen
        if self.y <= 0:
            self.path = 'south'
        elif self.y >= 500:
            self.path = 'north'
        elif self.x <= 0:
            self.path = 'east'
        elif self.x >= 600:
            self.path = 'west'
        #Chances of them switching direction
        elif random.random() > .97:
            self.path = random.choice(self.directions)

    def movement(self):
        if self.path == 'north':
            self.y -= self.speed
        elif self.path == 'south':
            self.y += self.speed
        elif self.path == 'east':
            self.x += self.speed
        elif self.path == 'west':
            self.x -= self.speed
        self.rect.topleft = (self.x, self.y)
        #Calls a direction
        self.get_direction()


class Coin():
    def __init__(self):

        super().__init__()
        original_image = pygame.image.load("coin.png.png").convert_alpha()

        self.surf = pygame.transform.scale(original_image, (30, 30))

        self.rect = self.surf.get_rect()

        # Starting x and y position of the player.
        self.x = 120
        self.y = 380

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


class Score:
    def __init__(self):
        #initializes value
         self.value = 0

    def add_point(self):
        #When called updates the score by one.
        self.value += 1

    def display(self, screen):
         font = pygame.font.SysFont("arial", 30)
         txt = font.render("Score: " + str(self.value), True, (0, 0, 0))
         screen.blit(txt, (60, 10))


def main():
    game = Game()   # Creates the Game object.
    game.game_time()  # Starts the main game loop.

# Makes sure the game only runs if this file is executed directly.
if __name__ == "__main__":
    main()
