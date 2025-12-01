#
# '''
#
#    Subtask I: Create a screen and display, player,coin,NPC, and the screen.
#         Subtast I.A: Load an image of a sprite for the player, NPC, and coin(could just draw a yellow circle)
#             Subtask I.A.1: Import turtle,pygames, and random.*
#             Subtask I.A.2: Choose an image or create one.*
#             Subtask I.A.3: Display them on screen.*
#             Subtask I.A.4: Use turtle.screen to create a screen.*
#             Subtask I.A.5: Set screen width and height.*

import pygame, time

class Game:
    def __init__(self):
        pygame.init()
        #Initializes the game
        pygame.font.init()
        #Initializes the font for pygame

        self.screen = pygame.display.set_mode((800, 600))
        #Sets the screen size for the game
        self.screen.fill((255, 0, 0))
        #Sets the screen color for the game(white for now probably change in the future)
        self.run = True
        #Makes the game currently set to run
        self.npc1 = NPC()
        #Creates the timer

        self.timer = Timer(30)
        #Calls the timer class


    def game_time(self):
        #Main loop for the game to run essentially saying while the game is running doe everything within this.
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.timer.update()
            #calls the update part of the timer class to make sure its updating it while the game is running
            self.screen.fill((255, 255, 255))
            #Keeps screen updating with game
            self.screen.blit(self.npc1.surf, (250, 250))
            #Puts the NPC's current position on the screen.
            self.timer.display(self.screen)
            # Displays it the timer after the screen is drawn, you have to keep it here or it wont display.
            pygame.display.update()
        pygame.quit()

class NPC:

    def __init__(self):
        self.surf = pygame.image.load("pygames_character.png")
        self.rect = self.surf.get_rect()
        pygame.display.set_caption("pygames_character.png")



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

        if self.time_left <0:
            self.time_left = 0
        #This stops it from ever being negative

    def display(self,screen):

        font = pygame.font.SysFont("arial", 30)
        #Gives the clock a font
        timer_screen = font.render(str(self.time_left), True, (0, 0, 0))
        #Gives the font a color, makes it true, and gives it the string to put at the top in this case being the timer
        screen.blit(timer_screen, (10, 10))
        #Puts it onto the screen with 10,10 being the size.




def main():

    game = Game()
    game.game_time()

if __name__ == "__main__":

    main()
