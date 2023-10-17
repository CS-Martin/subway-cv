import pygame
from src.utilities.constants import BUTTON_COLOR, BUTTON_FONT_SIZE, BUTTON_HOVER_COLOR, MENU_FONT_COLOR

class Button:
    def __init__(self, x, y, text, action=None):
        self.x = x
        self.y = y
        self.text = text
        self.action = action
        self.is_hovered = False

    def draw(self, screen):
        font = pygame.font.Font(None, BUTTON_FONT_SIZE)
        label = font.render(self.text, True, MENU_FONT_COLOR)

        color = BUTTON_HOVER_COLOR if self.is_hovered else BUTTON_COLOR
        pygame.draw.rect(screen, color, (self.x, self.y, label.get_width() + 20, label.get_height() + 10))

        screen.blit(label, (self.x + 10, self.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()

    @property
    def rect(self):
        font = pygame.font.Font(None, BUTTON_FONT_SIZE)
        label = font.render(self.text, True, MENU_FONT_COLOR)
        return pygame.Rect(self.x, self.y, label.get_width() + 20, label.get_height() + 10)