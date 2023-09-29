import pygame
import sys
from src.states.player.player import Player
from src.states.coin.coin import Coin
from src.utilities.constants import WIDTH, HEIGHT, NUM_LANES, LANE_GAP, LANE_WIDTH, TOTAL_WIDTH, DESIRED_FPS
from src.states.base_entity import BaseEntity
import random

class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the game window
        self.screen_width, self.screen_height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Subway Surfers")

        self.num_lanes = NUM_LANES
        self.lane_width = LANE_WIDTH
        self.lane_gap = LANE_GAP
        self.total_width = TOTAL_WIDTH
        self.start_x = (self.screen_width - self.total_width) // 2
        self.lane_positions = [self.start_x + i * (self.lane_width + self.lane_gap) for i in range(self.num_lanes)]
        # [315, 375, 435]
        self.scroll_speed = 5

        # # Create entities
        self.entity_classes = {"Player": Player, "Coin": Coin}
        self.player = Player(self, self.lane_positions[1])
        self.coins = []

        self.last_coin_spawn_time = pygame.time.get_ticks()
        self.coin_spawn_interval = 3000  # 10 seconds in milliseconds


        # Game properties
        self.clock = pygame.time.Clock()

    def get_entity_class(self, class_name):
        return self.entity_classes.get(class_name, BaseEntity)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Delegate events to entities
            self.player.handle_event(event)

    def spawn_coin(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_coin_spawn_time > self.coin_spawn_interval:
            lane = random.choice(self.lane_positions)
            coin = Coin(self, lane)
            self.coins.append(coin)
            self.last_coin_spawn_time = current_time

    def update_entities(self):
        self.player.update()

        for coin in self.coins:
            coin.update()

    def draw_entities(self):
        # Draw entities
        self.screen.fill((255, 255, 255))  # Clear the screen
        self.draw_lanes()  # Draw lanes
        self.player.draw(self.screen)

        for coin in self.coins:
            coin.draw(self.screen)

    def draw_lanes(self):
        for lane in self.lane_positions:
            pygame.draw.rect(self.screen, (0, 0, 0), (lane, 0, self.lane_width, self.screen_height), 1)

    def run(self):
        # Game loop
        while True:
            self.handle_events()
            self.update_entities()
            self.draw_entities()

            self.spawn_coin()

            # Update the display
            pygame.display.flip()

            # Cap the frame rate
            self.clock.tick(DESIRED_FPS)
