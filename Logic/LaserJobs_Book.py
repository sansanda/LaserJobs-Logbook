"""

Creating a Laser Jobs Book to store all the laser jobs

David SAnchez Sanchez


"""

from Logic.Filter.IFilter import IFilter
from Logic.LaserJobs import VectorJob
from Logic.LaserJobs import RasterJob
from Logic.LaserJobs import CombinedJob

from Data.Excel_Utilities.ExcelUtils_OpenpyxlBased import loadJobsFromExcel
from Data.Excel_Utilities.ExcelUtils_OpenpyxlBased import insertRowInExcel
from Data.Excel_Utilities.ExcelUtils_OpenpyxlBased import deleteRowInExcel


class LaserJobs_Book(list):

    def __init__(self):
        list.__init__(self)

    def filterJobs(self, IFilter):
        laserJobsFiltered = list()
        for laserJob in self:
            if IFilter.satisfies(laserJob):
                laserJobsFiltered.append(laserJob)
        return laserJobsFiltered

    # Job CRUD

    # newjobData as dictionary
    def newJob(self, laserJob):

        if self.existJob(int(laserJob['jobId'])) == -1:
            self.append(laserJob)
        else:
            raise Exception('The job dat with Id=' + str(laserJob['jobId']) + ' already exists!!!!')

    # return jobData as dictionary with Id equals to jobId
    # jobId could be a integer or a str castable to integer

    def getJob(self, laserJobId):
        laserJobIdIndex = self.existJob(int(laserJobId))
        if not laserJobIdIndex == -1:
            return self[laserJobIdIndex]
        else:
            raise Exception('The job dat with Id=' + str(laserJobId) + ' does not exists!!!!')

    # updatedLaserJob as dictionary without Id
    def updateJob(self, updatedLaserJob):
        self.deleteJob(updatedLaserJob)
        self.newJob(updatedLaserJob)

    # delete job indicated by laserJobId
    def deleteJob(self, laserJobId):
        jobDataIndex = self.existJob(laserJobId)
        if not jobDataIndex == -1:
            del self[jobDataIndex]
        else:
            raise Exception('The job dat with Id=' + str(laserJobId) + ' already exists!!!!')

    def deleteAllJobs(self):
        self.clear()

    # jobList Ids are 1 based.
    def getFirstFreeId(self):
        lastLaserJobId = 0
        for laserJobIndex, laserJob in enumerate(self):
            actualLaserJobId = laserJob['jobId']
            if (actualLaserJobId - lastLaserJobId) > 1:
                # We have a free id in between
                return laserJobIndex + 1
            else:
                lastLaserJobId = actualLaserJobId

        # empty book case
        return (len(self) + 1)  # +1 because list is zero referenced.

    # jobId could be an integer or an str parseable to int
    # return the index of the job if the job exists. -1 otherwise
    def existJob(self, laserJobId):
        laserJobIndex = -1
        for index in range(len(self)):
            if int(self[index]['jobId']) == int(laserJobId):
                exists = True
                laserJobIndex = index
                break
        return laserJobIndex

    def loadJobsFromSource(self, laserJobsFilepath, laserJobsFilename, filter):
        self.deleteAllJobs()
        loadJobsFromExcel(self, laserJobsFilepath, laserJobsFilename)
        filteredJobs = (self.filterJobs(filter))
        filteredJobs.sort(key=lambda k: k['jobId'])
        filteredJobs_Count = LaserJobs_Book.countJobs(filteredJobs)
        return filteredJobs, filteredJobs_Count[0], filteredJobs_Count[1], filteredJobs_Count[2]

    def updateJobsSource(self, laserJobsFilepath, laserJobsFilename, updatedJobData, deleteJob=False):
        if deleteJob == False:
            insertRowInExcel(updatedJobData, laserJobsFilepath, laserJobsFilename)
        elif deleteJob == True:
            deleteRowInExcel(updatedJobData, laserJobsFilepath, laserJobsFilename)

#class methods
    @classmethod
    def countJobs(cls, laserJobs):

        nVectorJobs, nRasterJobs, nCombinedJobs = 0, 0, 0

        for laserJob in laserJobs:

            if isinstance(laserJob, CombinedJob):  # combinedJob first because is isntance of vector and raster
                nCombinedJobs = nCombinedJobs + 1  # we don't want to count double
                continue

            if isinstance(laserJob, VectorJob):
                nVectorJobs = nVectorJobs + 1
                continue

            if isinstance(laserJob, RasterJob):
                nRasterJobs = nRasterJobs + 1
                continue

        return nVectorJobs, nRasterJobs, nCombinedJobs