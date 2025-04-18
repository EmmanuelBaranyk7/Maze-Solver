import time
import random
from cell import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win    
        self._cells = []
        if seed != None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            cells = []
            for j in range(self._num_rows):
                cells.append(Cell(self._win))
            self._cells.append(cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        print(f"x1: {x1}, y1: {y1}, x2: {x2}, y2: {y2}")
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        # right
        if i < self._num_cols - 1 and self._cells[i][j].has_right_wall == False and self._cells[i+1][j].has_left_wall == False and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j], True)
        # left
        if i > 0 and self._cells[i][j].has_left_wall == False and self._cells[i-1][j].has_right_wall == False and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j], True)
        # up
        if j > 0 and self._cells[i][j].has_top_wall == False and self._cells[i][j-1].has_bottom_wall == False and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j-1], True)
        # down
        if j < self._num_rows - 1 and self._cells[i][j].has_bottom_wall == False and self._cells[i][j+1].has_top_wall == False and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], True)
        return False


    '''
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = self._get_neighbors(i, j)
            print(f"to visit: {to_visit}")

            # If no unvisited neighbors, backtrack
            if not to_visit:
                return

            # Choose random neighbor
            direction_index = random.randrange(len(to_visit))
            next_index = to_visit[direction_index]
            print("called random")

            # Break walls between current cell and chosen neighbor
            if next_index == i + 1:  # Down
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j-1].has_top_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i, j-1)
            elif next_index == i - 1:  # Up
                self._cells[i][j].has_top_wall = False
                self._cells[i][j+1].has_bottom_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i, j+1)
            elif next_index == j + 1:  # Right
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i+1, j)
            elif next_index == j - 1:  # Left
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i-1, j)

            print("calling _break_walls_r...")
            # Recursively break walls
            self._break_walls_r(next_index[0], next_index[1])

    def _get_neighbors(self, i, j):
            to_vist = []
            if i > 0 and not self._cells[i - 1][j].visited:
                to_vist.append([i - 1, j])
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_vist.append([i + 1, j])
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                to_vist.append([i, j - 1])
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_vist.append([i, j + 1])
            return to_vist
            
            neighbors = []
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                neighbors.append((i + 1, j))
            if j < self._num_rows and not self._cells[i][j + 1].visited:
                neighbors.append((i, j + 1))
            if i > 0 and not self._cells[i - 1][j].visited:
                neighbors.append((i - 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                neighbors.append((i, j - 1))
            return neighbors
            '''
    '''
        self._cells[i][j]._visited = True
        while True: # infinte loop?
            to_vist = []
            if isinstance(self._cells[i+1][j], Cell) and not self._cells[i+1][j]._visited:
                to_vist.append([i+1, j])
            if isinstance(self._cells[i][j+1], Cell) and not self._cells[i][j+1]._visited:
                to_vist.append([i, j+1])
            if isinstance(self._cells[i-1][j], Cell) and not self._cells[i-1][j]._visited:
                to_vist.append([i-1, j])
            if isinstance(self._cells[i][j-1], Cell) and not self._cells[i][j-1]._visited:
                to_vist.append([i, j-1])
            if len(to_vist) == 0:
                self._draw_cell(i, j)
                return
            n = random.randrange(1, 5)
            if n == 1 and [i+1, j] in to_vist:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i+1, j)
                self._break_walls_r(i+1, j)
            elif n == 2 and [i, j-1] in to_vist:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j-1].has_top_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i, j-1)
                self._break_walls_r(i, j-1)
            elif n == 3 and [i-1, j] in to_vist:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i-1, j)
                self._break_walls_r(i-1, j)
            elif n == 4 and [i, j+1] in to_vist:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j+1].has_bottom_wall = False
                self._draw_cell(i, j)
                self._draw_cell(i, j+1)
                self._break_walls_r(i, j+1)
            
        '''


