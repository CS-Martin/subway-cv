import pygame
import sys
from src.utilities.buttons import Button
from src.utilities.constants import MENU_FONT_COLOR, MENU_FONT_SIZE

class Menu:
    def __init__(self, game):
        self.game = game
        self.buttons = [
            Button(200, 200, "Retry", self.retry_game),
            Button(200, 270, "Leaderboards", self.show_leaderboards),
            Button(200, 340, "Quit", self.quit_game)
        ]

    def retry_game(self):
        self.game.run()  # Call the game's run method to restart the game

    def show_leaderboards(self):
        pass  # Implement this to show leaderboards

    def quit_game(self):
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for button in self.buttons:
                button.handle_event(event)

            if event.type == pygame.MOUSEMOTION:
                for button in self.buttons:
                    button.is_hovered = button.rect.collidepoint(event.pos)

    def draw(self):
        self.game.screen.fill((26, 186, 86))  # Use the game's screen to draw

        # Display "GAME OVER"
        font = pygame.font.Font(None, MENU_FONT_SIZE)
        game_over_label = font.render("GAME OVER", True, MENU_FONT_COLOR)
        self.game.screen.blit(game_over_label, (200, 100))

        # Display score
        score_text = "Score: " + str(self.game.player.score)
        score_label = font.render(score_text, True, MENU_FONT_COLOR)
        self.game.screen.blit(score_label, (200, 150))

        # Draw buttons
        for button in self.buttons:
            button.draw(self.game.screen)

    def run(self):
        while True:
            self.handle_events()
            self.draw()
            pygame.display.flip()