"""

Creating a main window class GUI manage the Laser Jobs

David SAnchez Sanchez


"""
from Gui.MainWindow import MainWindow
from Gui.NewJobWindow import NewJobWindow

class GuiController():

    def __init__(self, logicController=None):
        self.logicController = logicController
        #self.windows = {'mainWindow':MainWindow, 'newJobWindow':NewJobWindow}

    def addRegister(self):
        print('Add register order')

    def deleteRegister(self):
        print('Delete register order')

    def configureMainWindow(self, _jobsTableHeaders):
        self.jobsTableHeaders = _jobsTableHeaders

    def start(self):
        self.actualWindow = MainWindow(self)
