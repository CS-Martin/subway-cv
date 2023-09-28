# states/coin/coin_states.py
from src.states.base_state import BaseState
from src.states.player.player_states import PickupCoinState
import pygame
import logging

logger = logging.getLogger(__name__)


class CoinIdleState(BaseState):
    def handle_event(self, coin, event):
        # Check for collision with the player
        player_rect = coin.game.player.get_rect()
        coin_rect = coin.get_rect()

        # Check for collision between player and coin
        if player_rect.colliderect(coin_rect):
            logger.info("Player picked up a coin")
            coin.game.score += 10  # Increase the player's score
            coin.game.remove_coin(coin)  # Remove the coin from the game
            coin.game.player.state_manager.change_state(PickupCoinState())
            logger.info("Player score: {}".format(coin.game.score))

    def update(self, coin):
        # Implement coin idle state update logic
        pass

    def draw(self, coin, screen):
        # Implement coin idle state draw logic
        screen.blit(coin.image, coin.rect)
