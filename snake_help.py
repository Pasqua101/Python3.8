# course: ICS3 U1-01
# exercise: Pygame culminating assignment
# date: 2019-12-06
# student number: 349612614
# name: Marco Pasqua
# description: a basic start-up program
#
#   ______  ___                               ________
# ___   |/  /_____ ___________________      ___  __ \_____ _____________ ____  _______ _
# __  /|_/ /_  __ `/_  ___/  ___/  __ \     __  /_/ /  __ `/_  ___/  __ `/  / / /  __ `/
# _  /  / / / /_/ /_  /   / /__ / /_/ /     _  ____// /_/ /_(__  )/ /_/ // /_/ // /_/ /
# /_/  /_/  \__,_/ /_/    \___/ \____/      /_/     \__,_/ /____/ \__, / \__,_/ \__,_/
#                                                                   /_/


import pygame, sys, time,random
from pygame.constants import *
pygame.init()

#Setting the area for the board
screen = w,h = 800, 600
#Setting borders
board = pygame.display.set_mode(screen)
pygame.display.set_caption("Snake, Pygame culminating - Pasqua, Marco")

#colours
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)

#Setting variable for fps
fpsClock = pygame.time.Clock()

#Setting for the game
#Snake speed
speed = 10
x_dir = -1
y_dir = 0
#Spawn point for the part of the snake that is controlled by the player
snake_Pos = [400, 300]
#Position for the rest of the snake's body
snake_Body = [[390, 300], [380, 300], [370, 300]]
#Spawn point for the first piece of fruit
fruit = [300, 50]
#Variable for spawning fruit
fruit_Spawn = True
#Score variable is being used to count the player's score
score = 0

#Function for game over
def GameOver():
    """GameOver() : Will display the text that I put saying game over on top of the screen with the player's score and will stop the program """
    font = pygame.font.SysFont("monaco", 32)
    #Displays the string game over on the screen
    go_surf = font.render("Game over", True, red)
    #Draws a rectangle that allows the string to be displayed over the game
    go_rect = go_surf.get_rect()
    #allows the rectangle that is being drawn that displays the word Game over to be moved
    go_rect.midtop = (320,25)
    board.blit(go_surf, go_rect)
    Score(0)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    sys.exit(0)

#Function for showing the score
def Score(choice=1):
    score_font =  pygame.font.SysFont('monaco', 32)
    score_surf = score_font.render("score : [0]".format(score), True, white)
    score_rect = score_surf.get_rect()
    if choice == 1:
        score_rect.midtop = (80, 10)
    else:
        score_rect.midtop = (320, 100)
    board.blit(score_surf, score_rect)

while True:
    for event in pygame.event.get():
        if (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                pygame.quit()
                sys.exit(0)
            if (event.key == K_UP or event.key == K_w):
                if y_dir == 0:
                    y_dir = -1
                    x_dir = 0
            if (event.key == K_DOWN or event.key == K_s):
                if y_dir == 0:
                    y_dir = -1
                    x_dir = 0
            if (event.key == K_RIGHT or event.key == K_d):
                if y_dir == 0:
                    y_dir = -1
                    x_dir = 0
            if (event.key == K_LEFT or event.key == K_a):
                if y_dir == 0:
                    y_dir = -1
                    x_dir = 0
    #Snake body mechanics
    snake_Body.insert(0, list(snake_Pos))
    if snake_Pos == fruit:
        fruit_Spawn = False
        score += 1
    else:
        # Allows the snake's body to continue
        snake_Body.pop()
    if fruit_Spawn == False:
        fruit = [random.randrange(1, w // 10) * speed, random.randrange(1, h // 10) * speed]
        fruit_Spawn = True
        
    board.fill(black)
    for pos in snake_Body:
        pygame.draw.rect(board, green, pygame.Rect(pos[0], pos[1], speed, speed))
    pygame.draw.rect(board, red, pygame.Rect(fruit[0], fruit[1], speed, speed))

    #Setting Boundaries
    if snake_Pos[0] >= w or snake_Pos[0] < 0:
        print("condition 1")
        GameOver()
    if snake_Pos[1] >= h or snake_Pos[1] < 0:
        print("condition 2")
        GameOver()

    #If player were to hit themself
    for hit in snake_Body[1:]:
        if snake_Pos == hit:
            print("condition 3")
            GameOver()
    Score()
    pygame.display.update()
    fpsClock.tick(24)
