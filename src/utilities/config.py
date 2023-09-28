import logging
import os 

def configure_logging():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    logging_path = os.path.join('logs', 'game.log')

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(logging_path),
            logging.StreamHandler()
        ]
    )
