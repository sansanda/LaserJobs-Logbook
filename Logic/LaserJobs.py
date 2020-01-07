class LaserJob(dict):

    def __init__(self,id=1,username='username',date='01/01/2000',material='PMMA',
                 speed=100,power=100,dpi=1200,nPasses=1,others='Other data of interest'):
        self['jobId'] = id
        self['Username'] = username
        self['Date'] = date
        self['Material'] = material
        self['Speed'] = speed
        self['Power'] = power
        self['DPI'] = dpi
        self['Passes'] = nPasses
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

    def getJobDataAsList(self):

        jobDataAsList = list()
        for key in self.keys():
            jobDataAsList.append(self[key])
        return jobDataAsList

    def getJobDataAsStrRepresentation(self):

        jobDataAsList = list()
        for key in self.keys():
            jobDataAsList.append(str(key) + ':' + str(self[key]))
        return jobDataAsList


    def __str__(self):
        """Devuelve una cadena representativa al LaserJob"""

        return "Job Parameters: %s" % self.getJobDataAsStrRepresentation()

class Raster(LaserJob):

    def __init__(self,id=1,username='username',date='01/01/2000',material='PMMA',
                 speed=100,power=100,dpi=1200,nPasses=1,depth=1,others='Other data of interest',
                 engraveDirection='Top-Down', imageDithering='Standard'):

        LaserJob.__init__(self,id,username,date,material,speed,power,dpi,nPasses,others)

        self['JobType'] = 'Raster'
        self['Depth'] = depth
        self['EngraveDirection'] = engraveDirection
        self['ImageDithering'] = imageDithering


class Vector(LaserJob):

    def __init__(self,id=1,username='username',date='01/01/2000',material='PMMA',
                 speed=100,power=100,dpi=1200,nPasses=1,others='Other data of interest',
                 vectorSorting='Optimize', frequencyAutomatic=False):

        LaserJob.__init__(self,id,username,date,material,speed,power,dpi,nPasses,others)

        self['JobType'] = 'Vector'
        self['VectorSorting'] = vectorSorting
        self['FrequencyAutomatic'] = frequencyAutomatic

class Combined(Raster,Vector):

    def __init__(self,id=1,username='username',date='01/01/2000',material='PMMA',
                 speed=100,power=100,dpi=1200,nPasses=1,depth=1,others='Other data of interest',
                 engraveDirection='Top-Down', imageDithering='Standard',
                 vectorSorting='Optimize', frequencyAutomatic=False):

        Raster.__init__(self, id, username, date, material, speed, power, dpi, nPasses, depth, others,engraveDirection,imageDithering)
        Vector.__init__(self, id, username, date, material, speed, power, dpi, nPasses, others,vectorSorting,frequencyAutomatic)

        self['JobType'] = 'Combined'


def main():
    v = Vector(1,'sansanda','01/01/2010','PMMA',100,100,1200,1,'others','Optimize',False)
    print(v)
    r = Raster(1, 'sansanda', '01/01/2010', 'PMMA', 100, 100, 1200, 1, 1.2, 'others', 'Top-Down', 'Special')
    print(r)
    c = Combined(1, 'sansanda', '01/01/2010', 'PMMA', 100, 100, 1200, 1, 1.2, 'others', 'Top-Down', 'Special', 'Optimize',False)
    print(c)


if __name__ == "__main__":
    main()