"""

Creating a Logic Controller to control the logic part of the Laser Job Manager

David Sanchez Sanchez


"""
from tkinter import messagebox

from Logic.LaserJobs_Book import LaserJobs_Book
from Logic.DesignPatterns.ObserverPattern import Publisher
from Logic.Filter.TextFilter import TextFilter

from Gui.GuiController import GuiController

from threading import Timer

import json
import os

class LogicController(Publisher):


    def __init__(self, configFilePath, configFileName):
        Publisher.__init__(self)
        self.guiController = None
        self.laserJobsBook = LaserJobs_Book()
        self.configFilenamePath = configFilePath
        self.configFilename = configFileName

        self.laserJobsFilepath, self.laserJobsFilename = self.loadLaserJobsFileLocation(self.configFilenamePath+self.configFilename)
        self.laserJobsFilepath = os.path.abspath(self.laserJobsFilepath ) + '/'
        self.filter = self.loadFilter(self.configFilenamePath + self.configFilename)

    def setGuiController(self,guicontroller):
        self.guiController = guicontroller
        self.guiController.setLogicController(self)
        #add the main window as observer
        self.addObserver(self.guiController.actualWindow)

    def getGuiController(self):
        return self.guiController

    def loadFilter(self, configFilename):
        with open(configFilename) as f:
            data = json.load(f)
        return TextFilter(
            [''],
            data['textFilterOptions']['caseSensitive'],
            data['textFilterOptions']['and'],
            data['textFilterOptions']['wholeWord']
        )

    def loadLaserJobsFileLocation(self, configFilename):

        with open(configFilename) as f:
            data = json.load(f)
        return data['laserJobsFileLocation']['laserJobsFilePath'],data['laserJobsFileLocation']['laserJobsFileName']

    def loadJobsFromSource(self, laserJobsFilepath, laserJobsFilename, filter):
        jobsData = self.laserJobsBook.loadJobsFromSource(laserJobsFilepath, laserJobsFilename, filter)
        jobs, nVectorJobs, nRasterJobs, nCombinedJobs = jobsData[0:4]
        self.notify((jobs, nVectorJobs, nRasterJobs, nCombinedJobs, self.laserJobsFilepath+self.laserJobsFilename))

    def newJob(self,laserJob):
        try:
            jobId = self.laserJobsBook.getFirstFreeId()
            laserJob['jobId'] = jobId
            self.laserJobsBook.updateJobsSource(self.laserJobsFilepath,self.laserJobsFilename,laserJob)
            self.laserJobsBook.newJob(laserJob)
            self.laserJobsBook.sort(key=lambda k: k['jobId'])
            filteredJobs = (self.laserJobsBook.filterJobs(self.filter))
            filteredJobs_Count = LaserJobs_Book.countJobs(filteredJobs)
            self.notify((filteredJobs, filteredJobs_Count[0], filteredJobs_Count[1], filteredJobs_Count[2], self.laserJobsFilepath+self.laserJobsFilename))

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
            self.laserJobsBook.updateJobsSource(self.laserJobsFilepath,self.laserJobsFilename,jobData,deleteJob=True)
            self.laserJobsBook.deleteJob(jobId)
            filteredJobs = (self.laserJobsBook.filterJobs(self.filter))
            filteredJobs_Count = LaserJobs_Book.countJobs(filteredJobs)
            self.notify((filteredJobs, filteredJobs_Count[0], filteredJobs_Count[1], filteredJobs_Count[2], self.laserJobsFilepath+self.laserJobsFilename))

        except PermissionError as pe:
            messagebox.showerror("Excel opened!!!!!", "The excel file must be closed if you want to add new jobs!!!!!")

        except Exception as inst:
            raise (inst)

    def getJob(self, jobId):
        return self.laserJobsBook.getJob(jobId)

    def updateJob(self,updatedJobData):
        self.laserJobsBook.updateJob(updatedJobData)
        self.laserJobsBook.updateJobsSource(self.laserJobsFilepath, self.laserJobsFilename, updatedJobData)
        self.laserJobsBook.sort(key=lambda k: k['jobId'])
        filteredJobs = (self.laserJobsBook.filterJobs(self.filter))
        filteredJobs_Count = LaserJobs_Book.countJobs(filteredJobs)
        self.notify((filteredJobs, filteredJobs_Count[0], filteredJobs_Count[1], filteredJobs_Count[2], self.laserJobsFilepath+self.laserJobsFilename))


    def updateTextFilterList(self,sv):
        self.filter.textList = str.split(sv,';')
        filteredJobs = (self.laserJobsBook.filterJobs(self.filter))
        filteredJobs_Count = LaserJobs_Book.countJobs(filteredJobs)
        self.notify((filteredJobs, filteredJobs_Count[0], filteredJobs_Count[1], filteredJobs_Count[2], self.laserJobsFilepath+self.laserJobsFilename))

    def updateTextFilterOptions(self, cs_option, and_option, wholeword_option):
        self.filter.caseSensitiveOption = cs_option
        self.filter.andOption = and_option
        self.filter.wholeWordOption = wholeword_option
        filteredJobs = (self.laserJobsBook.filterJobs(self.filter))
        filteredJobs_Count = LaserJobs_Book.countJobs(filteredJobs)
        self.notify((filteredJobs, filteredJobs_Count[0], filteredJobs_Count[1], filteredJobs_Count[2], self.laserJobsFilepath+self.laserJobsFilename))

        self.updateConfigFile()

    def updateLaserJobsFileLocation(self, laserJobsFilepath, laserJobsFilename):
        self.laserJobsFilepath = laserJobsFilepath
        self.laserJobsFilename = laserJobsFilename
        self.updateConfigFile()
        self.loadJobsFromSource(laserJobsFilepath, laserJobsFilename, self.filter)

    def updateConfigFile(self):

        # save changes to file
        configData = dict()
        configData['textFilterOptions'] = self.filter.getTextFilterOptions()
        configData['laserJobsFileLocation'] = {'laserJobsFilePath':self.laserJobsFilepath,'laserJobsFileName':self.laserJobsFilename}

        with open(self.configFilenamePath + self.configFilename, 'w') as f:
            json.dump(configData, f)

    def start(self):

        delay = 2000
        GuiController.showLoadingJobsWindow(delay)
        # first time we load the laser jobs
        # we give time to guicontroller for creating the main window before load the laser jobs
        t = Timer(delay/1000, self.loadJobsFromSource, [self.laserJobsFilepath, self.laserJobsFilename, self.filter])
        t.start()

        self.guiController.start()
