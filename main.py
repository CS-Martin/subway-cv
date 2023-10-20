from src.utilities.config import configure_logging
from src.game import Game
from cv.cv_model import cvmodel
import logging
import multiprocessing

logger = logging.getLogger(__name__)

def run_game():
    # Start the game
    game = Game()
    game.run()

def run_cv_model():
    game_cv = cvmodel()
    game_cv.run()

if __name__ == "__main__":
    # Configure logging
    configure_logging()

    # Use 'spawn' as the start method for creating processes
    multiprocessing.set_start_method('spawn')

    # Create separate processes for the game and computer vision
    game_process = multiprocessing.Process(target=run_game)
    cv_process = multiprocessing.Process(target=run_cv_model)

    # Start both processes
    game_process.start()
    cv_process.start()

    # If the game process ends, terminate the computer vision process
    game_process.join()
    cv_process.terminate()

