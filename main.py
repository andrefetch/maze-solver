from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas()
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
    def __init__(self, point_one, point_two) -> None:
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

def main() -> None:
    win = Window(800, 600)
    p1 = Point(100, 20)
    p2 = Point(30, 40)
    line = Line(p1, p2)
    win.draw_line(line, "red")
    win.wait_for_close()

if __name__ == "__main__":
    main()