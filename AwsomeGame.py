####################
#Authors:Osman and Scott

####################



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

        # Creates a player object .
        self.player = Player()

        # creating coin and player objects
        self.coin = Coin()

        #Initialize the NPC as a list so it can hold all of the ones created. Not sure how to do it otherwise.
        self.npcs = [NPC()]
        #Made the NPC call into a list
        self.spawn_timer = 0


        self.timer = Timer(30)
        #Creates the timer object

        # Creates the score
        self.score = Score()

        #Checks to see if the game is over
        self.game_over = False

        #Checks to see if the game has started
        self.game_started = False

    def game_time(self):
        # The loop keeps running as long as self.run is True.
        while self.run:
            # This processes all events (keyboard, mouse, close button, etc.)
            for event in pygame.event.get():
                # If the player clicks the X button, stop the loop.
                if event.type == pygame.QUIT:
                    self.run = False
            if not self.game_started:
                self.display_start_screen()
                #Keeps the rest of the game from functioning
                continue


            #Checks to see if game_over == True
            if self.game_over:
                self.screen.fill((255,255,255))
                self.display_game_over()
                #Allows the player to restart by pressing r
                keys = pygame.key.get_pressed()
                if keys[pygame.K_r]:
                    self.restart()
                pygame.display.update()
                continue

            # Detects which keys are currently being pressed.
            keys = pygame.key.get_pressed()

            # Moves the player based on the pressed keys.
            self.player.move(keys)
            self.timer.update()

            #Adding NPCS
            self.spawn_timer += 1
            #Seems to be around 5 seconds
            if self.spawn_timer > 900:
                self.spawn_timer = 0
                self.npcs.append(NPC())


            if self.timer.time_left == 0:
                self.game_over = True

            # Fills the screen with white (resets background each frame).
            self.screen.fill((255, 255, 255))

            #This calls the NPC movement while also making sure to update the new ones to the screen
            for npc in self.npcs:
                npc.movement()
                self.screen.blit(npc.surf, (npc.x, npc.y))
                npc.rect.topleft = (npc.x, npc.y)

            # Draws the player image at its current (x, y) position. Also updates the rectangle with it.
            self.screen.blit(self.player.surf, (self.player.x, self.player.y))
            #Also updating the rectangle with it.
            self.player.rect.topleft = (self.player.x, self.player.y)

            #Coin
            self.screen.blit(self.coin.surf, (self.coin.x, self.coin.y))
            self.coin.rect.topleft = (self.coin.x, self.coin.y)

            #Tests to see if collisions are working and will end game upon collision
            for npc in self.npcs:
                if pygame.sprite.collide_rect(self.player, npc):
                    self.game_over = True

            #Coin collision
            if pygame.sprite.collide_rect(self.player, self.coin):
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




    def display_game_over(self):
        font = pygame.font.SysFont("arial", 80)
        subfont = pygame.font.SysFont("arial", 40)
        txt = font.render("GAME OVER", True, (0, 0, 0))
        self.screen.blit(txt, (self.size[0]//2-200, self.size[1]-500))
        score_txt = font.render("Final Score: " + str(self. score.value), True, (0, 0, 0))
        self.screen.blit(score_txt, (self.size[0]//2-200, self.size[1]-300))
        restart_txt = subfont.render("Press R to restart", True, (0, 0, 0))
        self.screen.blit(restart_txt, (self.size[0]//2-200, self.size[1]-100))

#Sets everything to its default state so the game can restart
    def restart(self):
        self.player = Player()
        self.coin = Coin()
        self.npcs = [NPC()]
        self.spawn_timer = 0
        self.timer = Timer(30)
        self.score = Score()
        self.game_over = False

    def display_start_screen(self):
        font = pygame.font.SysFont("arial", 50)
        start_txt = font.render("Press the Spacebar to Begin", True, (0,0,0))
        game_title = font.render("Welcome to Don't get caught", True, (0,0,0))
        self.screen.fill((255, 255, 255))
        self.screen.blit(game_title, (self.size[0]//2-250, self.size[1] //2 -150))
        self.screen.blit(start_txt, (self.size[0] // 2 -250, self.size[1] // 2 + 100))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.game_started = True






class Player(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        # Loads the image file and keeps transparency.
        original_image = pygame.image.load("pygames_character.png").convert_alpha()
        self.surf = pygame.transform.scale(original_image, (135, 135))

        self.rect = self.surf.get_rect()
        self.rect = self.rect.inflate(-40, -40)


        # Starting x and y position of the player.
        self.x = 250
        self.y = 450

        # How many pixels the player moves each frame.
        self.speed = 2


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
        self.rect = self.rect.inflate(-30, -30)

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
        elif self.y >= 540:
            self.path = 'north'
        elif self.x <= 0:
            self.path = 'east'
        elif self.x >= 720:
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
        self.rect = self.rect.inflate(-40, -40)

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
    game.game_time() # Starts the main game loop.


# Makes sure the game only runs if this file is executed directly.
if __name__ == "__main__":
    main()
