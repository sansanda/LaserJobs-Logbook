# The reason for the behavior you are seeing is that tkinter widgets are designed to shrink or expand to exactly fit around their children when using grid or pack. 99.99% of the time this is the exact right behavior, because it results in GUIs that are responsive to changes in font size, screen resolution, and window size.
#
# If your goal is to divide the screen into two parts, where one part takes up 1/4 of the screen and one part takes up 3/4, the best solution is to use grid or place since those both make it easy to set relative sizes.
#
# I don't normally recommend place, so here's a solution using grid. Note the use of grid.rowconfigure and grid.columnconfigure

from tkinter import *

class Application(object):
    def __init__(self):
        self.window = Tk()
        self.window.geometry('{}x{}'.format(400, 400))

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=3)
        self.window.grid_columnconfigure(0, weight=1)

        frame = Frame(self.window, background="pink")
        frame.grid(row=1, column=0, sticky="nsew")

        for row in range(4):
            frame.grid_rowconfigure(row, weight=1)
        for column in range(4):
            frame.grid_columnconfigure(column, weight=1)

        # add buttons
        for i in range(4):
            for j in range(4):
                button = Button(frame, text=str(4*i + j + 1))
                button.grid(row=i, column=j, sticky=N+E+S+W)
        self.window.mainloop()


def main():
    app = Application()

main()
