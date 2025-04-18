from window import Window
from maze import Maze

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()
    
    '''
    line1 = Line(Point(100, 100), Point(300, 100))
    line2 = Line(Point(200, 0), Point(200, 200))
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    '''
    win.wait_for_close()

main() 