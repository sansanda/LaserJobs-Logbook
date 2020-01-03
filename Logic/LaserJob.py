"""

Creating a Laser Jobs Book to store all the laser jobs

David SAnchez Sanchez


"""


class LaserJob(dict):

    def __init__(self,id=1,username='username',date='01/01/2000',material='PMMA',jobType='Cut',
                 speed=100,power=100,dpi=1200,freq=5000,nPasses='1/0',rasterDepth=1,others='Other data of interest'):
        self['jobId'] = id
        self['Username'] = username
        self['Date'] = date
        self['Material'] = material
        self['Cut_Raster'] = jobType
        self['Speed'] = speed
        self['Power'] = power
        self['DPI'] = dpi
        self['Freq'] = freq
        self['Passes'] = nPasses
        self['RasterDepth'] = rasterDepth
        self['Others'] = others

    def containsText(self, text, wholeWord, caseSensitive):

        matched = False

        textToFind = str(text)
        if not caseSensitive:
            textToFind = str.upper(textToFind)

        for data in LaserJob.getJobDataAsList(self):
            dataSource = str(data)
            if not caseSensitive:
                dataSource = str.upper(dataSource)

            if wholeWord:
                if dataSource == textToFind:
                    matched = True
                    break
            else:
                if not (dataSource.find(textToFind) == -1):
                    matched = True
                    break

        return matched

    def getJobDataAsList(self):

        jobDataAsList = list()
        for key in self.keys():
            jobDataAsList.append(self[key])
        return jobDataAsList


