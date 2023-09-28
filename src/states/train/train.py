# states/train/train.py
from src.states.base_entity import BaseEntity
from src.states.state_manager import StateManager
from src.states.train.train_states import TrainMoveState, TrainIdleState
import pygame

class Train(BaseEntity):
    def __init__(self, game, move_down=True, lane=None):
        super().__init__(game, 100, 50, (255, 0, 0), 800, 300, lane)  # Adjust size and color as needed
        self.move_speed = 5  # Adjust move_speed as needed

        if move_down:
            self.state_manager = StateManager(TrainMoveState())
        else:
            self.state_manager = StateManager(TrainIdleState())

    def handle_event(self, event):
        self.state_manager.handle_event(self, event)

    def update(self):
        self.state_manager.update(self)

    def draw(self, screen):
        self.state_manager.draw(self, screen)
        super().draw(screen)
