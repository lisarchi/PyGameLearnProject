import pygame
import sys
from random import randint

pygame.init()

game_font = pygame.font.Font(None, 30)

screen_width, screen_height = 1000, 1000
screen_color = (32, 52, 71)
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Awesome Shooter Game")

STEP = 0.5
fighter_image = pygame.image.load('images/fighter.png')
fighter_width, fighter_height = fighter_image.get_size()
fighter_x, fighter_y = screen_width/2 - fighter_width / 2, screen_height - fighter_height

ROCKET_STEP = 0.5
rocket_image = pygame.image.load('images/rocket.png')
rocket_width, rocket_height = rocket_image.get_size()
rocket_x, rocket_y = 0 , 0
rocket_was_fired = False

ALIEN_STEP = 0.1
alien_speed = ALIEN_STEP
alien_image = pygame.image.load('images/alien.png')
alien_width, alien_height = alien_image.get_size()
alien_x, alien_y = randint(0, screen_width - alien_width), 0

fighter_is_moving_left, fighter_is_moving_right = False, False

game_is_running = True

game_score = 0

while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = True
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = True
            if event.key == pygame.K_SPACE:
                rocket_was_fired = True
                rocket_x, rocket_y = fighter_x + fighter_width / 2 - rocket_width / 2, fighter_y - rocket_height

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                fighter_is_moving_left = False
            if event.key == pygame.K_RIGHT:
                fighter_is_moving_right = False

    if fighter_is_moving_left  and fighter_x >= STEP:
        fighter_x -= STEP
    if fighter_is_moving_right and fighter_x < screen_width - fighter_width:
        fighter_x += STEP

    alien_y += alien_speed

    if rocket_was_fired and rocket_y + rocket_height < 0:
        rocket_was_fired = False

    if rocket_was_fired:
        rocket_y -= ROCKET_STEP

    screen.fill(screen_color)
    screen.blit(fighter_image, (fighter_x, fighter_y))
    screen.blit(alien_image, (alien_x, alien_y))

    if rocket_was_fired:
        screen.blit(rocket_image, (rocket_x, rocket_y))

    game_score_text = game_font.render (f"Score is {game_score}", True, 'white')
    screen.blit(game_score_text, (20, 20))

    pygame.display.update()

    if alien_y+alien_height > fighter_y:
        game_is_running = False

    if rocket_was_fired and alien_x < rocket_x < alien_x + alien_width - rocket_width and alien_y < rocket_y < alien_y + alien_height - rocket_height:
        rocket_was_fired = False
        alien_x, alien_y = randint(0, screen_width - alien_width), 0
        alien_speed += ALIEN_STEP/5
        game_score += 1

game_over_text = game_font.render("Game Over", True, 'white')
game_over_rect = game_over_text.get_rect()
game_over_rect.center = (screen_width / 2, screen_height / 2)
screen.blit(game_over_text, game_over_rect)
pygame.display.update()
pygame.time.wait(5000)

pygame.quit()
