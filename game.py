import pygame
from pygame.locals import *

from game_of_life import build_board, generate_next_generation
from structures import populate_board_with_example, place_acorn


def is_exit_event(e):
    if e.type == KEYDOWN and e.key == K_ESCAPE:
        return True

    if e.type == QUIT:
        return True

    return False


def draw_rectangle(color):
    surf = pygame.Surface((15, 15))
    surf.fill(color)
    # rect = surf.get_rect()
    return surf


def draw_dead():
    return draw_rectangle((255, 255, 255))


def draw_alive():
    return draw_rectangle((125, 125, 125))


pygame.init()

WIDTH = 75
width_in_pixels = WIDTH * (15 + 3) + 3
HEIGHT = 40
height_in_pixels = HEIGHT * (15 + 3) + 3

screen = pygame.display.set_mode((width_in_pixels, height_in_pixels))
running = True

board = build_board(height=HEIGHT, width=WIDTH)
# populate_board_with_example(board)
place_acorn(board, (35, 17))

while running:
    for event in pygame.event.get():
        if is_exit_event(event):
            running = False

    for y in range(len(board)):
        for x in range(len(board[y])):
            surf = draw_dead()
            if board[y][x]:
                surf = draw_alive()
            screen.blit(surf, (x * (15 + 3) + 3, y * (15 + 3) + 3))

    board = generate_next_generation(board)

    pygame.display.flip()
