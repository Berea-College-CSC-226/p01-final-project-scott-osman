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

import pygame

class Game:
    def __init__(self):
        pygame.init()
        #Initializes the game
        self.screen = pygame.display.set_mode((800, 600))
        #Sets the screen size for the game
        self.screen.fill((255,255,255))
        #Sets the screen color for the game(white for now probably change in the future)
        self.run = True
        #Makes the game currently set to run

    def game_time(self):
        #Main loop for the game to run essentially saying while the game is running doe everything within this.
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            pygame.display.update()
        pygame.quit()

def main():

    game = Game()
    game.game_time()

if __name__ == "__main__":

    main()
