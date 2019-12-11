"""

Creating a Laser Jobs Book to store all the laser jobs

David SAnchez Sanchez


"""

class LaserJobs_Book(list):


    def __init__(self):
        list.__init__(self)

    def updateJobsSource(self):
        pass


    #Job CRUD

    #newjobData as dictionary
    def createNewJob(self, newjobData):
        newjobData['jobId'] = len(self)
        self.append(newjobData)

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
