import pygame
import sys

pygame.init()

screen_width, screen_height = 1000, 1000
screen_color = (32, 52, 71)

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Awesome Shooter Game")

STEP = 0.5
fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x, fighter_y = screen_width/2 - fighter_width / 2, screen_height - fighter_height


fighter_is_moving_left, fighter_is_moving_right = False, False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left  and fighter_x >= STEP:
        fighter_x -= STEP
    if fighter_is_moving_right and fighter_x < screen_width - fighter_width:
        fighter_x += STEP

    screen.fill(screen_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))

    pygame.display.update()
