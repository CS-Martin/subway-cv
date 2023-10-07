from src.entities.base_entity import BaseEntity
from src.entities.state_manager import StateManager
from src.entities.train.train_states import IdleState, MovingState
from src.utilities.constants import TRAIN_SPRITES, TRAIN_HEIGHTS
import logging
import random
import pygame

logger = logging.getLogger(__name__)

class Train(BaseEntity):
    def __init__(self, game, lane, is_moving=False):
        logger.debug('Initializing train')

        self.height = random.choice(TRAIN_HEIGHTS)
        self.train_sprites = [pygame.transform.scale(pygame.image.load(train), (100, self.height))
                            for train in TRAIN_SPRITES]  
        
        self.current_frame = 0
        self.frame_counter = 0
        self.frame_delay = 6     

        super().__init__(game, 50, self.height, (255, 0, 0), lane=lane)

        self.state_manager = StateManager(IdleState()) if not is_moving else StateManager(MovingState())
        self.set_lane_position(lane) 
        self.set_start_y()
        self.game = game
        logger.info('Train initialized at lane {} with height {}'.format(self.lane, self.height))

    def handle_event(self, event):
        self.state_manager.handle_event(self, event)

    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.train_sprites)
            self.image = self.train_sprites[self.current_frame]
            self.frame_counter = 0

        logger.debug('Train lane: {}'.format(self.lane))
        logger.debug('Train height: {}'.format(self.height))
        logger.debug('Train rect.y: {}'.format(self.rect.y))
        
        self.rect.y += self.game.scroll_speed 

        if self.rect.y > self.game.screen_height:
            logger.debug('Removing train')
            self.game.trains.remove(self)

        self.state_manager.update(self)

    def draw(self, screen):
        self.state_manager.draw(self, screen)
        super().draw(screen)

        
