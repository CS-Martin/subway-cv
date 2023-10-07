from src.entities.base_state import BaseState
from src.utilities.constants import PLAYER_CRASH_SFX, PLAYER_DEATH_SFX
import pygame
import logging 

logger = logging.getLogger(__name__)

class RunState(BaseState):
    def handle_event(self, player, event):
        logger.info('Player in RunState')
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.state_manager.change_state(JumpState())
            elif event.key == pygame.K_LEFT:
                player.state_manager.change_state(TurnLeftState())
            elif event.key == pygame.K_RIGHT:
                player.state_manager.change_state(TurnRightState())

    def update(self, player):
        for train in player.game.trains:
            train_collision = player.rect.colliderect(train)
            if train_collision:
                logger.info('Player collided with train')
                player.state_manager.change_state(CrashedState())
                return

    def draw(self, player, screen):
        pass

class TurnRightState(BaseState):
    def handle_event(self, player, event):
        logger.info('Player in TurnRightState')

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
        logger.info('Player in TurnLeftState')

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
        pass

    def update(self, player):
        pass

    def draw(self, player, screen):
        pass

class CrashedState(BaseState):
    def handle_event(self, player, event):
        logger.info('Player in CrashedState')

    def update(self, player):
        logger.info('Player in CrashedState update')

        # Sound game sfx
        player.game.game_sound.stop()
        
        # Play player crash sfx
        player_crash_sound = pygame.mixer.Sound(PLAYER_CRASH_SFX)
        player_death_sound = pygame.mixer.Sound(PLAYER_DEATH_SFX)
        player_crash_sound.play()
        player_death_sound.play()
        
        player.game.game_over = True

    def draw(self, player, screen):
        pass

