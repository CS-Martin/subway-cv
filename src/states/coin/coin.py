from src.states.base_entity import BaseEntity
from src.states.state_manager import StateManager
from src.states.coin.coin_states import IdleState
import logging
import pygame

logger = logging.getLogger(__name__)

class Coin(BaseEntity):
    def __init__(self, game, lane):
        logger.debug('Initializing coin')

        self.coin_sprites = [pygame.transform.scale(pygame.image.load(path), (50, 50))
                             for path in ['assets\Coin\Coin-1.png', 'assets\Coin\Coin-2.png',
                                          'assets\Coin\Coin-3.png', 'assets\Coin\Coin-4.png',
                                          'assets\Coin\Coin-5.png', 'assets\Coin\Coin-6.png',
                                          'assets\Coin\Coin-7.png']]
        self.current_frame = 0
        self.frame_counter = 0  
        self.frame_delay = 7 
        
        super().__init__(game, 50, 50, self.coin_sprites[0], lane=lane)  

        self.state_manager = StateManager(IdleState())
        self.set_lane_position(lane)
        self.set_start_y()
        self.game = game

        logger.info('Coin initialized at lane {}'.format(self.lane))

    def handle_event(self, event):
        self.state_manager.handle_event(self, event)

    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.coin_sprites)
            self.image = self.coin_sprites[self.current_frame]
            self.frame_counter = 0
            
        logger.debug('Coin lane: {}'.format(self.lane))
        self.rect.y += self.game.scroll_speed
        logger.debug('Coin rect.y: {}'.format(self.rect.y))

        if self.rect.y > self.game.screen_height:
            logger.debug('Removing coin')
            self.kill()

        self.state_manager.update(self)

    def draw(self, screen):
        self.state_manager.draw(self, screen)
        super().draw(screen)

        
