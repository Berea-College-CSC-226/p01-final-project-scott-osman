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
#
#
# '''
#
#
#
# ## Import all modules necessary for the game
#
# import turtle
# import random
# import pygame
#
# class Game_Setup:
#
#     def __init__(self):
#         self.screen_width = 800
#         self.screen_height = 600
#         self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))  # Requesting pygame to display and save it under the veriable Screen.
#     # Fill screen
#         self.screen.fill((255, 255, 255))
#         self.run = True  # Variable to keep screen running
#
#
#     # Draw the player image
#         #self.screen.blit(npc, (50, 50))  # set the player size to
#
#     def run(self):
#
#
#         #pygame.display.set_caption("pygames_character.png")  # Crate pycham npc
#
#         while self.run:  # This loop keeps the screen running until user click X button.
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     run = False
#
#             pygame.display.update()
#             pygame.quit()  # Use to exit the screen
#         #npc = pygame.image.load("pygames_character.png")  # make sure file exists
#
# # Setting the screen size of the game
#
#
#
#
# def main():
#
#     pygame.init()  # pygame initializer
#
#     game = Game_Setup()
#     game.run()
#
# main()
#
#

import pygame
pygame.init()
#screen = pygame.display.set_mode((800, 600))

class game_setup:


    def __init__(self):
