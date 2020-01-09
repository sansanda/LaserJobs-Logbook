from tkinter import *
from tkinter import ttk

def main():
    gMaster = Tk()
    w = ttk.Treeview(gMaster, show="headings", columns=('Column1', 'Column2'))
    w.heading('#1', text='Column1', anchor=W)
    w.heading('#2', text='Column2', anchor=W)

    w.column('#1', minwidth = 70, width = 70, stretch = False)
    w.column('#2', minwidth = 70, width = 70, stretch = True)  # Try to change the value of stretch here.

    # The following 2 lines will make the Treeview `w` fill the window horizontally.
    w.grid(row = 0, column = 0, sticky='we')
    gMaster.grid_columnconfigure(0, weight=1)

    mainloop()

if __name__ == "__main__":
    # Try to change the width of the application window use your mouse and you will see
    # the width of column #2 will:
    # 1. keep unchanged when strech=False
    # 2. change when strech=True
    main()