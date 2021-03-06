class LaserJob(dict):

    vectorType = 'Vector'
    rasterType = 'Raster'
    combinedType = 'Combined'
    keys = ['jobId', 'Username', 'Date', 'Material', 'Thickness', 'JobType', 'Speed', 'Power', 'DPI', 'Frequency', 'Passes', 'Depth', 'VectorSorting', 'FrequencyAutomatic', 'EngraveDirection', 'ImageDithering', 'Others']

    def __init__(self,id=1,username='username',date='01/01/2000',material='PMMA', thickness=1,
                 speed=100,power=100,dpi=1200,freq = 5000, nPasses=1, depth=1, others='Other data of interest'):
        self['jobId'] = id
        self['Username'] = username
        self['Date'] = date
        self['Material'] = material
        self['Thickness'] = thickness
        self['Speed'] = speed
        self['Power'] = power
        self['DPI'] = dpi
        self['Frequency'] = freq
        self['Passes'] = nPasses
        self['Depth'] = depth
        self['Others'] = others
        self['JobType'] = 'Not defined'

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

    @classmethod
    def getJobDataAsList(cls, laserJob):

        jobDataAsList = list()
        for key in cls.keys:
            jobDataAsList.append(laserJob[key])

        return jobDataAsList

    @classmethod
    def createLaserJobFromDict(cls, laserJobDataAsDict):

        laserJob = None

        if laserJobDataAsDict['JobType']==LaserJob.vectorType:
            laserJob = VectorJob(
                laserJobDataAsDict['jobId'],
                laserJobDataAsDict['Username'],
                laserJobDataAsDict['Date'],
                laserJobDataAsDict['Material'],
                laserJobDataAsDict['Thickness'],
                laserJobDataAsDict['Speed'],
                laserJobDataAsDict['Power'],
                laserJobDataAsDict['DPI'],
                laserJobDataAsDict['Frequency'],
                laserJobDataAsDict['Passes'],
                laserJobDataAsDict['Depth'],
                laserJobDataAsDict['Others'],
                laserJobDataAsDict['VectorSorting'],
                laserJobDataAsDict['FrequencyAutomatic']
            )

        if laserJobDataAsDict['JobType']==LaserJob.rasterType:
            laserJob = RasterJob(
                laserJobDataAsDict['jobId'],
                laserJobDataAsDict['Username'],
                laserJobDataAsDict['Date'],
                laserJobDataAsDict['Material'],
                laserJobDataAsDict['Thickness'],
                laserJobDataAsDict['Speed'],
                laserJobDataAsDict['Power'],
                laserJobDataAsDict['DPI'],
                laserJobDataAsDict['Frequency'],
                laserJobDataAsDict['Passes'],
                laserJobDataAsDict['Depth'],
                laserJobDataAsDict['Others'],
                laserJobDataAsDict['EngraveDirection'],
                laserJobDataAsDict['ImageDithering']
            )

        if laserJobDataAsDict['JobType']==LaserJob.combinedType:
            laserJob = CombinedJob(
                laserJobDataAsDict['jobId'],
                laserJobDataAsDict['Username'],
                laserJobDataAsDict['Date'],
                laserJobDataAsDict['Material'],
                laserJobDataAsDict['Thickness'],
                laserJobDataAsDict['Speed'],
                laserJobDataAsDict['Power'],
                laserJobDataAsDict['DPI'],
                laserJobDataAsDict['Frequency'],
                laserJobDataAsDict['Passes'],
                laserJobDataAsDict['Depth'],
                laserJobDataAsDict['Others'],
                laserJobDataAsDict['EngraveDirection'],
                laserJobDataAsDict['ImageDithering'],
                laserJobDataAsDict['VectorSorting'],
                laserJobDataAsDict['FrequencyAutomatic']
            )

        return laserJob

class RasterJob(LaserJob):

    def __init__(self, id=1, username='username', date='01/01/2000', material='PMMA', thickness=1,
                 speed=100, power=100, dpi=1200,freq = -1, nPasses=1, depth=1, others='Other data of interest',
                 engraveDirection='Top-Down', imageDithering='Standard'):

        LaserJob.__init__(self,id,username,date,material,thickness, speed,power,dpi,-1, nPasses, depth, others)

        self['JobType'] = 'Raster'
        self['EngraveDirection'] = engraveDirection
        self['ImageDithering'] = imageDithering
        self['VectorSorting'] = None
        self['FrequencyAutomatic'] = None


class VectorJob(LaserJob):

    def __init__(self,id=1,username='username',date='01/01/2000',material='PMMA', thickness=1,
                 speed=100,power=100,dpi=1200,freq=5000, nPasses=1, depth=-1, others='Other data of interest',
                 vectorSorting='Optimize', frequencyAutomatic=False):

        LaserJob.__init__(self,id,username,date,material, thickness, speed,power,dpi,freq, nPasses, -1, others)

        self['JobType'] = 'Vector'
        self['EngraveDirection'] = None
        self['ImageDithering'] = None
        self['VectorSorting'] = vectorSorting
        self['FrequencyAutomatic'] = frequencyAutomatic

class CombinedJob(RasterJob, VectorJob):

    def __init__(self,id=1,username='username',date='01/01/2000',material='PMMA', thickness = 1,
                 speed=100,power=100,dpi=1200, freq=5000, nPasses=1,depth=1,others='Other data of interest',
                 engraveDirection='Top-Down', imageDithering='Standard',
                 vectorSorting='Optimize', frequencyAutomatic=False):

        RasterJob.__init__(self, id, username, date, material, thickness, speed, power, dpi, freq, nPasses, depth, others, engraveDirection, imageDithering)
        VectorJob.__init__(self, id, username, date, material, thickness, speed, power, dpi, freq, nPasses, depth, others, vectorSorting, frequencyAutomatic)

        self['JobType'] = 'Combined'
        self['Frequency'] = freq
        self['Depth'] = depth
        self['EngraveDirection'] = engraveDirection
        self['ImageDithering'] = imageDithering
        self['VectorSorting'] = vectorSorting
        self['FrequencyAutomatic'] = frequencyAutomatic

def main():
    v = VectorJob(1, 'sansanda', '01/01/2010', 'PMMA', 1, 100, 100, 1200, 5000,  1, 'others', 'Optimize', False)
    print(v)
    r = RasterJob(1, 'sansanda', '01/01/2010', 'PMMA', 1, 100, 100, 1200, 1, 1.2, 'others', 'Top-Down', 'Special')
    print(r)
    c = CombinedJob(1, 'sansanda', '01/01/2010', 'PMMA', 10, 100, 100, 1200, 4000, 1, 1.2, 'others', 'Top-Down', 'Special', 'Optimize', False)
    print(c)


if __name__ == "__main__":
    main()