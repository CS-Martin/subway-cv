from src.entities.base_entity import BaseEntity
from src.entities.state_manager import StateManager
from src.entities.player.player_states import RunState
from src.utilities.constants import PLAYER_SPRITES
import logging
import pygame

logger = logging.getLogger(__name__)

class Player(BaseEntity):
    def __init__(self, game, lane):
        logger.debug('Initializing player')

        self.char_sprites = [pygame.transform.scale(pygame.image.load(path), (50, 50))
                             for path in PLAYER_SPRITES]
        
        self.current_frame = 0
        self.frame_counter = 0
        self.frame_delay = 7  # Adjust this for desired speed
        
        super().__init__(game, 50, 50, self.char_sprites[0], lane=lane)  
        self.state_manager = StateManager(RunState())
        self.set_lane_position(lane)
        self.set_start_y()
        self.distance = 0
        self.game = game
        self.score = 0

        logger.info('Player initialized at lane {}'.format(self.lane))

    def handle_event(self, event):
        self.state_manager.handle_event(self, event)

    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.frame_delay:
            self.current_frame = (self.current_frame + 1) % len(self.char_sprites)
            self.image = self.char_sprites[self.current_frame]
            self.frame_counter = 0
        
        self.distance += self.game.scroll_speed

        logger.debug('Player lane: {}'.format(self.lane))
        logger.debug('Score: {}'.format(self.score))
        logger.debug('Distance: {}'.format(self.distance))
        
        self.state_manager.update(self)

    def draw(self, screen):
        self.state_manager.draw(self, screen)
        super().draw(screen)