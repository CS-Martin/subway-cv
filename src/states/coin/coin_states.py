from src.states.base_state import BaseState
import pygame
import logging 

logger = logging.getLogger(__name__)

class IdleState(BaseState):
    def handle_event(self, player, event):
        pass
    def update(self, player):
        pass

    def draw(self, player, screen):
        pass

class PickedUpState(BaseState):
    def handle_event(self, player, event):
        pass
    def update(self, player):
        pass

    def draw(self, player, screen):
        pass