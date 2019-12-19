"""

Creating a Laser Jobs Book to store all the laser jobs

David SAnchez Sanchez


"""


class LaserJobs_Book(list):

    jobAtributes = dict()
    jobAtributes['jobId'] = 'jobId'
    jobAtributes['Username'] = 'Username'
    jobAtributes['Date'] = 'Date'
    jobAtributes['Material'] = 'Material'
    jobAtributes['Cut_Raster'] = 'Cut_Raster'
    jobAtributes['Speed'] = 'Speed'
    jobAtributes['Power'] = 'Power'
    jobAtributes['DPI'] = 'DPI'
    jobAtributes['Freq'] = 'Freq'
    jobAtributes['Passes'] = 'Passes'
    jobAtributes['RasterDepth'] = 'RasterDepth'
    jobAtributes['Others'] = 'Others'

    def __init__(self):
        list.__init__(self)

    # Job CRUD

    # newjobData as dictionary
    def newJob(self, newJobData):
        if self.existJob(int(newJobData['jobId'])) == -1:
            self.append(newJobData)
        else:
            raise Exception('The job dat with Id=' + str(newJobData['jobId']) + ' already exists!!!!')

    # return jobData as dictionary with Id equals to jobId
    # jobId could be a integer or a str castable to integer

    def getJob(self, jobId):
        jobIdIndex = self.existJob(int(jobId))
        if not jobIdIndex == -1:
            return self[jobIdIndex]
        else:
            raise Exception('The job dat with Id=' + jobId + ' does not exists!!!!')

    # updatedJobData as dictionary without Id
    def updateJob(self, updatedJobData):
        self.deleteJob(updatedJobData)
        self.newJob(updatedJobData)

    # delete job indicated by jobId
    def deleteJob(self, jobId):
        jobDataIndex = self.existJob(jobId)
        if not jobDataIndex == -1:
            del self[jobDataIndex]
        else:
            raise Exception('The job dat with Id=' + jobId + ' already exists!!!!')

    #jobList Ids are 1 based.
    def getFirstFreeId(self):
        lastJobId = 0
        for jobIndex,job in enumerate(self):
            actualJobId = int(job[LaserJobs_Book.jobAtributes['jobId']])
            if (actualJobId-lastJobId)>1:
                #We have a free id in between
                return jobIndex + 1
            else:
                lastJobId = actualJobId

        #empty book case
        return (len(self)+1) #+1 because list is zero referenced.

    def deleteAllJobs(self):
        self.clear()

    # jobId could be an integer or an str parseable to int
    # return the index of the job if the job exists. -1 otherwise
    def existJob(self, jobId):
        jobIndex = -1
        for index in range(len(self)):
            if int(self[index]['jobId']) == int(jobId):
                exists = True
                jobIndex = index
                break
        return jobIndex

    #jobData is a dict
    @classmethod
    def getJobDataAsList(cls,jobData):
        jobDataAsList = list()
        jobDataAsList.append(jobData[cls.jobAtributes['jobId']])
        jobDataAsList.append(jobData[cls.jobAtributes['Username']])
        jobDataAsList.append(jobData[cls.jobAtributes['Date']])
        jobDataAsList.append(jobData[cls.jobAtributes['Material']])
        jobDataAsList.append(jobData[cls.jobAtributes['Cut_Raster']])
        jobDataAsList.append(jobData[cls.jobAtributes['Speed']])
        jobDataAsList.append(jobData[cls.jobAtributes['Power']])
        jobDataAsList.append(jobData[cls.jobAtributes['DPI']])
        jobDataAsList.append(jobData[cls.jobAtributes['Freq']])
        jobDataAsList.append(jobData[cls.jobAtributes['Passes']])
        jobDataAsList.append(jobData[cls.jobAtributes['RasterDepth']])
        jobDataAsList.append(jobData[cls.jobAtributes['Others']])
        return jobDataAsList

    #TODO: Create jobData class