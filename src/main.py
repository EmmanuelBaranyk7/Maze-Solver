from window import Window, Point, Line

def main():
    win = Window(800, 600)
    line1 = Line(Point(100, 100), Point(300, 100))
    line2 = Line(Point(200, 0), Point(200, 200))
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.wait_for_close()

main() 