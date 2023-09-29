from src.states.base_entity import BaseEntity
from src.states.state_manager import StateManager
from src.states.player.player_states import RunState
import logging

logger = logging.getLogger(__name__)

class Player(BaseEntity):
    def __init__(self, game, lane):
        logger.debug('Initializing player')

        super().__init__(game, 50, 50, (0, 128, 255), lane=lane)  
        self.state_manager = StateManager(RunState())
        self.set_lane_position(lane)
        self.set_start_y()
        self.game = game
        self.score = 0

        logger.info('Player initialized at lane {}'.format(self.lane))

    def handle_event(self, event):
        self.state_manager.handle_event(self, event)

    def update(self):
        logger.debug('Player lane: {}'.format(self.lane))
        logger.debug('Score: {}'.format(self.score))

        self.state_manager.update(self)

    def draw(self, screen):
        self.state_manager.draw(self, screen)
        super().draw(screen)

        
