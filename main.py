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

def main() -> None:
    win = Window(800, 600)
    win.wait_for_close()

if __name__ == "__main__":
    main()