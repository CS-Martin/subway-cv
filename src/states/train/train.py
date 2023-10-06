from src.states.base_entity import BaseEntity
from src.states.state_manager import StateManager
from src.states.train.train_states import IdleState, MovingState
from src.utilities.constants import TRAIN_HEIGHTS
import logging
import random
import pygame

logger = logging.getLogger(__name__)

class Train(BaseEntity):
    def __init__(self, game, lane, is_moving=False):
        logger.debug('Initializing train')

        self.train_sprite = (pygame.image.load("assets/Firetruck.png"))
        
        height = random.choice(TRAIN_HEIGHTS)
        super().__init__(game, 100, height, self.train_sprite, lane=lane)
        self.state_manager = StateManager(IdleState()) if not is_moving else StateManager(MovingState())
        self.set_lane_position(lane) 
        self.set_start_y()
        self.height = height
        self.game = game

        logger.info('Train initialized at lane {} with height {}'.format(self.lane, self.height))

    def handle_event(self, event):
        self.state_manager.handle_event(self, event)

    def update(self):
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

        
