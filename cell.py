from line import Line
from point import Point
from window import Window


class Cell:

    def __init__(self, win: Window = None) -> None:

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

        if self.__win is None:
            return

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

        if self.__win is None:
            return

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