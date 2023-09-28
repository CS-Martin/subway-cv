from src.states.base_entity import BaseEntity
from src.states.state_manager import StateManager
from src.states.player.player_states import RunState

class Player(BaseEntity):
    def __init__(self, game, lane):
        super().__init__(game, 50, 50, (0, 128, 255), lane=lane)  # Starting in the middle lane
        self.state_manager = StateManager(RunState())
        self.move_speed = 5  # Adjust move_speed as needed
        self.set_lane_position(lane)  # Call the set_lane_position method

    def handle_event(self, event):
        self.state_manager.handle_event(self, event)

    def update(self):
        self.state_manager.update(self)

    def draw(self, screen):
        self.state_manager.draw(self, screen)
        super().draw(screen)

        
