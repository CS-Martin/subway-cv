from src.states.base_state import BaseState
import pygame
import logging 

logger = logging.getLogger(__name__)

class IdleState(BaseState):
    def handle_event(self, coin, event):
        pass
    def update(self, coin):
        pass

    def draw(self, coin, screen):
        pass

class PickedUpState(BaseState):
    def handle_event(self, coin, event):
        pass
    def update(self, coin):
        pass

    def draw(self, coin, screen):
        pass