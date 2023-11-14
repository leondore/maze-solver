from graphics import Window
from maze import Maze


def main():
    num_rows = 12
    num_cols = 14
    margin = 50
    screen_x = 940
    screen_y = 820
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, win)

    win.wait_for_close()


main()
