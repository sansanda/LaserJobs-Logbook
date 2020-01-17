"""

Creating a main window class GUI manage the Laser Jobs

David SAnchez Sanchez


"""
from Gui.MainWindow import MainWindow
from Gui.NewJobWindow import NewJobWindow
from Gui.TextFilterOptionsWindow import TextFilterOptionsWindow
from Gui.DataSourceOptionsWindow import DataSourceOptionsWindow

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
        if isinstance(window,NewJobWindow) or isinstance(window, TextFilterOptionsWindow) or isinstance(window, DataSourceOptionsWindow):
            window.root.destroy()
            self.actualWindow = self.windowsStack.pop()
            self.actualWindow.enable(True)
            self.actualWindow.root.focus_force()

        elif isinstance(window,MainWindow):
            #destroy all windows
            window.root.destroy()

    def showNewJobWindow(self):
        print(self.actualWindow)
        self.actualWindow.enable(False)
        self.windowsStack.append(self.actualWindow)
        self.actualWindow = NewJobWindow(600,300,self,None)
        self.actualWindow.show()

    def showTextFilterOptionsWindow(self):
        self.actualWindow.enable(False)
        self.windowsStack.append(self.actualWindow)
        self.actualWindow = TextFilterOptionsWindow(300, 120, self, self.logicController.filter)
        self.actualWindow.show()

    def showDataSourceOptionsWindow(self):
        self.actualWindow.enable(False)
        self.windowsStack.append(self.actualWindow)
        self.actualWindow = DataSourceOptionsWindow(500, 100, self, self.logicController.laserJobsFilepath,
                                                    self.logicController.laserJobsFilename)
        self.actualWindow.show()


    def updateTextFilterList(self,sv):
        self.logicController.updateTextFilterList(sv)

    def updateTextFilterOptions(self,cs_option,and_option,wholeword_option):
        self.logicController.updateTextFilterOptions(cs_option,and_option,wholeword_option)

    def updateLaserJobsFileLocation(self, laserJobsFilepath, laserJobsFilename):
        self.logicController.updateLaserJobsFileLocation(laserJobsFilepath, laserJobsFilename)

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

    def editJob(self,jobId):
        print('Editing job ...')
        self.logicController.editJob(jobId)

    #filterOptions is a dict
    def saveFilterOptions(self, filterOptions):
        print("saving filter options")
        self.logicController.saveFilterOptions(filterOptions)

    def start(self):
        self.actualWindow.show()
