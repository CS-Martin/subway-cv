import pygame

class BaseEntity:
    def __init__(self, game, width, height, color, lane=None):
        self.game = game
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.lane = lane 
        self.rect.x = 0
        self.rect.y = 0
        
    
    def set_lane_position(self, lane):
        if lane is not None:
            self.lane = lane
            self.rect.x = lane

    def set_height(self):
        if isinstance(self, self.game.get_entity_class("Player")):
            self.rect.y = self.game.screen_height - self.rect.height
        else:
            # For other entities, start at the top
            self.rect.y = 0


    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect