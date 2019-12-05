import tkinter

class NewJobWindow():

    def __init__(self, guiController):
        self.guiController = guiController
        self.root = tkinter.Tk()
        self.root.title('Laser-Jobs Manager. New Job Window.')
        self.root.iconbitmap('../icons/laserJobsManager_Icon5.ico')
        self.root.mainloop()