import random
import time

from cell import Cell
from window import Window


class Maze:

    def __init__(

        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: float,
        cell_size_y: float,
        win: Window = None,
        seed = None

   ) -> None:

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__cells = []

        self.__create_cells()
        self.__break_entrance_and_exit()

        if seed != None:
            random.seed(seed)

        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self):

        for i in range(self.num_cols):

            columns = []

            for j in range(self.num_rows):

                maze_cell = Cell(self.win)
                columns.append(maze_cell)

            self.__cells.append(columns)

        for i in range(self.num_cols):

            for j in range(self.num_rows):

                self.__draw_cell(i, j)

    def __draw_cell(self, i: int, j: int) -> None:

        x1 = self.x1 + (i * self.cell_size_x)
        x2 = x1 + self.cell_size_x

        y1 = self.y1 + (j * self.cell_size_y)
        y2 = y1 + self.cell_size_y

        self.__cells[i][j].draw(x1, y1, x2, y2)
        self.__animate()

    def __animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.025)

    def __break_entrance_and_exit(self):

        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        self.__cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)

    def __break_walls_r(self, i: int, j: int) -> None:

        self.__cells[i][j].visited = True

        while True:

            possible_directions = []

            if i > 0 and not self.__cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))

            if i < self.num_cols - 1 and not self.__cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))

            if j > 0 and not self.__cells[i][j - 1].visited:
                possible_directions.append((i, j - 1))

            if j < self.num_rows - 1 and not self.__cells[i][j + 1].visited:
                possible_directions.append((i, j + 1))

            if len(possible_directions) == 0:
                self.__draw_cell(i, j)
                return

            direction_index = random.randrange(len(possible_directions))
            next_i, next_j = possible_directions[direction_index]

            if next_i == i + 1:
                self.__cells[i][j].has_right_wall = False
                self.__cells[next_i][next_j].has_left_wall = False

            if next_i == i - 1:
                self.__cells[i][j].has_left_wall = False
                self.__cells[next_i][next_j].has_right_wall = False

            if next_j == j + 1:
                self.__cells[i][j].has_bottom_wall = False
                self.__cells[next_i][next_j].has_top_wall = False

            if next_j == j - 1:
                self.__cells[i][j].has_top_wall = False
                self.__cells[next_i][next_j].has_bottom_wall = False

            self.__break_walls_r(next_i, next_j)

    def __reset_cells_visited(self):

        for i in range(self.num_cols):

            for j in range(self.num_rows):

                self.__cells[i][j].visited = False