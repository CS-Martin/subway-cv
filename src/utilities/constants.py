import pygame

WIDTH = 800
HEIGHT = 600
DESIRED_FPS = 60
SCREENRECT = pygame.Rect(0, 0, WIDTH, HEIGHT)
NUM_LANES = 4
LANE_GAP = 50
LANE_WIDTH = 25
TOTAL_WIDTH = NUM_LANES * LANE_WIDTH + (NUM_LANES - 1) * LANE_GAP
