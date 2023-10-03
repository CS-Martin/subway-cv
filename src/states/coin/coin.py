from src.states.base_entity import BaseEntity
from src.states.state_manager import StateManager
from src.states.coin.coin_states import IdleState
import logging
import pygame

logger = logging.getLogger(__name__)

class Coin(BaseEntity):
    def __init__(self, game, lane):
        # Initialize the coin
        logger.debug('Initializing coin')

        # Call the constructor of the parent class BaseEntity
        coin_sprite = pygame.image.load('assets/Coin-1.png')
        super().__init__(game, 50, 50, coin_sprite, lane=lane)  

        # Create a StateManager object with an IdleState object as the initial state
        self.state_manager = StateManager(IdleState())

        # Set the lane position of the coin
        self.set_lane_position(lane)

        # Set the starting y position of the coin
        self.set_start_y()

        # Set the game object
        self.game = game

        # Log that the coin has been initialized
        logger.info('Coin initialized at lane {}'.format(self.lane))

    def handle_event(self, event):
        # Handle the event using the StateManager object
        self.state_manager.handle_event(self, event)

    def update(self):
        # Log the lane of the coin
        logger.debug('Coin lane: {}'.format(self.lane))

        # Scroll the coin with the screen
        self.rect.y += self.game.scroll_speed

        # Log the y position of the coin
        logger.debug('Coin rect.y: {}'.format(self.rect.y))

        # Remove the coin if it goes off the screen
        if self.rect.y > self.game.screen_height:
            logger.debug('Removing coin')
            self.kill()

        # Update the state of the coin using the StateManager object
        self.state_manager.update(self)

    def draw(self, screen):
        # Draw the coin using the StateManager object
        self.state_manager.draw(self, screen)

        # Call the draw method of the parent class BaseEntity
        super().draw(screen)

        
