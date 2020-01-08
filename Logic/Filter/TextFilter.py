from Logic.Filter.IFilter import IFilter

class TextFilter(IFilter):

    def __init__(self, textList, caseSensitiveOption=True, andOption=True, wholeWordOption=True):
        self.textList = textList
        self.caseSensitiveOption = caseSensitiveOption
        self.andOption = andOption
        self.wholeWordOption = wholeWordOption

    def satisfies(self,laserJob):

        if len(self.textList) == 1 and self.textList[0]=='': return True

        if self.andOption:
            return self.__allTextAreInLaserJob(laserJob)
        else:
            return self.__atLeastOneTextIsInLaserJob(laserJob)

    def getName(self):
        return 'TextFilter'

    def getTextFilterOptions(self):
        textFilterOptions = dict()
        textFilterOptions['caseSensitive'] = self.caseSensitiveOption
        textFilterOptions['and'] = self.andOption
        textFilterOptions['wholeWord'] = self.wholeWordOption
        return textFilterOptions

    #auxiliar methods
    def __allTextAreInLaserJob(self, laserJob):
        for text in self.textList:
            if not LaserJob.containsText(laserJob,text,self.wholeWordOption,self.caseSensitiveOption):
                return False
        return True


    def __atLeastOneTextIsInLaserJob(self, laserJob):
        for text in self.textList:
            if LaserJob.containsText(laserJob, text,self.wholeWordOption,self.caseSensitiveOption):
                return True
        return False
