from src.entities.base_state import BaseState
from src.utilities.constants import COIN_COLLISION_SOUND
import pygame
import logging 

logger = logging.getLogger(__name__)

class IdleState(BaseState):
    def handle_event(self, coin, event):
        logger.debug('Coin in idle state')

    def update(self, coin):
        player_collision = coin.rect.colliderect(coin.game.player)
        logger.debug('Player collision: {}'.format(player_collision))
        if player_collision:
            coin.state_manager.change_state(PickedUpState())

    def draw(self, coin, screen):
        pass

from src.entities.base_state import BaseState
from src.utilities.constants import COIN_COLLISION_SOUND
import pygame
import logging 

logger = logging.getLogger(__name__)

class PickedUpState(BaseState):
    def handle_event(self, coin, event):
        logger.debug('Coin in picked up state')

    def update(self, coin):
        coin.game.player.score += 1
        coin_collision_sound = pygame.mixer.Sound(COIN_COLLISION_SOUND)
        coin_collision_sound.set_volume(0.5) # Lower the volume to 50%
        coin_collision_sound.play()
        coin.kill()

    def draw(self, coin, screen):
        pass