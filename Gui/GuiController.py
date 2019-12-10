"""

Creating a main window class GUI manage the Laser Jobs

David SAnchez Sanchez


"""
from Gui.MainWindow import MainWindow
from Gui.NewJobWindow import NewJobWindow

class GuiController():

    def __init__(self):
        self.logicController = None
        self.actualWindow = None
        self.windowsStack = []

    def setLogicController(self, logicController):
        self.logicController = logicController

    def closeWindow(self,window):
        if isinstance(window,NewJobWindow):
            window.root.destroy()
            self.actualWindow = MainWindow(self)
        elif isinstance(window,MainWindow):
            window.root.destroy()

    def showNewJobWindow(self):
        self.actualWindow = NewJobWindow(self)
        self.windowsStack.append(self.actualWindow)
        self.actualWindow.show()

    def deleteJob(self):
        print('Delete register order')

    def configureMainWindow(self, _jobsTableHeaders):
        self.jobsTableHeaders = _jobsTableHeaders

    def cancelAddJob(self):
        print('Cancelling add register')

    def addJob(self):
        print('Adding new register')

    def start(self):
        self.actualWindow = MainWindow(self)
        self.windowsStack.append(self.actualWindow)
        self.actualWindow.show()

