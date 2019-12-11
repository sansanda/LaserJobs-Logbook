"""

Creating a Laser Jobs Book to store all the laser jobs

David SAnchez Sanchez


"""

import xlrd

class LaserJobs_Book(list):


    def __init__(self, sourceURL):
        self.sourceURL = sourceURL
        self.loadJobsFromExcel(sourceURL)

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
            self.append(elm)


    def updateJobsSource(self):
        pass


    #Job CRUD

    #newjobData as dictionary
    def createNewJob(self, newjobData):
        newjobData['jobId'] = len(self)
        self.append(newjobData)
        print(newjobData)

    #return jobData as dictionary
    def getJob(self, jobId):
        pass

    #updatedJobData as dictionary
    def updateJob(self,updatedJobData):
        if self.existJob(updatedJobData['jobId']):
            self.createNewJob(updatedJobData)
        else:
            raise (updatedJobData['jobId'] + ' does not exists!!!!')


    def deleteJob(self,jobId):
        pass



    def existJob(self, jobId):
        pass
