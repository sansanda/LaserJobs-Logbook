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
import json
from threading import Timer

class LogicController(Publisher):


    def __init__(self, laserJobsPath, laserJobsFileName, filterOptionsPath, filterOptionsFileName):
        Publisher.__init__(self)
        self.guiController = None
        self.laserJobsBook = LaserJobs_Book()
        self.laserJobsPath = laserJobsPath
        self.laserJobsFileName = laserJobsFileName
        self.filterOptionsPath = filterOptionsPath
        self.filterOptionsFileName = filterOptionsFileName
        self.createTextFilter()

    def setGuiController(self,guicontroller):
        self.guiController = guicontroller
        self.guiController.setLogicController(self)
        #add the main window as observer
        self.addObserver(self.guiController.actualWindow)

    def getGuiController(self):
        return self.guiController

    def createTextFilter(self):
        with open(self.filterOptionsPath + self.filterOptionsFileName) as f:
            data = json.load(f)
        self.filter =  TextFilter([''],
                                  data['textFilterOptions']['caseSensitive'],
                                  data['textFilterOptions']['and'],
                                  data['textFilterOptions']['wholeWord']
                                  )

    def loadJobsFromExcel(self):
        print('hola')
        loadJobsFromExcel(self.laserJobsBook, self.laserJobsPath, self.laserJobsFileName)
        filteredJobs = (self.laserJobsBook.filterJobs(self.filter))
        filteredJobs_Count = LaserJobs_Book.countJobs(filteredJobs)
        self.notify((filteredJobs, filteredJobs_Count[0], filteredJobs_Count[1], filteredJobs_Count[2]))

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
            filteredJobs = (self.laserJobsBook.filterJobs(self.filter))
            filteredJobs_Count = LaserJobs_Book.countJobs(filteredJobs)
            self.notify((filteredJobs, filteredJobs_Count[0], filteredJobs_Count[1], filteredJobs_Count[2]))

        except PermissionError as pe:
            messagebox.showerror("Excel opened!!!!!", "The excel file must be closed if you want to add new jobs!!!!!")

        except Exception as inst:
            raise(inst)

    def editJob(self,jobId):
        print('Editing job...')
        pass

    def deleteJob(self,jobId):

        try:
            jobData = self.laserJobsBook.getJob(jobId) #jobData is a dict
            self.updateExcel(jobData,deleteJob=True)
            self.laserJobsBook.deleteJob(jobId)
            filteredJobs = (self.laserJobsBook.filterJobs(self.filter))
            filteredJobs_Count = LaserJobs_Book.countJobs(filteredJobs)
            self.notify((filteredJobs, filteredJobs_Count[0], filteredJobs_Count[1], filteredJobs_Count[2]))

        except PermissionError as pe:
            messagebox.showerror("Excel opened!!!!!", "The excel file must be closed if you want to add new jobs!!!!!")

        except Exception as inst:
            raise (inst)

    def getJob(self, jobId):
        return self.laserJobsBook.getJob(jobId)

    def updateJob(self,updatedJobData):
        self.laserJobsBook.updateJob(updatedJobData)
        filteredJobs = (self.laserJobsBook.filterJobs(self.filter))
        filteredJobs_Count = LaserJobs_Book.countJobs(filteredJobs)
        self.notify((filteredJobs, filteredJobs_Count[0], filteredJobs_Count[1], filteredJobs_Count[2]))


    def updateTextFilterList(self,sv):
        self.filter.textList = str.split(sv,';')
        filteredJobs = (self.laserJobsBook.filterJobs(self.filter))
        filteredJobs_Count = LaserJobs_Book.countJobs(filteredJobs)
        self.notify((filteredJobs, filteredJobs_Count[0], filteredJobs_Count[1], filteredJobs_Count[2]))

    def updateTextFilterOptions(self, cs_option, and_option, wholeword_option):
        self.filter.caseSensitiveOption = cs_option
        self.filter.andOption = and_option
        self.filter.wholeWordOption = wholeword_option
        filteredJobs = (self.laserJobsBook.filterJobs(self.filter))
        filteredJobs_Count = LaserJobs_Book.countJobs(filteredJobs)
        self.notify((filteredJobs, filteredJobs_Count[0], filteredJobs_Count[1], filteredJobs_Count[2]))

        #save changes to file
        data = dict()
        data['textFilterOptions'] = self.filter.getTextFilterOptions()
        with open(self.filterOptionsPath + self.filterOptionsFileName, 'w') as f:
            json.dump(data, f)


    def start(self):

        # first time we load the laser jobs
        # we give time to guicontroller for creating the main window before load the laser jobs
        t = Timer(2.0, self.loadJobsFromExcel)
        t.start()

        self.guiController.start()
