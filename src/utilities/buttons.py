import pygame
from src.utilities.constants import BUTTON_COLOR, BUTTON_FONT_SIZE, BUTTON_HOVER_COLOR

class Button:
    def __init__(self, x, y, text, action=None, image=None):
        self.x = x
        self.y = y
        self.text = text
        self.action = action
        self.image = image
        self.is_hovered = False
        if self.image:
            self.rect = self.image.get_rect(topleft=(x, y))
        else:
            self.rect = self._compute_rect_based_on_text()

    def _compute_rect_based_on_text(self):
        font = pygame.font.Font(None, BUTTON_FONT_SIZE)
        label = font.render(self.text, True, (0, 0, 0,))
        return pygame.Rect(self.x, self.y, label.get_width() + 20, label.get_height() + 10)

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            color = BUTTON_HOVER_COLOR if self.is_hovered else BUTTON_COLOR
            pygame.draw.rect(screen, color, self.rect)

        font = pygame.font.Font(None, BUTTON_FONT_SIZE)
        label = font.render(self.text, True, (0, 0, 0))
        screen.blit(label, (self.x + 10, self.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()