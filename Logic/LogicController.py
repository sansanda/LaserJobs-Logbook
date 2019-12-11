"""

Creating a Logic Controller to control the logic part of the Laser Job Manager

David SAnchez Sanchez


"""
import xlrd

from Logic.LaserJobs_Book import LaserJobs_Book

class LogicController():

    def __init__(self,sourceURL):
        self.guiController = None
        self.laserJobsBook = LaserJobs_Book()

    def setGuiController(self,guicontroller):
        self.guiController = guicontroller
        self.guiController.setLogicController(self)

    def getGuiController(self):
        return self.guiController


    def loadJobsFromExcel(self, sourceURL):

        workbook = xlrd.open_workbook(sourceURL, on_demand=True)
        worksheet = workbook.sheet_by_index(0)
        columns_row = []  # The row where we stock the name of the column

        for col in range(worksheet.ncols):
            columns_row.append(worksheet.cell_value(0, col))

        # tronsform the workbook to a list of dictionnary
        for row in range(1, worksheet.nrows):
            elm = {}
            for col in range(worksheet.ncols - 1):
                elm[columns_row[col+1]] = str(worksheet.cell_value(row, col+1))
            self.laserJobsBook.append(elm)

    def createNewJob(self,newJobdata):
        self.laserJobsBook.createNewJob(newJobdata)

    def start(self):
        self.guiController.start()