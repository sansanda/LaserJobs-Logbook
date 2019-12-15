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

    def setActualWindow(self, window):
        self.actualWindow = window
        self.windowsStack.append(self.actualWindow)

    def closeWindow(self,window):
        if isinstance(window,NewJobWindow):
            window.root.destroy()
            self.actualWindow = self.windowsStack.pop()
            self.actualWindow.enable(True)
        elif isinstance(window,MainWindow):
            #destroy all windows
            window.root.destroy()

    def showNewJobWindow(self):
        self.actualWindow.enable(False)
        self.windowsStack.append(self.actualWindow)
        self.actualWindow = NewJobWindow(600,300,self)
        self.actualWindow.show()

    def newJob(self,newJobData):
        print('Adding new job ...')
        self.logicController.newJob(newJobData)

    def getJob(self, jobId):
        print('Getting job ...')
        return self.logicController.getJob(jobId)

    def updateJob(self,updatedJobData):
        print('Updating job ...')
        self.logicController.updateJob(updatedJobData)

    def deleteJob(self,jobId):
        print('Deleting job ...')
        self.logicController.deleteJob(jobId)


    def start(self):
        self.actualWindow.show()

