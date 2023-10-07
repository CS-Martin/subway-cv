import pygame
import os

WIDTH = 1200 
HEIGHT = 800
DESIRED_FPS = 60
SCREENRECT = pygame.Rect(0, 0, WIDTH, HEIGHT)
NUM_LANES = 3
LANE_GAP = 10
LANE_WIDTH = 100
TOTAL_WIDTH = NUM_LANES * LANE_WIDTH + (NUM_LANES - 1) * LANE_GAP
START_X = (WIDTH - TOTAL_WIDTH) // 2
LANE_POSITIONS = [START_X + i * (LANE_WIDTH + LANE_GAP) for i in range(NUM_LANES)]
TRAIN_HEIGHTS = [200, 300, 400]
START_Y = -1 * max(TRAIN_HEIGHTS)
SCROLL_SPEED = 4
COIN_GAP = 20
NUM_COINS = 3

CWD = os.getcwd()

PLAYER_PATH = os.path.join(CWD, 'assets', 'Player')
PLAYERS = os.listdir(PLAYER_PATH)
PLAYER_SPRITES = [os.path.join(PLAYER_PATH, player) for player in PLAYERS]

COIN_PATH = os.path.join(CWD, 'assets', 'Coin')
COINS = os.listdir(COIN_PATH)
COIN_SPRITES = [os.path.join(COIN_PATH, coin) for coin in COINS]

TRAIN_PATH = os.path.join(CWD, 'assets', 'Firetruck')
TRAINS = os.listdir(TRAIN_PATH)
TRAIN_SPRITES = [os.path.join(TRAIN_PATH, train) for train in TRAINS]

ASPHALT_PATH = os.path.join(CWD, 'assets', 'Asphalt')
ASPHALTS = os.listdir(ASPHALT_PATH)
ASPHALT_SPRITES = [os.path.join(ASPHALT_PATH, asphalt) for asphalt in ASPHALTS]

