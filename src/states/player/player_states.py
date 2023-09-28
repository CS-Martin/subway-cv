# player_states.py
from base_state import BaseState
import pygame

class RunState(BaseState):
    def handle_event(self, player, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.state_manager.change_state(JumpState())
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.state_manager.change_state(TurnState())

    def update(self, player):
        # Implement player running state update logic
        pass

    def draw(self, player, screen):
        # Implement player running state draw logic
        pass

class JumpState(BaseState):
    def handle_event(self, player, event):
        # Additional logic for handling events during a jump
        pass

    def update(self, player):
        # Implement player jump state update logic
        pass

    def draw(self, player, screen):
        # Implement player jump state draw logic
        pass

class TurnState(BaseState):
    def handle_event(self, player, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.state_manager.change_state(RunState())

    def update(self, player):
        # Implement player turn state update logic
        pass

    def draw(self, player, screen):
        # Implement player turn state draw logic
        pass

class CrashedState(BaseState):
    def handle_event(self, player, event):
        pass  # No input during the crashed state

    def update(self, player):
        # Implement player crashed state update logic
        pass

    def draw(self, player, screen):
        # Implement player crashed state draw logic
        pass


class CoinPickupState(BaseState):
    def handle_event(self, player, event):
        pass  # No additional events during pickup state

    def update(self, player):
        # Implement player pickup state update logic
        pass

    def draw(self, player, screen):
        # Implement player pickup state draw logic
        pass