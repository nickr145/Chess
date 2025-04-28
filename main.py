import pygame
import sys
import random

from data.classes.TitleScreen import TitleScreen
from data.classes.Board import Board

# Initialize pygame
pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess')

FPS = 60
CLOCK = pygame.time.Clock()

# Game variables
board = Board(WIDTH, HEIGHT)

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
            if result == "pvp":
                return "pvp"

        title_screen.draw()

if __name__ == '__main__':
    mode = title_loop()  # Go to title screen first
    if mode == "pvp":
        running = True
        while running:
            CLOCK.tick(FPS)
            mx, my = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        board.handle_click(mx, my)

            if board.is_in_checkmate('black'):
                print('White wins!')
                running = False
            elif board.is_in_checkmate('white'):
                print('Black wins!')
                running = False

            draw(screen)

    pygame.quit()
    sys.exit()
