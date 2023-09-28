from src.states.base_entity import BaseEntity
from src.states.state_manager import StateManager
from src.states.coin.coin_states import CoinIdleState

class Coin(BaseEntity):
    def __init__(self, game, lane):
        super().__init__(game, 30, 30, (255, 255, 0), 0, 0, lane=lane)  # Adjust size and color as needed
        self.state_manager = StateManager(CoinIdleState())

    def handle_event(self, event):
        self.state_manager.handle_event(self, event)

    def update(self):
        self.state_manager.update(self)

    def draw(self, screen):
        self.state_manager.draw(self, screen)
        super().draw(screen)
