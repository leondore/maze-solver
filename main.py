from graphics import Window
from maze import Maze
import sys


def main():
    num_rows = 12
    num_cols = 14
    margin = 50
    screen_x = 940
    screen_y = 820

    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, win, 10)
    print("maze created")
    is_solveable = maze.solve()
    if not is_solveable:
        print("maze can not be solved!")
    else:
        print("maze solved!")

    win.wait_for_close()


main()
