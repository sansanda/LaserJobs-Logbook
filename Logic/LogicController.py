"""

Creating a Logic Controller to control the logic part of the Laser Job Manager

David SAnchez Sanchez


"""

from Logic.LaserJobs_Book import LaserJobs_Book

class LogicController():

    def __init__(self,sourceURL):
        self.guiController = None
        self.laserJobsBook = LaserJobs_Book(sourceURL)

    def setGuiController(self,guicontroller):
        self.guiController = guicontroller
        self.guiController.setLogicController(self)

    def getGuiController(self):
        return self.guiController

    def createNewJob(self,newJobdata):
        self.laserJobsBook.createNewJob(newJobdata)
    def start(self):
        self.guiController.start()