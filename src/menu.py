import pygame
import sys
import csv
from src.leaderboards import Leaderboard
from src.utilities.buttons import Button
from src.utilities.constants import  WIDTH, HEIGHT, MENU_PANEL_PATH, RESTART_BUTTON_PATH, LEADERBOARDS_BUTTON_PATH, QUIT_BUTTON_PATH, SUBMIT_BUTTON_PATH, FONT

import logging
logger = logging.getLogger(__name__)
class Menu:
    def __init__(self, game):
        self.game = game

        # Preloading images for performance
        self.menu_panel = pygame.transform.scale(pygame.image.load(MENU_PANEL_PATH), (400, 450))
        self.restart_btn_img = pygame.transform.scale(pygame.image.load(RESTART_BUTTON_PATH), (200, 50))
        self.leaderboards_btn_img = pygame.transform.scale(pygame.image.load(LEADERBOARDS_BUTTON_PATH), (200, 50))
        self.quit_btn_img = pygame.transform.scale(pygame.image.load(QUIT_BUTTON_PATH), (200, 50))
        self.submit_btn_img = pygame.transform.scale(pygame.image.load(SUBMIT_BUTTON_PATH), (300, 60))

        # Initializing buttons
        button_x = (WIDTH / 2) - 100
        self.buttons = [
            Button(button_x, 530, "", self.retry_game, image=self.restart_btn_img),
            Button(button_x, 600, "", self.show_leaderboards, image=self.leaderboards_btn_img),
            Button(button_x, 670, "", self.quit_game, image=self.quit_btn_img)
        ]

        # Input box settings
        self.input_box = pygame.Rect((WIDTH / 2) - 150, 285, 100, 50)
        self.color_inactive = pygame.Color(113, 33, 2)
        self.color_active = pygame.Color(0, 255, 0)
        self.color = self.color_inactive
        self.text = ''
        self.placeholder = 'Enter your name'  # Placeholder text
        self.font = pygame.font.Font(None, 45)
        self.active = False
        self.submit_button = Button(button_x - 50, 340, "", self.submit_name, image=self.submit_btn_img)

    def run(self):
        self.running = True
        while self.running:
            self.draw()
            self.handle_events()
            logger.debug("Menu running")
            pygame.display.flip()
            
    def retry_game(self):
        self.game.reset()
        self.game.run()  # Call the game's run method to restart the game

    def show_leaderboards(self):
        leaderboard = Leaderboard(self.game)
        leaderboard.run()

        self.draw()
        pygame.display.flip()
    
    def save_score_to_csv(self, name, score):
        with open('leaderboards.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, score])
            
    def submit_name(self):
        print(f"Name: {self.text}, Score: {self.game.player.score}")
        self.save_score_to_csv(self.text, self.game.player.score)
        self.text = ''
        
    def save_score_to_csv(self, name, score):
        filename = 'leaderboards.csv'
        
        try:
            with open(filename, 'r'):
                pass
        except FileNotFoundError:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Score'])
                
        # Append the new score
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, score])

    def handle_events(self):
        for event in pygame.event.get():
            # Handle name input event
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.input_box.collidepoint(event.pos):
                    self.active = not self.active
                else:
                    self.active = False
                self.color = self.color_active if self.active else self.color_inactive
            if event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key == pygame.K_RETURN:
                        print(self.text)
                        self.text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        self.text += event.unicode
                        
            self.submit_button.handle_event(event)
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for button in self.buttons:
                button.handle_event(event)

            if event.type == pygame.MOUSEMOTION:
                for button in self.buttons:
                    button.is_hovered = button.rect.collidepoint(event.pos)

            self.draw()  # Draw after handling events to reflect asdupdates immediatel

    def name_input_box(self):
        # Clear the previous text by drawing a rectangle over it.
        pygame.draw.rect(self.game.screen, (0, 0, 0, 10), self.input_box)

        # If the text is empty and the input box is not active, show the placeholder.
        if not self.text and not self.active:
            txt_surface = self.font.render(self.placeholder, True, (128, 128, 128))  # Use a lighter color for placeholder
        else:
            txt_surface = self.font.render(self.text, True, self.color)
        
        width = max(300, txt_surface.get_width() + 50)
        self.input_box.w = width
        self.game.screen.blit(txt_surface, (self.input_box.x + 5, self.input_box.y + 13))
        pygame.draw.rect(self.game.screen, self.color, self.input_box, 2)

        # Draw submit button
        self.submit_button.draw(self.game.screen)
        
    def draw(self):
        self.game.screen.fill((0, 0, 0, 120))

        # Display menu panel and other UI elements
        self.display_ui_elements()

        # Name input box and submit button
        self.name_input_box()

        # Draw buttons
        for button in self.buttons:
            button.draw(self.game.screen)

    def display_ui_elements(self):
        # Menu panel
        self.game.screen.blit(self.menu_panel, (WIDTH / 2 - self.menu_panel.get_width() / 2, 50))

        # Game Over text
        score_font = pygame.font.Font(FONT, 40)
        game_over_label = score_font.render("GAME OVER", True, (255, 255, 255))
        game_over_rect = game_over_label.get_rect(center=(WIDTH / 2, 180))
        self.game.screen.blit(game_over_label, game_over_rect)

        # Score display
        score_text_font = pygame.font.Font(FONT, 28)
        score_text = "Score: " + str(self.game.player.score)
        score_label = score_text_font.render(score_text, True, (255, 255, 255))
        score_rect = score_label.get_rect(center=(WIDTH / 2, 240))
        self.game.screen.blit(score_label, score_rect)

    def quit_game(self):
        pygame.quit()
        sys.exit()