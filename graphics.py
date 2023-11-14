from __future__ import annotations
from tkinter import Tk, BOTH, Canvas

CELL_SIZE = 60


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self._p1 = p1
        self._p2 = p2

    def draw(self, canvas: Canvas, fill_color: str = "black"):
        canvas.create_line(
            self._p1.x, self._p1.y, self._p2.x, self._p2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)


class Window:
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Maze Solver")

        self._canvas = Canvas(self._root, bg="white", width=width, height=height)
        self._canvas.pack(fill=BOTH, expand=1)

        self._is_running = False

        self._root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self._root.update()
        self._root.update_idletasks()

    def wait_for_close(self):
        self._is_running = True
        while self._is_running:
            self.redraw()

    def close(self):
        self._is_running = False

    def draw_line(self, line: Line, fill_color: str = "black"):
        line.draw(self._canvas, fill_color)


class Cell:
    def __init__(
        self, window: Window | None = None, top=True, right=True, bottom=True, left=True
    ):
        self.has_top_wall = top
        self.has_right_wall = right
        self.has_bottom_wall = bottom
        self.has_left_wall = left
        self._origin_x = 0
        self._origin_y = 0
        self.visited = False
        self._win = window

    def draw(self, x, y):
        if self._win is None:
            return
        self._origin_x = x
        self._origin_y = y
        end_x = x + CELL_SIZE
        end_y = y + CELL_SIZE

        top_line = Line(Point(x, y), Point(end_x, y))
        top_line_color = "black" if self.has_top_wall else "white"
        self._win.draw_line(top_line, top_line_color)

        right_line = Line(Point(end_x, y), Point(end_x, end_y))
        right_line_color = "black" if self.has_right_wall else "white"
        self._win.draw_line(right_line, right_line_color)

        bottom_line = Line(Point(x, end_y), Point(end_x, end_y))
        bottom_line_color = "black" if self.has_bottom_wall else "white"
        self._win.draw_line(bottom_line, bottom_line_color)

        left_line = Line(Point(x, y), Point(x, end_y))
        left_line_color = "black" if self.has_left_wall else "white"
        self._win.draw_line(left_line, left_line_color)

    def draw_move(self, to_cell: Cell, undo=False):
        if self._win is None:
            return
        line_color = "gray" if undo else "red"
        x1 = self._origin_x + (CELL_SIZE / 2)
        y1 = self._origin_y + (CELL_SIZE / 2)
        x2 = to_cell._origin_x + (CELL_SIZE / 2)
        y2 = to_cell._origin_y + (CELL_SIZE / 2)
        line = Line(Point(x1, y1), Point(x2, y2))

        self._win.draw_line(line, line_color)
