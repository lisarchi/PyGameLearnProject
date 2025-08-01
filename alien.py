import pygame
from random import randint
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ALIEN_STEP


class Alien:
    def __init__(self):
        self.image = pygame.image.load("images/alien.png")
        self.width, self.height = self.image.get_size()
        self.x, self.y = randint(0, SCREEN_WIDTH - self.width), 0
        self.step = ALIEN_STEP
        self.speed = self.step

    def update_position(self):
        self.y += self.speed

    def increase_speed(self):
        self.speed += self.step /2

    def reset(self):
        self.increase_speed()
        self.x, self.y = randint(0, SCREEN_WIDTH - self.width), 0

    def has_reached_fighter(self, fighter):
        return self.y + self.height > fighter.y