from src.states.base_state import BaseState
import pygame
import logging 

logger = logging.getLogger(__name__)

class IdleState(BaseState):
    def handle_event(self, train, event):
        logger.debug('Train in idle state')

    def update(self, train):
        pass

    def draw(self, train, screen):
        pass

class MovingState(BaseState):
    def handle_event(self, train, event):
        logger.debug('Train in moving state')

    def update(self, train):
        train.rect.y += 2  # Moving trains have +2 speed

    def draw(self, train, screen):
        pass
