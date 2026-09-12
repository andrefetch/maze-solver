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