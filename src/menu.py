import pygame
import sys
import csv
from src.utilities.buttons import Button
from src.utilities.constants import MENU_FONT_COLOR, MENU_FONT_SIZE, MENU_BG_COLOR, WIDTH, HEIGHT

class Menu:
    def __init__(self, game):
        self.game = game
        self.buttons = [
            Button(200, 200, "Retry", self.retry_game),
            Button(200, 340, "Leaderboards", self.show_leaderboards),
            Button(200, 410, "Quit", self.quit_game)
        ]
        self.input_box = pygame.Rect(200, 270, 140, 32)  # X, Y, Width, Height
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = ''
        self.font = pygame.font.Font(None, 32)
        self.active = False
        self.submit_button = Button(350, 270, "Submit", self.submit_name)
        
    def retry_game(self):
        self.game.reset()
        self.game.run()  # Call the game's run method to restart the game

    def show_leaderboards(self):
        pass  # Implement this to show leaderboards
        
        
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

            self.draw()  # Draw after handling events to reflect updates immediately b

    def name_input_box(self):
        # Clear the previous text by drawing a rectangle over it.
        pygame.draw.rect(self.game.screen, MENU_BG_COLOR, self.input_box)

        # Render the current text.
        txt_surface = self.font.render(self.text, True, self.color)
        # Resize the box if the text is too long.
        width = max(300, txt_surface.get_width()+10)
        self.input_box.w = width
        # Blit the text.
        self.game.screen.blit(txt_surface, (self.input_box.x+5, self.input_box.y+5))
        # Blit the input box rect.
        pygame.draw.rect(self.game.screen, self.color, self.input_box, 2)
        
        # Draw submit button
        self.submit_button.draw(self.game.screen)
        
    def draw(self):
        # Display "GAME OVER"
        font = pygame.font.Font(None, MENU_FONT_SIZE)
        game_over_label = font.render("GAME OVER", True, MENU_FONT_COLOR)
        game_over_rect = game_over_label.get_rect(center=(WIDTH/2, 100))
        self.game.screen.blit(game_over_label, game_over_rect)

        # Display score
        score_text = "Score: " + str(self.game.player.score)
        score_label = font.render(score_text, True, MENU_FONT_COLOR)
        score_rect = score_label.get_rect(center=(WIDTH/2, 150))
        self.game.screen.blit(score_label, score_rect)

        self.name_input_box()
        
        # Draw buttons
        for button in self.buttons:
            button.draw(self.game.screen)
            button.rect.centerx = WIDTH/2
            
    def run(self):
        while True:
            self.draw()
            self.handle_events()
            pygame.display.flip()

    def quit_game(self):
        pygame.quit()
        sys.exit()