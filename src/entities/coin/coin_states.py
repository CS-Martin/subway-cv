from src.entities.base_state import BaseState
import pygame
import logging 

logger = logging.getLogger(__name__)

class IdleState(BaseState):
    def handle_event(self, coin, event):
        logger.debug('Coin in idle state')

    def update(self, coin):
        player_collision = coin.rect.colliderect(coin.game.player)
        logger.debug('Player collision: {}'.format(player_collision))
        if player_collision:
            coin.state_manager.change_state(PickedUpState())

    def draw(self, coin, screen):
        pass

class PickedUpState(BaseState):
    def handle_event(self, coin, event):
        logger.debug('Coin in picked up state')

    def update(self, coin):
        coin.game.player.score += 1
        coin.kill()

    def draw(self, coin, screen):
        pass