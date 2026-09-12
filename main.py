from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root)
        self.__canvas.pack()
        self.running = False

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

    def __init__(self, win: Window):
        self.__win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__x1 = -1.0
        self.__x2 = -1.0
        self.__y1 = -1.0
        self.__y2 = -1.0

    def draw(self, x, y):

        self.__x1 = x
        self.__y1 = y
        self.__x2 = x + 50
        self.__y2 = y + 50

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


def main() -> None:
    win = Window(800, 200)
    cell = Cell(win)
    cell.draw(20, 20)
    win.wait_for_close()

if __name__ == "__main__":
    main()