import pygame
import main

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([50, 50])
        self.image.fill((255, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 60)
        self.speed = 5

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed
