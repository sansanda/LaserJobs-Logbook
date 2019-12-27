"""

Creating a Logic Controller to control the logic part of the Laser Job Manager

David Sanchez Sanchez


"""

from Logic.LaserJobs_Book import LaserJobs_Book
from Data.Excel_Utilities.ExcelUtils_OpenpyxlBased import loadJobsFromExcel
from Data.Excel_Utilities.ExcelUtils_OpenpyxlBased import insertRowInExcel
from Data.Excel_Utilities.ExcelUtils_OpenpyxlBased import deleteRowInExcel

from Logic.DesignPatterns.ObserverPattern import Publisher
from tkinter import messagebox
from Logic.Filter.TextFilter import TextFilter

class LogicController(Publisher):

    #TODO: Refocus at main window after close a secondary window
    def __init__(self, laserJobsPath, laserJobsFileName):
        Publisher.__init__(self)
        self.guiController = None
        self.laserJobsBook = LaserJobs_Book()
        self.laserJobsPath = laserJobsPath
        self.laserJobsFileName = laserJobsFileName
        self.filterOptions = {'Casesensitive':True, 'And':True}

    def setGuiController(self,guicontroller):
        self.guiController = guicontroller
        self.guiController.setLogicController(self)
        #add the main window as observer
        self.addObserver(self.guiController.actualWindow)

    def getGuiController(self):
        return self.guiController

    def loadJobsFromExcel(self):
        loadJobsFromExcel(self.laserJobsBook, self.laserJobsPath, self.laserJobsFileName)
        self.notify(self.laserJobsBook)

    def updateExcel(self, updatedJobData, deleteJob=False):
        if deleteJob==False:
            insertRowInExcel(updatedJobData, self.laserJobsPath, self.laserJobsFileName)
        elif deleteJob==True:
            deleteRowInExcel(updatedJobData, self.laserJobsPath, self.laserJobsFileName)

    def newJob(self,laserJob):
        try:
            jobId = self.laserJobsBook.getFirstFreeId()
            laserJob['jobId'] = jobId
            self.updateExcel(laserJob)
            self.laserJobsBook.newJob(laserJob)
            self.laserJobsBook.sort(key=lambda k: k['jobId'])
            self.notify(self.laserJobsBook)
        except PermissionError as pe:
            messagebox.showerror("Excel opened!!!!!", "The excel file must be closed if you want to add new jobs!!!!!")

        except Exception as inst:
            raise(inst)

    def editJob(self,jobId):
        print('Editing job...')
        pass

    def deleteJob(self,jobId):

        try:
            #TODO implement deleteJob
            jobData = self.laserJobsBook.getJob(jobId) #jobData is a dict
            self.updateExcel(jobData,deleteJob=True)
            self.laserJobsBook.deleteJob(jobId)
            self.notify(self.laserJobsBook)

        except PermissionError as pe:
            messagebox.showerror("Excel opened!!!!!", "The excel file must be closed if you want to add new jobs!!!!!")

        except Exception as inst:
            raise (inst)

    def getJob(self, jobId):
        # TODO implement getJob
        return self.laserJobsBook.getJob(jobId)

    def updateJob(self,updatedJobData):
        # TODO implement updateJob
        self.laserJobsBook.updateJob(updatedJobData)


    def saveFilterOptions(self,filterOptions):
        print('saving filter options')
        textFilter = TextFilter(list(),filterOptions['Casesensitive'],filterOptions['And'])
        self.notify(textFilter)
        print(filterOptions)

    def start(self):
        self.guiController.start()