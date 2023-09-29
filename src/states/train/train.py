from src.states.base_entity import BaseEntity
from src.states.state_manager import StateManager
from src.states.train.train_states import IdleState, MovingState
import logging
import random

logger = logging.getLogger(__name__)

class Train(BaseEntity):
    def __init__(self, game, lane, is_moving=False):
        # Randomize the height of the train
        heights = [200, 300, 400, 500]
        height = random.choice(heights)

        super().__init__(game, 50, height, (255, 0, 0), lane=lane)  # Starting in the middle lane
        self.state_manager = StateManager(IdleState())
        self.set_lane_position(lane)  # Call the set_lane_position method
        self.set_height()

    def handle_event(self, event):
        self.state_manager.handle_event(self, event)

    def update(self):
        logger.debug(self.lane)
        self.rect.y += self.game.scroll_speed  # Scroll the train with the screen
        self.state_manager.update(self)

    def draw(self, screen):
        self.state_manager.draw(self, screen)
        super().draw(screen)

        
