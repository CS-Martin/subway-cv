import pygame
import random
import sys
from src.entities.player.player import Player
from src.entities.coin.coin import Coin
from src.entities.train.train import Train
from src.utilities.constants import WIDTH, HEIGHT, NUM_LANES, LANE_GAP, LANE_WIDTH, TOTAL_WIDTH, DESIRED_FPS, START_X, LANE_POSITIONS, SCROLL_SPEED, COIN_GAP, ASPHALT_SPRITES
from src.entities.base_entity import BaseEntity
import random
from pygame.sprite import Group, GroupSingle

import logging

logger = logging.getLogger(__name__)

class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the game window
        self.screen_width, self.screen_height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Subway Surfers")

        # Game properties
        self.clock = pygame.time.Clock()    
        self.num_lanes = NUM_LANES
        self.lane_width = LANE_WIDTH
        self.lane_gap = LANE_GAP
        self.total_width = TOTAL_WIDTH
        self.start_x = START_X
        self.lane_positions = LANE_POSITIONS
        self.scroll_speed = SCROLL_SPEED
        self.game_over = False

        # Create entities
        self.entity_classes = {"Player": Player, "Coin": Coin, "Train": Train}
        self.player = Player(self, self.lane_positions[1])
        self.coins = Group()
        self.trains = Group()

        # Spawn timers
        self.last_coin_spawn_time = pygame.time.get_ticks()
        self.coin_spawn_interval = 3000  # 3 seconds 

        self.last_train_spawn_time = pygame.time.get_ticks()
        self.train_spawn_interval = 10000  # 10 seconds


    def draw_lanes(self):
        # Load and scale the asphalt sprite
        original_asphalt = [pygame.image.load(path)
                            for path in ASPHALT_SPRITES]
        scaled_asphalt = [pygame.transform.scale(img, (100, img.get_height())) for img in original_asphalt]
        
        # Randomize the asphalt sprite for each lane
        self.asphalt = [random.choice(scaled_asphalt) for _ in range(self.num_lanes)]

        for i in range(int(self.screen_height / self.asphalt[0].get_height()) + 1):
            for j, lane in enumerate(self.lane_positions):
                logger.debug('Drawing lane {} at position {}'.format(j, lane))
                self.screen.blit(self.asphalt[j], (lane, i * self.asphalt[j].get_height()))
                
    def spawn_coins(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_coin_spawn_time > self.coin_spawn_interval:
            lane = random.choice(self.lane_positions)
            
            num_coins = random.randint(3, 10)
            for i in range(num_coins):
                coin = Coin(self, lane)
                coin.rect.y += i * coin.rect.height + i * COIN_GAP

                self.coins.add(coin)

            self.last_coin_spawn_time = current_time

    def spawn_trains(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_train_spawn_time > self.train_spawn_interval:
            occupied_lanes = [train.lane for train in self.trains]
            available_lanes = list(set(self.lane_positions) - set(occupied_lanes))
            
            idle_lane = random.choice(available_lanes)
            available_lanes.remove(idle_lane)
            moving_lane = random.choice(available_lanes)

            if available_lanes:
                train1 = Train(self, idle_lane, is_moving=False)
                train2 = Train(self, moving_lane, is_moving=True)
                self.trains.add(train1)
                self.trains.add(train2)

            self.last_train_spawn_time = current_time

    def display_game_over_screen(self):
        print("Game Over! Press ESC to exit.")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

    def get_entity_class(self, class_name):
        return self.entity_classes.get(class_name, BaseEntity)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.player.handle_event(event)

    def update_entities(self):
        self.player.update()
        self.coins.update()
        self.trains.update()

    def draw_entities(self):
        # Draw entities
        self.screen.fill((255, 255, 255))  # Clear the screen
        self.draw_lanes()  # Draw lanes
        self.player.draw(self.screen)

        for coin in self.coins.sprites():
            coin.draw(self.screen)

        for train in self.trains.sprites():
            train.draw(self.screen)

    def run(self):
        # Game loop
        while not self.game_over:
            self.handle_events()
            self.update_entities()
            self.draw_entities()

            self.spawn_coins()
            self.spawn_trains()

            # Update scroll speed depending on distance travelled
            self.scroll_speed = SCROLL_SPEED + self.player.distance // 10000

            pygame.display.flip()

            self.clock.tick(DESIRED_FPS)

            if self.game_over:
                self.display_game_over_screen()


        
