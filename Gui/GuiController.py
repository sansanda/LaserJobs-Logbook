"""

Creating a main window class GUI manage the Laser Jobs

David SAnchez Sanchez


"""
from Gui.MainWindow import MainWindow
from Gui.NewJobWindow import NewJobWindow
from Gui.TextFilterOptionsWindow import TextFilterOptionsWindow
from Gui.DataSourceOptionsWindow import DataSourceOptionsWindow
from tkinter import Toplevel, Message

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
        if isinstance(window,NewJobWindow) or isinstance(window, TextFilterOptionsWindow):
            window.root.destroy()
            self.actualWindow = self.windowsStack.pop()
            self.actualWindow.enable(True)
            self.actualWindow.root.focus_force()

        elif isinstance(window,MainWindow):
            #destroy all windows
            window.root.destroy()

    def showNewJobWindow(self):
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
        self.actualWindow = DataSourceOptionsWindow(500, 150, self, self.logicController.laserJobsPath,
                                                    self.logicController.laserJobsFileName)
        self.actualWindow.show()


    def updateTextFilterList(self,sv):
        self.logicController.updateTextFilterList(sv)

    def updateTextFilterOptions(self,cs_option,and_option,wholeword_option):
        self.logicController.updateTextFilterOptions(cs_option,and_option,wholeword_option)

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

    @classmethod
    def showLoadingJobsWindow(cls, destroyTime):

        infoWindow = Toplevel()
        infoWindow.title('Loading laser jobs. \n Be patient.')
        infoWindow.geometry("%dx%d+%d+%d" % (300, 100, 100, 100))
        Message(infoWindow, text='Loading laser jobs. \n\n Be patient.', padx=20, pady=20, width=200).pack()
        infoWindow.after(destroyTime, infoWindow.destroy)
