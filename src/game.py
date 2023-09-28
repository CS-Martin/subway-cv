import pygame
import sys
from src.states.state_manager import StateManager
from src.states.player.player import Player

class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the game window
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Subway Surfers")

        # Create entities
        self.player = Player()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Delegate events to entities
            self.player.handle_event(event)

    def update_entities(self):
        # Update entities
        self.player.update()

    def draw_entities(self):
        # Draw entities
        self.screen.fill((255, 255, 255))  # Clear the screen
        self.player.draw(self.screen)

    def run(self):
        # Game loop
        while True:
            self.handle_events()
            self.update_entities()
            self.draw_entities()

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            pygame.time.Clock().tick(60)
