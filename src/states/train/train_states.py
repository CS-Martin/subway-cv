from src.states.base_state import BaseState

class TrainIdleState(BaseState):
    def handle_event(self, train, event):
        pass  # No event handling for idle state

    def update(self, train):
        # Idle trains do not move
        pass

    def draw(self, train, screen):
        # Implement train idle state draw logic
        screen.blit(train.image, train.rect)

class TrainMoveState(BaseState):
    def handle_event(self, train, event):
        # Handle events specific to moving trains (if needed)
        pass

    def update(self, train):
        train.rect.y += train.move_speed  # Move from top to bottom

        # If the train goes off the bottom of the screen, reset its position to the top
        if train.rect.top > train.game.screen_height:
            train.rect.y = 0

    def draw(self, train, screen):
        # Implement train move state draw logic
        screen.blit(train.image, train.rect)
