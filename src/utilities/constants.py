import pygame
import os

WIDTH = 1200 
HEIGHT = 800
DESIRED_FPS = 60
SCREENRECT = pygame.Rect(0, 0, WIDTH, HEIGHT)
NUM_LANES = 3
LANE_GAP = 1
LANE_WIDTH = 100
TOTAL_WIDTH = NUM_LANES * LANE_WIDTH + (NUM_LANES - 1) * LANE_GAP
START_X = (WIDTH - TOTAL_WIDTH) // 2
LANE_POSITIONS = [START_X + i * (LANE_WIDTH + LANE_GAP) for i in range(NUM_LANES)]
TRAIN_HEIGHTS = [200, 300, 400]
START_Y = -1 * max(TRAIN_HEIGHTS)
SCROLL_SPEED = 4
COIN_GAP = 20
NUM_COINS = 3
GAME_SFX = os.path.join(os.getcwd(), 'assets', 'game-sfx.wav')

CWD = os.getcwd()

PLAYER_PATH = os.path.join(CWD, 'assets', 'player')
PLAYERS = os.listdir(PLAYER_PATH)
PLAYER_SPRITES = [os.path.join(PLAYER_PATH, player) for player in PLAYERS if os.path.isfile(os.path.join(PLAYER_PATH, player))]
PLAYER_CRASH_SFX = os.path.join(CWD, 'assets', 'player', 'player-sfx', 'player-crashed-sfx.wav')
PLAYER_DEATH_SFX = os.path.join(CWD, 'assets', 'player', 'player-sfx', 'player-death-sfx.wav')

COIN_PATH = os.path.join(CWD, 'assets', 'coin')
COINS = os.listdir(COIN_PATH)
COIN_SPRITES = [os.path.join(COIN_PATH, coin) for coin in COINS if os.path.isfile(os.path.join(COIN_PATH, coin))] # filtering out any nonfile items (e.g., coin subdirectories).
COIN_COLLISION_SFX = os.path.join(CWD, 'assets', 'coin', 'coin-sfx', 'coin-collision-sound.wav')

TRAIN_PATH = os.path.join(CWD, 'assets', 'firetruck')
TRAINS = os.listdir(TRAIN_PATH)
TRAIN_SPRITES = [os.path.join(TRAIN_PATH, train) for train in TRAINS]

ASPHALT_PATH = os.path.join(CWD, 'assets', 'asphalt')
ASPHALTS = os.listdir(ASPHALT_PATH)
ASPHALT_SPRITES = [os.path.join(ASPHALT_PATH, asphalt) for asphalt in ASPHALTS]
ASPHALT_SCALE = 100

LEFT_LANE_EDGE_PATH = os.path.join(CWD, 'assets', 'lane_edge', 'left-lane-edge.png')
LANE_EDGE_SCALE = 100

SIDEWALK_PATH = os.path.join(CWD, 'assets', 'sidewalk')
SIDEWALK = os.listdir(SIDEWALK_PATH)
SIDEWALK_SPRITES = [os.path.join(SIDEWALK_PATH, sidewalk) for sidewalk in SIDEWALK]
SIDEWALK_SCALE = 70

SIDEWALK_TO_GRASS_SPRITE = os.path.join(CWD, 'assets', 'grass', 'sidewalk-to-grass.png')
SIDEWALK_TO_GRASS_SCALE = 70