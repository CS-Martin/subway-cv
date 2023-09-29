from src.states.base_entity import BaseEntity
from src.states.state_manager import StateManager
from src.states.coin.coin_states import IdleState
import logging

logger = logging.getLogger(__name__)

class Coin(BaseEntity):
    def __init__(self, game, lane):
        logger.debug('Initializing coin')

        super().__init__(game, 50, 50, (255, 255, 0), lane=lane)  
        self.state_manager = StateManager(IdleState())
        self.set_lane_position(lane)
        self.set_start_y()
        self.game = game

        logger.info('Coin initialized at lane {}'.format(self.lane))

    def handle_event(self, event):
        self.state_manager.handle_event(self, event)

    def update(self):
        logger.debug('Coin lane: {}'.format(self.lane))

        # Scroll the coin with the screen
        self.rect.y += self.game.scroll_speed
        logger.debug('Coin rect.y: {}'.format(self.rect.y))

        # Remove the coin if it goes off the screen
        if self.rect.y > self.game.screen_height:
            logger.debug('Removing coin')
            self.game.coins.remove(self)

        self.state_manager.update(self)

    def draw(self, screen):
        self.state_manager.draw(self, screen)
        super().draw(screen)

        
