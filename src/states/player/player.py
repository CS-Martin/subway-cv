# states/player/player.py
from src.states.base_state import StateManager
from src.states.player.player_states import RunState

class Player:
    def __init__(self, game):
        self.game = game
        self.state_manager = StateManager(RunState())

    def handle_event(self, event):
        self.state_manager.handle_event(self, event)

    def update(self):
        self.state_manager.update(self)

    def draw(self, screen):
        self.state_manager.draw(self, screen)
