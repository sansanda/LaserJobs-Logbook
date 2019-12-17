"""

Creating a Logic Controller to control the logic part of the Laser Job Manager

David SAnchez Sanchez


"""

from Logic.LaserJobs_Book import LaserJobs_Book
from Data.Excel_Utilities.ExcelUtils import loadJobsFromExcel
from Data.Excel_Utilities.ExcelUtils import loadJobsFromExcelByOpenpyxl
from Data.Excel_Utilities.ExcelUtils import insertRowInExcel
from Data.Excel_Utilities.ExcelUtils import insertRowInExcelByOpenpyxl
from Data.Excel_Utilities.ExcelUtils import deleteRowInExcel
from Data.Excel_Utilities.ExcelUtils import deleteRowInExcelByOpenpyxl

from Logic.DesignPatterns.ObserverPattern import Publisher
from tkinter import messagebox

class LogicController(Publisher):

    def __init__(self, laserJobsPath, laserJobsFileName):
        Publisher.__init__(self)
        self.guiController = None
        self.laserJobsBook = LaserJobs_Book()
        self.laserJobsPath = laserJobsPath
        self.laserJobsFileName = laserJobsFileName

    def setGuiController(self,guicontroller):
        self.guiController = guicontroller
        self.guiController.setLogicController(self)

    def getGuiController(self):
        return self.guiController

    def loadJobsFromExcel(self):
        loadJobsFromExcelByOpenpyxl(self.laserJobsBook, self.laserJobsPath, self.laserJobsFileName)
        self.notify(self.laserJobsBook)

    def updateExcel(self, updatedJobData, deleteJob=False):
        if deleteJob==False:
            insertRowInExcelByOpenpyxl(updatedJobData, self.laserJobsPath, self.laserJobsFileName)
        elif deleteJob==True:
            deleteRowInExcelByOpenpyxl(updatedJobData, self.laserJobsPath, self.laserJobsFileName)

    def newJob(self,newJobData):
        try:
            jobId = self.laserJobsBook.getFirstFreeId()
            newJobData['jobId'] = jobId
            self.updateExcel(newJobData)
            self.laserJobsBook.newJob(newJobData)
            self.notify(self.laserJobsBook)
        except PermissionError as pe:
            messagebox.showerror("Excel opened!!!!!", "The excel file must be closed if you want to add new jobs!!!!!")

        except Exception as inst:
            raise(inst)


    def getJob(self, jobId):
        # TODO implement getJob
        return self.laserJobsBook.getJob(jobId)

    def updateJob(self,updatedJobData):
        # TODO implement updateJob
        self.laserJobsBook.updateJob(updatedJobData)


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

    def start(self):
        self.guiController.start()