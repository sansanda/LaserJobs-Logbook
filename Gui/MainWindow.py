"""

Creating a main window class GUI manage the Laser Jobs

David SAnchez Sanchez


"""
import tkinter

class MainWindow():

    def __init__(self, guiController):
        self.guiController = guiController
        self.root = tkinter.Tk()
        self.root.title('Laser-Jobs Manager. Main Window.')
        self.root.iconbitmap('../icons/laserJobsManager_Icon5.ico')
        self.root.mainloop()
