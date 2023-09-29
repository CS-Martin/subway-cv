from src.utilities.config import configure_logging
from src.game import Game
import logging

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Configure logging
    configure_logging()

    # Start the game
    game = Game()
    game.run()
