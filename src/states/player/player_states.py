from src.states.base_state import BaseState
import pygame
import logging 

logger = logging.getLogger(__name__)

class RunState(BaseState):
    def handle_event(self, player, event):
        logger.info("Handling event in RunState")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.state_manager.change_state(JumpState())
            elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.state_manager.change_state(TurnState())

    def update(self, player):
        logger.info("Updating in RunState")
        # Log x and y
        logger.info("Player x: {}".format(player.rect.x))
        logger.info("Player y: {}".format(player.rect.y))
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
        logger.info("Handling event in TurnState")
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player.state_manager.change_state(RunState())

    def update(self, player):
        logger.info("Updating in TurnState")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            logger.info("Moving left")
            player.rect.x -= player.move_speed  # Adjust move_speed as needed
        elif keys[pygame.K_RIGHT]:
            logger.info("Moving right")
            player.rect.x += player.move_speed  # Adjust move_speed as needed

    def draw(self, player, screen):
        # Implement player turn state draw logic
        screen.blit(player.image, player.rect)

class CrashedState(BaseState):
    def handle_event(self, player, event):
        pass  # No input during the crashed state

    def update(self, player):
        # Implement player crashed state update logic
        pass

    def draw(self, player, screen):
        # Implement player crashed state draw logic
        pass


class PickupCoinState(BaseState):
    def handle_event(self, player, event):
        pass  # No additional events during pickup state

    def update(self, player):
        # Implement player pickup state update logic
        pass

    def draw(self, player, screen):
        # Implement player pickup state draw logic
        pass