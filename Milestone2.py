
'''

   Subtask I: Create a screen and display, player,coin,NPC, and the screen.
        Subtast I.A: Load an image of a sprite for the player, NPC, and coin(could just draw a yellow circle)
            Subtask I.A.1: Import turtle,pygames, and random.*
            Subtask I.A.2: Choose an image or create one.*
            Subtask I.A.3: Display them on screen.*
            Subtask I.A.4: Use turtle.screen to create a screen.*
            Subtask I.A.5: Set screen width and height.*


'''



## Import all modules necessary for the game

import turtle
import random
import pygame

pygame.init() #pygame initializer

# Setting the screen size of the game

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))  #Requesting pygame to display and save it under the veriable Screen.


run = True  # Variable to keep screen running



pygame.display.set_caption("pygames_character.png") # Crate pycham npc

npc = pygame.image.load("pygames_character.png")   # make sure file exists


while run:  # This loop keeps the screen running until user click X button.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Fill screen
    screen.fill((255, 255, 255))


    # Draw the player image
    screen.blit(npc, (50, 50)) #set the player size to

    pygame.display.update()


pygame.quit() #Use to exit the screen
















