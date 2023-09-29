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
            elif event.key == pygame.K_LEFT:
                player.state_manager.change_state(TurnLeftState())
            elif event.key == pygame.K_RIGHT:
                player.state_manager.change_state(TurnRightState())

    def update(self, player):
        logger.info("Updating Player in RunState")

        # Log x and y
        logger.info("Player x: {}".format(player.rect.x))
        logger.info("Player y: {}".format(player.rect.y))

        # Log lane
        logger.info("Player lane: {}".format(player.lane))

    def draw(self, player, screen):
        pass

class TurnRightState(BaseState):
    def handle_event(self, player, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.state_manager.change_state(TurnLeftState())
            elif event.key == pygame.K_RIGHT:
                logger.info("Cannot move anymore right")

    def update(self, player):
        if player.lane == player.game.lane_positions[0]:
            logger.info("Setting lane position to {}".format(player.game.lane_positions[1]))
            player.set_lane_position(player.game.lane_positions[1])
        elif player.lane == player.game.lane_positions[1]:
            logger.info("Setting lane position to {}".format(player.game.lane_positions[2]))
            player.set_lane_position(player.game.lane_positions[2])
        elif player.lane == player.game.lane_positions[2]:
            logger.info("Cannot move anymore right")
        
        # Transition back to RunState
        player.state_manager.change_state(RunState())

    def draw(self, player, screen):
        pass

class TurnLeftState(BaseState):
    def handle_event(self, player, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                logger.info("Cannot move anymore left")
            elif event.key == pygame.K_RIGHT:
                player.state_manager.change_state(TurnRightState())

    def update(self, player):
        if player.lane == player.game.lane_positions[0]:
            logger.info("Cannot move anymore left")
        elif player.lane == player.game.lane_positions[1]:
            logger.info("Setting lane position to {}".format(player.game.lane_positions[0]))
            player.set_lane_position(player.game.lane_positions[0])
        elif player.lane == player.game.lane_positions[2]:
            logger.info("Setting lane position to {}".format(player.game.lane_positions[1]))
            player.set_lane_position(player.game.lane_positions[1])
        
        # Transition back to RunState
        player.state_manager.change_state(RunState())

    def draw(self, player, screen):
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