"""

Creating a main window class GUI manage the Laser Jobs

David SAnchez Sanchez


"""
from Gui.MainWindow import MainWindow
from Gui.NewJobWindow import NewJobWindow

class GuiController():

    def __init__(self, logicController=None):
        self.logicController = logicController
        self.actualWindow = MainWindow(self)

    def addRegister(self):
        print('Add register order')

    def deleteRegister(self):
        print('Delete register order')