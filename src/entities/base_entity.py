import pygame
from pygame.sprite import Sprite
from src.utilities.constants import START_Y

class BaseEntity(Sprite):
    def __init__(self, game, width, height, color_or_image, lane=None):
        super().__init__()
        self.game = game
        
        # Check if image parameter has image
        if isinstance(color_or_image, pygame.Surface):
            self.image = color_or_image
        else:
            self.image = pygame.Surface((width, height))
            self.image.fill(color_or_image)

        # Check if image is a coin sprite and resize it
        if self.game.get_entity_class("Coin") == type(self):
            self.image = pygame.transform.scale(self.image, (height, width))

        # Check if image is a train sprite and resize it
        if self.game.get_entity_class("Train") == type(self):
            self.image = pygame.transform.scale(self.image, (width, height))
            
        self.rect = self.image.get_rect()
        self.lane = lane 
        self.rect.x = 0
        self.rect.y = 0
    
    def set_lane_position(self, lane):
        if lane is not None:
            self.lane = lane
            self.rect.x = lane

            if self.game.get_entity_class("Coin") == type(self) or self.game.get_entity_class("Player") == type(self):
                self.rect.x += self.rect.width // 2



    def set_start_y(self):
        if isinstance(self, self.game.get_entity_class("Player")):
            self.rect.y = self.game.screen_height - (self.rect.height + 20)
        else:
            self.rect.y = START_Y  # Start off screen to give the illusion of spawning

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect