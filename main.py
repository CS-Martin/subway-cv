from src.utilities.config import configure_logging
from src.game import Game
# from cv.cv_model import cvmodel
import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Configure logging
    configure_logging()

    # Start the game
    # game_cv = cvmodel()
    game = Game()
    game.run()
    # game_cv.run()
