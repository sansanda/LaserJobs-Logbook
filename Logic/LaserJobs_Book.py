"""

Creating a Laser Jobs Book to store all the laser jobs

David SAnchez Sanchez


"""


class LaserJobs_Book(list):

    def __init__(self):
        list.__init__(self)

    # Job CRUD

    # newjobData as dictionary without Id
    def newJob(self, newJobData):
        if not self.existJob(newJobData['jobId']):
            self.append(newJobData)
        else:
            raise (newJobData['jobId'] + ' already exists!!!!')

    # return jobData as dictionary with Id
    # the job data in the list is store as a dictionary without jobId.
    # So we have to insert it before returning the data
    def getJob(self, jobId):
        jobIdAsInt = int(jobId)
        if self.existJob(jobIdAsInt):
            jobData = self[jobIdAsInt]
            jobData['jobId'] = jobId
            return jobData
        else:
            raise (jobId + ' does not exists!!!!')

    # updatedJobData as dictionary without Id
    def updateJob(self, updatedJobData):
        if self.existJob(updatedJobData['jobId']):
            self.deleteJob(updatedJobData['jobId'])
            self.append(updatedJobData)
        else:
            raise (updatedJobData['jobId'] + ' does not exists!!!!')

    # delete job indicated by jobId
    def deleteJob(self, jobId):
        jobIdAsInt = int(jobId)
        if self.existJob(jobIdAsInt):
            self.remove(self[jobIdAsInt])
        else:
            raise (jobId + ' does not exists!!!!')

    def getFirstFreeId(self):
        return len(self)

    def deleteAllJobs(self):
        self.clear()

    def existJob(self, jobId):
        exists = True
        try:
            print(self[jobId])
        except IndexError:
            exists = False
        return exists
