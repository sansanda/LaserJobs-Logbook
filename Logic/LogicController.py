"""

Creating a Logic Controller to control the logic part of the Laser Job Manager

David SAnchez Sanchez


"""

from Logic.LaserJobs_Book import LaserJobs_Book
from Data.Excel_Utilities.ExcelUtils import loadJobsFromExcel
from Data.Excel_Utilities.ExcelUtils import updateExcel
from Logic.DesignPatterns.ObserverPattern import Publisher


class LogicController(Publisher):

    def __init__(self,sourceURL):
        Publisher.__init__(self)
        self.guiController = None
        self.laserJobsBook = LaserJobs_Book()
        self.sourceURL = sourceURL
        self.loadJobsFromExcel(self.laserJobsBook, self.sourceURL)


    def setGuiController(self,guicontroller):
        self.guiController = guicontroller
        self.guiController.setLogicController(self)

    def getGuiController(self):
        return self.guiController

    def loadJobsFromExcel(self, laserJobsBook, sourceURL):
        loadJobsFromExcel(laserJobsBook,sourceURL)

    def updateExcel(self, updatedJobData, sourceURL):
        updateExcel(updatedJobData,sourceURL)

    def newJob(self,newJobData):
        # TODO implements newJob
        try:
            self.laserJobsBook.newJob(newJobData)
        except Exception as inst:
            print(type(inst))  # the exception instance
            print(inst.args)  # arguments stored in .args
            print(inst)  # __str__ allows args to be printed directly,
            x, y = inst.args  # unpack args
            print('x =', x)
            print('y =', y)




    def getJob(self, jobId):
        # TODO implement getJob
        return self.laserJobsBook.getJob(jobId)

    def updateJob(self,updatedJobData):
        # TODO implement updateJob
        self.laserJobsBook.updateJob(updatedJobData)

    def deleteJob(self,jobId):
        #TODO implement deleteJob
        self.laserJobsBook.deleteJob(jobId)

    def start(self):
        self.guiController.start()