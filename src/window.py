from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("...")
        self.canvas = Canvas(self.__root)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )

'''
    def draw(self, x1, y1, x2, y2):
        if self.has_left_wall:
            wall = Line((x1, y1), (x2-(x2-x1), y2-(y2-y1)))
            wall.draw(self._win.canvas, "black")
        if self.has_right_wall:
            wall = Line((x1-(x2-x1), y1-(y2-y1)), (x2, y2))
            wall.draw(self._win.canvas, "black")
        if self.has_top_wall:
            wall = Line((x1, y1), (x2, y2-(y2-y1)))
            wall.draw(self._win.canvas, "black")
        if self.has_bottom_wall:
            wall = Line((x1, y1-(y2-y1)), (x2, y2))
            wall.draw(self._win.canvas, "black")
'''