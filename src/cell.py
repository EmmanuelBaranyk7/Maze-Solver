from window import Line, Point

class Cell():
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        color = "white"

        def draw_wall(left_x, top_y, right_x, bottom_y):
            wall = Line(Point(left_x, top_y), Point(right_x, bottom_y))
            self._win.draw_line(wall, color)

        if self.has_left_wall:
            color = "black"
        draw_wall(self._x1, self._y1, self._x1, self._y2)
        color = "white"
        if self.has_right_wall:
            color = "black"
        draw_wall(self._x2, self._y1, self._x2, self._y2)
        color = "white"
        if self.has_top_wall:
            color = "black"
        draw_wall(self._x1, self._y1, self._x2, self._y1)
        color = "white"
        if self.has_bottom_wall:
            color = "black"
        draw_wall(self._x1, self._y2, self._x2, self._y2)
        color = "white"

    def draw_move(self, to_cell, undo=False):
        color = "gray"
        if not undo:
            color = "red"

        start_x = (self._x1 + self._x2) // 2
        start_y = (self._y1 + self._y2) // 2
        finish_x = (to_cell._x1 + to_cell._x2) // 2
        finish_y = (to_cell._y1 + to_cell._y2) // 2

        sect = Line(Point(start_x, start_y), Point(finish_x, finish_y))
        self._win.draw_line(sect, color)