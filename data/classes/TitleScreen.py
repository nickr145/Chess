import pygame

class TitleScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background_color = (255, 255, 255)  # White background (you can change)
        self.title_font = pygame.font.Font(None, 100)
        self.button_font = pygame.font.Font(None, 50)

        # Button properties
        self.button_rect = pygame.Rect(300, 400, 200, 80)  # (x, y, width, height)

        # Load image (optional)
        self.image = pygame.image.load("data/imgs/chess_title.png")  # Example path
        self.image = pygame.transform.scale(self.image, (300, 300))  # Resize image

    def draw(self):
        self.screen.fill(self.background_color)

        # Draw title
        title_surface = self.title_font.render("Chess", True, (0, 0, 0))
        title_rect = title_surface.get_rect(center=(400, 100))
        self.screen.blit(title_surface, title_rect)

        # Draw image
        self.screen.blit(self.image, (250, 150))  # Adjust position as needed

        # Draw PvP button
        pygame.draw.rect(self.screen, (0, 0, 0), self.button_rect, border_radius=10)
        button_text = self.button_font.render("Play PvP", True, (255, 255, 255))
        text_rect = button_text.get_rect(center=self.button_rect.center)
        self.screen.blit(button_text, text_rect)

        pygame.display.update()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                return "pvp"

        return None
