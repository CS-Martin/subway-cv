import pygame
from src.states.base_state import StateManager
from src.states.coin.coin_states import CoinIdleState

class Coin:
    def __init__(self, game):
        self.game = game
        self.state_manager = StateManager(CoinIdleState())
        self.image = pygame.Surface((30, 30))  # Example size; replace with your actual image
        self.image.fill((255, 215, 0))  # Example color; replace with your actual color
        self.rect = self.image.get_rect()
        self.rect.x = 100  # Example position; replace with your actual position
        self.rect.y = 100
