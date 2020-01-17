import pygame, sys, time
from pygame.constants import *
from random import randint

pygame.init()

# setting the size of the board
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
# Naming the window
pygame.display.set_caption("Snake")

# Spawn point for the snake
snake_point_x = int(w / 2)
snake_point_y = int(h / 2)

# Colour variables
red = pygame.Color(255, 51, 0)
green = pygame.Color(102, 255, 51)
blue = pygame.Color(0, 153, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

# Storing the colour variables in a list that the snake will use. Including black and white so when the user losses the snake will flash on the screen with black and white
snake_colours = (red, green, blue, white)

snake = [[snake_point_x, snake_point_y], [snake_point_x - 1, snake_point_y], [snake_point_x - 2, snake_point_y]]

# Making a variable similar to count that will increase the length of the snake.
length_snake = len(snake)


# Function for drawing pellets
def pellet(screen, x, y, s, c):
    """pellet(screen, x, y, s, x) : Draws the pellet on the board that the snake is moving on."""
    pygame.draw.rect(screen, c, (int(x * s), int(y * s), int(s), int(s)))


# FPS setting
fpsClock = pygame.time.Clock()

# X and y directions
x_dir = -1
y_dir = 0
# Snake's speed
speed = 10

# Board size
board_w = w / speed
board_h = h / speed
# Starting area for the snake
snake_start_x = board_w / 2
snake_start_y = board_h / 2

# Coordinates for snake
snake = [[snake_start_x, snake_start_y], [snake_start_x - 1, snake_start_y], [snake_start_x - 2, snake_start_y]]

# Creating speed for snake to move
speed = 10

done = False
screen.fill(black)
# Randomizing where the fruit will spawn
fruit = (randint(2, board_w - 2), randint(2, board_h - 2))
print(fruit)
pellet(screen, fruit[0], fruit[1], speed, red)

while not done:
    # Filling the screen black to have a dark mode version of snake
    screen.fill(pygame.Color(0, 0, 0))
    for event in pygame.event.get():
        if (event.type == KEYDOWN):
            if (event.key == K_ESCAPE):
                done = True
            if (event.key == K_UP):
                if y_dir == 0:
                    y_dir = -1
                    x_dir = 0
            if (event.key == K_DOWN):
                if y_dir == 0:
                    y_dir = 1
                    x_dir = 0
            if (event.key == K_RIGHT):
                if x_dir == 0:
                    x_dir = 1
                    y_dir = 0
            if (event.key == K_LEFT):
                if x_dir == 0:
                    x_dir = -1
                    y_dir = 0

    pellet(screen, snake[0][0], snake[0][1], speed, red)
    new_x = snake[-1][0] + x_dir
    new_y = snake[-1][1] + y_dir
    print(snake, new_x, new_y)
    print("---")

    # Code for making the pellets spawning on the screen each time the snake eats them
    if new_x == fruit[0] and new_y == fruit[1]:
        length_snake += 1
        fruit = (randint(2, board_w - 2), randint(2, board_h - 2))
        pellet(screen, fruit[0], fruit[1], speed, red)

    for i in range(len(snake)):
        if snake[i][0] == new_x and snake[i][1] == new_y:
            print('exit', snake)
            done = True

    snake.append([snake[-1][0] + x_dir, snake[-1][1] + y_dir])

    if snake[-1][0] >= board_w - 1:
        snake[-1][0] = 1
        length_snake += 1
    elif snake[-1][0] < 1:
        snake[-1][0] = board_w - 2
        length_snake += 1

    if snake[-1][1] >= board_h - 1:
        snake[-1][1] = 1
        length_snake += 1
    elif snake[-1][1] < 1:
        snake[-1][1] = board_h - 2
        length_snake += 1

    pellet(screen, snake[-1][0], snake[-1][1], speed, snake_colours[length_snake % len(snake_colours)])

    # window is not drawn until the update command is called

    fpsClock.tick(30)
    for i in range(len(snake)):
        pellet(screen, snake[i][0], snake[i][1], speed, red)
        pygame.display.update()
        # How fast the snake disappears from the screen when the player loses
        fpsClock.tick(24)
    pygame.display.update()
# How long it takes for the window to close
time.sleep(.8)
# Quit the program
sys.exit(0)
