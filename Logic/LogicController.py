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

class LogicController(Publisher):

    #TODO: Refocus at main window after close a secondary window
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
        self.filter =  TextFilter(list(),
                                  data['textFilterOptions']['caseSensitive'],
                                  data['textFilterOptions']['and'],
                                  data['textFilterOptions']['wholeWord']
                                  )

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
            self.notify(self.laserJobsBook.filterJobs(self.filter))
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
            self.notify(self.laserJobsBook.filterJobs(self.filter))

        except PermissionError as pe:
            messagebox.showerror("Excel opened!!!!!", "The excel file must be closed if you want to add new jobs!!!!!")

        except Exception as inst:
            raise (inst)

    def getJob(self, jobId):
        return self.laserJobsBook.getJob(jobId)

    def updateJob(self,updatedJobData):
        self.laserJobsBook.updateJob(updatedJobData)
        self.notify(self.laserJobsBook.filterJobs(self.filter))


    def updateTextFilterList(self,sv):
        self.filter.textList = str.split(sv,';')
        self.notify(self.laserJobsBook.filterJobs(self.filter))

    def updateTextFilterOptions(self, cs_option, and_option, wholeword_option):
        self.filter.caseSensitiveOption = cs_option
        self.filter.andOption = and_option
        self.filter.wholeWordOption = wholeword_option
        self.notify(self.laserJobsBook.filterJobs(self.filter))

        #save changes to file
        data = dict()
        data['textFilterOptions'] = dict()
        data['textFilterOptions']['caseSensitive'] = self.filter.caseSensitiveOption
        data['textFilterOptions']['and'] = self.filter.andOption
        data['textFilterOptions']['wholeWord'] = self.filter.wholeWordOption

        with open(self.filterOptionsPath + self.filterOptionsFileName, 'w') as f:
            json.dump(data, f)



    def start(self):
        self.guiController.start()