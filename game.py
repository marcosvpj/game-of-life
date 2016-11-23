import pygame
from pygame.constants import QUIT, KEYDOWN, K_ESCAPE

from game_of_life import build_board, generate_next_generation
import structures


def should_keep_running():
    for event in pygame.event.get():
        if is_exit_event(event):
            return False
    return True


def is_exit_event(e):
    def esc_key_pressed(e):
        return e.type == KEYDOWN and e.key == K_ESCAPE

    def exit_button_pressed(e):
        return e.type == QUIT

    return esc_key_pressed(e) or exit_button_pressed(e)


def draw_rectangle(c):
    s = pygame.Surface((CELL_SIZE, CELL_SIZE))
    s.fill(c)
    return s


def draw_dead():
    return draw_rectangle((255, 255, 255))


def draw_alive():
    return draw_rectangle((125, 125, 125))


def cell_size_in_pixels():
    return CELL_SIZE + SPACE_BETWEEN_CELLS


def size_for_n_cells(n):
    return n * cell_size_in_pixels() + SPACE_BETWEEN_CELLS


def draw_cell(cell):
    surf = draw_dead()
    if cell:
        surf = draw_alive()

    return surf


def draw_board(b):
    board_surface = pygame.Surface((BOARD_WIDTH_IN_PIXELS, BOARD_HEIGHT_IN_PIXELS))
    for y in range(len(b)):
        for x in range(len(b[y])):
            surface = draw_cell(b[y][x])
            board_surface.blit(surface, (size_for_n_cells(x), size_for_n_cells(y)))

    return board_surface


def setup_board():
    b = build_board(height=BOARD_HEIGHT, width=BOARD_WIDTH)
    structures.place_acorn(b, (20, 20))

    return b


CELL_SIZE = 7
SPACE_BETWEEN_CELLS = 1
BOARD_WIDTH = 60
BOARD_HEIGHT = 50
BOARD_WIDTH_IN_PIXELS = size_for_n_cells(BOARD_WIDTH)
BOARD_HEIGHT_IN_PIXELS = size_for_n_cells(BOARD_HEIGHT)

board = setup_board()

screen = pygame.display.set_mode((BOARD_WIDTH_IN_PIXELS, BOARD_HEIGHT_IN_PIXELS))
pygame.init()

while should_keep_running():
    screen.blit(draw_board(board), (0, 0))
    board = generate_next_generation(board)
    pygame.display.flip()
