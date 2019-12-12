"""

Creating a Laser Jobs Book to store all the laser jobs

David SAnchez Sanchez


"""

class LaserJobs_Book(list):


    def __init__(self):
        list.__init__(self)

    #Job CRUD

    #newjobData as dictionary without Id
    def newJob(self, newjobData):
        jobId = len(self)
        if not self.existJob(jobId):
            newjobData['jobId'] = jobId
            self.append(newjobData)
            print(newjobData)
            #TODO: Notificate that the book has changed
        else:
            raise (jobId + ' already exists!!!!')

    #return jobData as dictionary with Id
    def getJob(self, jobId):
        if self.existJob(jobId):
            return self[jobId]
        else:
            raise (jobId + ' does not exists!!!!')

    #updatedJobData as dictionary without Id
    def updateJob(self,updatedJobData):
        if self.existJob(updatedJobData['jobId']):
            self.deleteJob(updatedJobData['jobId'])
            self.append(updatedJobData)
            # TODO: Notificate that the book has changed
        else:
            raise (jobId + ' does not exists!!!!')

    #delete job indicated by jobId
    def deleteJob(self,jobId):
        if self.existJob(jobId):
            self.remove(self[jobId])
            # TODO: Notificate that the book has changed
        else:
            raise (jobId + ' does not exists!!!!')


    def existJob(self, jobId):
        exists = True
        try:
            self[jobId]
        except IndexError:
            exists = False
        return exists
