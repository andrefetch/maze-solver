import time
from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width: int, height: int) -> None:

        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.__root.geometry(f"{width}x{height}")

    def draw_line(self, line, fill_color) -> None:

        line.draw(self.__canvas, fill_color=fill_color)

    def redraw(self) -> None:

        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:

        self.running = True
        while self.running:
            self.redraw()

    def close(self) -> None:

        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

class Point:

    def __init__(self, x: float, y: float) -> None:

        self.x = x;
        self.y = y;

class Line:

    def __init__(self, point_one: float | int, point_two: float | int) -> None:

        self.point_one = point_one
        self.point_two = point_two

    def draw(self, canvas, fill_color):

        canvas.create_line(
            self.point_one.x, 
            self.point_one.y, 
            self.point_two.x, 
            self.point_two.y, 
            fill=fill_color, 
            width=2
        )

class Cell():

    def __init__(self, win: Window) -> None:

        self.__win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1 = -1.0
        self.__x2 = -1.0
        self.__y1 = -1.0
        self.__y2 = -1.0

    def draw(
            self, 
            x1: float | int,
            y1: float | int,
            x2: float | int,
            y2: float | int,
        ):

        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2 
        self.__y2 = y2 

        if self.has_left_wall:
            line = Line(
                Point(self.__x1, self.__y1),
                Point(self.__x1, self.__y2)
            )

            self.__win.draw_line(line, "black")

        if self.has_top_wall:
            line = Line(
                Point(self.__x1, self.__y1),
                Point(self.__x2, self.__y1)
            )

            self.__win.draw_line(line, "black")

        if self.has_right_wall:
            line = Line(
                Point(self.__x2, self.__y1),
                Point(self.__x2, self.__y2)
            )

            self.__win.draw_line(line, "black")

        if self.has_bottom_wall:
            line = Line(
                Point(self.__x1, self.__y2),
                Point(self.__x2, self.__y2)
            )

            self.__win.draw_line(line, "black")

    def draw_move(self, to_cell: "Cell", undo: bool = False) -> None:

        from_center = Point(
            (self.__x1 + self.__x2) / 2,
            (self.__y1 + self.__y2) / 2,
        )

        to_center = Point(
            (to_cell.__x1 + to_cell.__x2) / 2,
            (to_cell.__y1 + to_cell.__y2) / 2,
        )

        line = Line(
            to_center,
            from_center
        )

        if not undo:
            self.__win.draw_line(line, "red")
        else:
            self.__win.draw_line(line, "grey")

class Maze:

    def __init__(
            
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: float,
        cell_size_y: float,
        win: Window,

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
        self.win.redraw()
        time.sleep(0.05)

def main() -> None:

    win = Window(1280, 720)

    maze = Maze(
        x1=20,
        y1=30,
        num_rows=12,
        num_cols=24,
        cell_size_x=50,
        cell_size_y=50,
        win=win,
    )

    win.wait_for_close()

if __name__ == "__main__":
    main()