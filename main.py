from graphics import Window
from maze import Maze

def main() -> None:

    win = Window(1280, 720)

    maze = Maze(
        x1=20,
        y1=30,
        num_rows=20,
        num_cols=37,
        cell_size_x=50,
        cell_size_y=50,
        win=win,
    )

    maze.solve()

    win.wait_for_close()

if __name__ == "__main__":
    main()