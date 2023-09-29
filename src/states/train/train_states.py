from src.states.base_state import BaseState
import pygame
import logging 

logger = logging.getLogger(__name__)

class IdleState(BaseState):
    def handle_event(self, train, event):
        pass
    def update(self, train):
        pass

    def draw(self, train, screen):
        pass

class MovingState(BaseState):
    def handle_event(self, train, event):
        pass
    def update(self, train):
        train.rect.y += 2
        # self.train.rect.y += self.train.game.scroll_speed

    def draw(self, train, screen):
        pass