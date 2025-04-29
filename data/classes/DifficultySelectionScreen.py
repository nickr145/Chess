import pygame

class DifficultySelectionScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background_color = (255, 255, 255)
        self.title_font = pygame.font.Font(None, 80)
        self.button_font = pygame.font.Font(None, 50)

        # Buttons
        self.level1_button = pygame.Rect(300, 300, 200, 80)
        self.level2_button = pygame.Rect(300, 400, 200, 80)

    def draw(self):
        self.screen.fill(self.background_color)

        # Title
        title_surface = self.title_font.render("Choose Difficulty", True, (0, 0, 0))
        title_rect = title_surface.get_rect(center=(400, 150))
        self.screen.blit(title_surface, title_rect)

        # Level 1 Button
        pygame.draw.rect(self.screen, (0, 0, 0), self.level1_button, border_radius=10)
        level1_text = self.button_font.render("Level 1", True, (255, 255, 255))
        level1_rect = level1_text.get_rect(center=self.level1_button.center)
        self.screen.blit(level1_text, level1_rect)

        # Level 2 Button
        pygame.draw.rect(self.screen, (0, 0, 0), self.level2_button, border_radius=10)
        level2_text = self.button_font.render("Level 2", True, (255, 255, 255))
        level2_rect = level2_text.get_rect(center=self.level2_button.center)
        self.screen.blit(level2_text, level2_rect)

        pygame.display.update()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.level1_button.collidepoint(event.pos):
                return "level1"
            elif self.level2_button.collidepoint(event.pos):
                return "level2"

        return None
