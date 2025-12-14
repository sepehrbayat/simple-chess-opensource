"""
Author: Sepehr Bayat | Open Source Chess MVP

Constants for colors, Unicode chess symbols, and board dimensions.
"""

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SQUARE = (240, 217, 181)  # Beige
DARK_SQUARE = (181, 136, 99)     # Brown
HIGHLIGHT = (255, 255, 0)        # Yellow for selected piece
VALID_MOVE_HIGHLIGHT = (144, 238, 144)  # Light green for valid moves
UI_BACKGROUND = (50, 50, 50)     # Dark gray for UI panel
UI_TEXT = (255, 255, 255)        # White text

# Unicode Chess Symbols
KING_WHITE = "♔"
QUEEN_WHITE = "♕"
ROOK_WHITE = "♖"
BISHOP_WHITE = "♗"
KNIGHT_WHITE = "♘"
PAWN_WHITE = "♙"

KING_BLACK = "♚"
QUEEN_BLACK = "♛"
ROOK_BLACK = "♜"
BISHOP_BLACK = "♝"
KNIGHT_BLACK = "♞"
PAWN_BLACK = "♟"

# Piece Symbols Dictionary
PIECE_SYMBOLS = {
    ('king', 'white'): KING_WHITE,
    ('queen', 'white'): QUEEN_WHITE,
    ('rook', 'white'): ROOK_WHITE,
    ('bishop', 'white'): BISHOP_WHITE,
    ('knight', 'white'): KNIGHT_WHITE,
    ('pawn', 'white'): PAWN_WHITE,
    ('king', 'black'): KING_BLACK,
    ('queen', 'black'): QUEEN_BLACK,
    ('rook', 'black'): ROOK_BLACK,
    ('bishop', 'black'): BISHOP_BLACK,
    ('knight', 'black'): KNIGHT_BLACK,
    ('pawn', 'black'): PAWN_BLACK,
}

# Board Dimensions
SQUARE_SIZE = 80
BOARD_SIZE = SQUARE_SIZE * 8
UI_PANEL_WIDTH = 300
WINDOW_WIDTH = BOARD_SIZE + UI_PANEL_WIDTH
WINDOW_HEIGHT = BOARD_SIZE

# Piece Values (for evaluation)
PIECE_VALUES = {
    'pawn': 1,
    'knight': 3,
    'bishop': 3,
    'rook': 5,
    'queen': 9,
    'king': 100  # High value to prevent trading
}

