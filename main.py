import pygame
import sys
import random

from data.classes.TitleScreen import TitleScreen
from data.classes.Board import Board
from data.classes.DifficultySelectionScreen import DifficultySelectionScreen
from data.classes.computers.Level1Computer import Level1Computer
from data.classes.computers.Level2Computer import Level2Computer

# Initialize pygame
pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

FPS = 60
CLOCK = pygame.time.Clock()

# Game variables
board = Board(WIDTH, HEIGHT)
current_turn = 'w'   # <<< ADD THIS
computer_player = None
pvc_mode = False

def draw(screen):
    board.draw(screen)
    pygame.display.update()

def title_loop():
    title_screen = TitleScreen(screen)

    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            result = title_screen.handle_event(event)
            if result in ("pvp", "pvc"):
                return result

        title_screen.draw()

def difficulty_loop():
    difficulty_screen = DifficultySelectionScreen(screen)
    while True:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            result = difficulty_screen.handle_event(event)
            if result in ("level1", "level2"):
                return result

        difficulty_screen.draw()
        
def draw_thinking_overlay(screen):
    font = pygame.font.Font(None, 50)
    text = font.render("Computer is thinking...", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width() // 2, 50))

    overlay = pygame.Surface((screen.get_width(), 100))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))
    screen.blit(text, text_rect)
    pygame.display.update()



if __name__ == '__main__':
    mode = title_loop()

    if mode == "pvp":
        pvc_mode = False
    elif mode == "pvc":
        difficulty = difficulty_loop()
        pvc_mode = True

        if difficulty == "level1":
            computer_player = Level1Computer('black')
        elif difficulty == "level2":
            computer_player = Level2Computer('black')

    running = True
    while running:
        CLOCK.tick(FPS)
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (not pvc_mode and True) or (pvc_mode and current_turn == 'w'):
                        moved = board.handle_click(mx, my)
                        if moved:
                            current_turn = 'w' if board.turn == 'white' else 'b'
                            if not pvc_mode:
                                current_turn = 'b' if current_turn == 'w' else 'w'
                            else:
                                current_turn = 'b'

        if pvc_mode and current_turn == 'b':
            draw_thinking_overlay(screen)
            pygame.time.delay(500)
            computer_player.make_move(board)
            board.turn = 'white'
            current_turn = 'w'

        if board.is_in_checkmate('black'):
            print('White wins!')
            running = False
        elif board.is_in_checkmate('white'):
            print('Black wins!')
            running = False

        draw(screen)

    pygame.quit()
    sys.exit()
