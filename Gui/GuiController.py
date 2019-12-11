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
            self.actualWindow = self.windowsStack.pop()
            self.actualWindow.changeState('normal')
        elif isinstance(window,MainWindow):
            window.root.destroy()

    def showNewJobWindow(self):
        self.actualWindow.changeState('disable')
        self.windowsStack.append(self.actualWindow)
        self.actualWindow = NewJobWindow(self)
        self.actualWindow.show()

    def deleteJob(self):
        print('Delete register order')

    def configureMainWindow(self, _jobsTableHeaders):
        self.jobsTableHeaders = _jobsTableHeaders

    def addJob(self, newJobData):
        print('Adding new job')
        self.logicController.createNewJob(newJobData)


    def start(self):
        self.actualWindow = MainWindow(self)
        self.windowsStack.append(self.actualWindow)
        self.actualWindow.show()

