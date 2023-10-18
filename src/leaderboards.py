import pygame
import sys
import csv
from src.utilities.buttons import Button
from src.utilities.constants import WIDTH, HEIGHT

class Leaderboard:
    def __init__(self, game):
        self.game = game
        self.clear_screen()
        transparent_dark_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        transparent_dark_surface.fill((0, 0, 0, 128))  # 50% transparent dark color
        self.game.screen.blit(transparent_dark_surface, (0, 0))
        self.back_button = Button(50, 50, "Back", self.back_to_menu)
        self.scores = self.get_sorted_scores()
        self.font = pygame.font.Font(None, 32)

    def get_sorted_scores(self):
        scores = []
        with open('leaderboards.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Skip the header
            for row in reader:
                if len(row) >= 2:  # Ensure there are at least two elements in the row
                    try:
                        name = row[0].strip()  # strip() helps remove unwanted spaces
                        score = int(row[1].strip())
                        scores.append((name, score))
                    except ValueError:  # In case the score is not a number
                        pass
        return sorted(scores, key=lambda x: x[1], reverse=True)[:10]  # Top 10 scores


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.back_button.handle_event(event)

    def clear_screen(self):
        # Fill the screen with a background color to clear it
        # self.game.screen.fill((0, 0, 0))
        # If you want the transparent dark surface to appear on your leaderboard screen
        transparent_dark_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        transparent_dark_surface.fill((0, 0, 0))  # 50% transparent dark color
        self.game.screen.blit(transparent_dark_surface, (0, 0))
    
    def back_to_menu(self):
        # Exit the leaderboard loop
        self.running = False
        self.game.screen.fill((0, 0, 0))
        pygame.display.flip()

    def draw(self):
        self.clear_screen()
        # Starting position
        y_offset = 100
        
        # Draw headers
        header_font = pygame.font.Font(None, 36)  # Slightly bigger font for headers
        name_header = header_font.render("Name", True, (255, 255, 255))
        score_header = header_font.render("Score", True, (255, 255, 255))
        self.game.screen.blit(name_header, (WIDTH // 4, y_offset))
        self.game.screen.blit(score_header, (2.5 * WIDTH // 4, y_offset))
        
        # Increase the y_offset to start displaying scores under the headers
        y_offset += 40

        # Draw scores
        for name, score in self.scores:
            name_label = self.font.render(name, True, (255, 255, 255))
            score_label = self.font.render(str(score), True, (255, 255, 255))
            self.game.screen.blit(name_label, (WIDTH // 4, y_offset))
            self.game.screen.blit(score_label, (2.5 * WIDTH // 4, y_offset))
            y_offset += 40

        # Draw back button
        self.back_button.draw(self.game.screen)


    def run(self):
        self.running = True
        while self.running:
            
            self.handle_events()
            self.draw()
            pygame.display.flip()

# In the Menu class
def show_leaderboards(self):
    leaderboard = Leaderboard(self.game)
    leaderboard.run()