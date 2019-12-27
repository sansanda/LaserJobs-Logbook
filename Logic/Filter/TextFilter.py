from Logic.Filter.IFilter import IFilter
from Logic.LaserJob import LaserJob

class TextFilter(IFilter):

    def __init__(self, textList, caseSensitiveOption=True, andOption=True):
        self.textList = textList
        self.caseSensitiveOption = caseSensitiveOption
        self.andOption = andOption

    def satisfies(self,laserJob):
        if self.andOption:
            return self.__allTextAreInLaserJob(laserJob)
        else:
            return self.__atLeastOneTextIsInLaserJob(laserJob)

    def getName(self):
        return 'TextFilter'

    #auxiliar methods
    def __allTextAreInLaserJob(self, laserJob):
        if not self.caseSensitiveOption:
            for text in self.textList:
                if text.upper() not in [value.upper() for value in LaserJob.getJobDataAsList(laserJob)]:
                    return False
        else:
            for text in self.textList:
                if text not in LaserJob.getJobDataAsList(laserJob):
                    return False
        return True

    def __atLeastOneTextIsInLaserJob(self, laserJob):
        if not self.caseSensitiveOption:
            for text in self.textList:
                if text.upper() in [value.upper() for value in LaserJob.getJobDataAsList(laserJob)]:
                    return True
        else:
            for text in self.textList:
                if text in LaserJob.getJobDataAsList(laserJob):
                    return True
        return False
