import pygame
import sys
from src.states.player.player import Player
from src.utilities.constants import WIDTH, HEIGHT, NUM_LANES, LANE_GAP, LANE_WIDTH, TOTAL_WIDTH
from src.states.base_entity import BaseEntity
class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the game window
        self.screen_width, self.screen_height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Subway Surfers")

        self.lane_width = LANE_WIDTH
        self.lane_gap = LANE_GAP
        self.total_width = TOTAL_WIDTH
        self.start_x = (self.screen_width - TOTAL_WIDTH) // 2
        self.lane_positions = [self.start_x + i * (LANE_WIDTH + LANE_GAP) for i in range(NUM_LANES)]

        # Create entities
        self.entity_classes = {"Player": Player}  # Add other entity classes as needed
        self.player = Player(self, self.lane_positions[1])

        # Game properties
        self.clock = pygame.time.Clock()

    def get_entity_class(self, class_name):
        return self.entity_classes.get(class_name, BaseEntity)
    
    def draw_lanes(self):
        lane_color = (192, 192, 192)  # Gray color
        for lane_x in self.lane_positions:
            pygame.draw.rect(self.screen, lane_color, (lane_x, 0, LANE_WIDTH, self.screen_height))  # Draw smaller lanes

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
        self.draw_lanes()  # Draw lanes
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
            self.clock.tick(60)
