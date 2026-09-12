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

    def __draw_cell(self, i, j):

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
        time.sleep(0.05)