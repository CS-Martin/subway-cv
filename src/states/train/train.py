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

        height = random.choice(TRAIN_HEIGHTS)
        self.train_sprites = [pygame.transform.scale(pygame.image.load(path), (100, height))
                               for path in ['assets/Firetruck/Firetruck1.png', 'assets/Firetruck/Firetruck2.png',
                                            'assets/Firetruck/Firetruck3.png', 'assets/Firetruck/Firetruck4.png',
                                            'assets/Firetruck/Firetruck5.png', 'assets/Firetruck/Firetruck6.png',]]
        self.current_frame = 0
        self.frame_counter = 0
        self.frame_delay = 3  # Adjust this for desired speed
        
        super().__init__(game, 100, height, self.train_sprites[0], lane=lane)
        self.state_manager = StateManager(IdleState()) if not is_moving else StateManager(MovingState())
        self.set_lane_position(lane) 
        self.set_start_y()
        self.height = height
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

        
