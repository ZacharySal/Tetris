WIDTH = 1000
HEIGHT = 1000

DOWN = -1
LEFT = 0
RIGHT = 1
ROTATE = 3
AUTO = 4
DROP = 5

FPS = 60
MAX_LEVEL = 10

ROWS = 20
COLS = 15
SQUARE_WIDTH = 450 // COLS
SQUARE_HEIGHT = 800 // ROWS

BG_COLOR = (0, 0, 0)

# the anchor of each piece is the first index
SHAPES = [
    [(0, 6), (-1, 6), (1, 6), (2, 6)],
    [(-1, 5), (-1, 6), (0, 5), (0, 6)],
    [(0, 6), (-1, 5), (-1, 6), (1, 6)],
    [(0, 6), (-1, 7), (-1, 6), (1, 6)],
    [(-1, 6), (-1, 5), (-1, 7), (0, 6)],
    [(0, 6), (-1, 6), (0, 5), (1, 5)],
    [(0, 5), (-1, 5), (0, 6), (1, 6)],
]

COLORS = [
    (0, 255, 255),
    (255, 255, 0),
    (128, 0, 128),
    (0, 255, 0),
    (255, 0, 0),
    (0, 0, 255),
    (255, 127, 0)
]

NEW_COLORS = [
    "red",
    "lightblue",
    "orange",
    "pink",
    "yellow",
    "green"
]

LEVEL_SPEED = {
    1: 1000,
    2: 900,
    3: 800,
    4: 700,
    5: 600,
    6: 500,
    7: 400,
    8: 300,
    9: 200,
    10: 100,
}



