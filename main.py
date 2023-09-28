# import pygame
# import random

# pygame.init()

# # Screen dimensions
# screen_width = 800
# screen_height = 600

# # Create the game window
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Subway Surfers 2D")

# # Define the player class
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()

#         # Create the player sprite
#         self.image = pygame.Surface([50, 50])
#         self.image.fill((255, 0, 0))

#         # Set the player's initial position
#         self.rect = self.image.get_rect()
#         self.rect.center = (screen_width // 2, screen_height - 60)

#         # Set the player's speed and initial lane
#         self.speed = 5
#         self.lane = 2  # initialize player's lane to the middle lane

#     # Move the player to the left
#     def move_left(self):
#         if self.lane > 1:  # check if player is not in the leftmost lane
#             self.lane -= 1
#             self.rect.x -= 250

#     # Move the player to the right
#     def move_right(self):
#         if self.lane < 3:  # check if player is not in the rightmost lane
#             self.lane += 1
#             self.rect.x += 250

# # Define the obstacle class
# class Obstacle(pygame.sprite.Sprite):
#     def __init__(self, x):
#         super().__init__()

#         # Create the obstacle sprite
#         self.image = pygame.Surface([50, 50])
#         self.image.fill((0, 255, 0))

#         # Set the obstacle's initial position
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (x, 0)

#     # Update the obstacle's position
#     def update(self, player_lane):
#         self.rect.y += 4
#         self.rect.x = player_lane * 250

# # Define the train obstacle class
# class Train(pygame.sprite.Sprite):
#     def __init__(self, x):
#         super().__init__()

#         # Create the train sprite
#         self.image = pygame.Surface([200, 50])
#         self.image.fill((0, 0, 255))

#         # Set the train's initial position
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (x, 0)
#         self.initial_x = x  # store the train's initial x-coordinate

#     # Update the train's position
#     def update(self):
#         self.rect.y += 4
#         self.rect.x = self.initial_x  # set the x-coordinate to the initial value

# # Create the player and obstacle groups
# player = Player()
# obstacles = pygame.sprite.Group()
# all_sprites = pygame.sprite.Group()
# all_sprites.add(player)

# # Set up the game clock and loop
# clock = pygame.time.Clock()
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 player.move_left()
#             elif event.key == pygame.K_RIGHT:
#                 player.move_right()

#     # Spawn obstacles
#     if pygame.time.get_ticks() % 1500 == 0:
#         x = random.randint(0, 2) * 250  # spawn obstacles only in 3 lanes
#         if random.randint(0, 1) == 0:  # randomly spawn either a regular obstacle or a train obstacle
#             obstacle = Obstacle(x)
#         else:
#             obstacle = Train(x)
#         obstacles.add(obstacle)
#         all_sprites.add(obstacle)

#     # Update the obstacles and draw all sprites
#     obstacles.update(player.lane)
#     screen.fill((255, 255, 255))
#     all_sprites.draw(screen)

#     # Update the display and tick the clock
#     pygame.display.flip()
#     clock.tick(60)

from src.game import Game

def start_game():
    game = Game.create()
    game.loop()

if __name__ == "__main__":
    start_game()