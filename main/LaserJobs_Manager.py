from Gui.GuiController import GuiController
from Logic.LogicController import LogicController
from Gui.MainWindow import MainWindow
from tkinter import Tk

def main():

    #TODO: create standalone exe and liberate it
    laserJobsPath = '..\\persistence\\data\\'
    laserJobsFileName = 'laserJobs.xlsx'
    filterOptionsPath = '..\\persistence\\config\\'
    filterOptionsFileName = 'config.json'

    lc = LogicController(laserJobsPath, laserJobsFileName, filterOptionsPath,filterOptionsFileName)

    gc = GuiController()


    # ('#0','jobID',10) #0 es el id de la columna, 'jobID' es el texto del encabezado de dicha columna,
    # 10 es el procentaje de ancho de la columna (del total de MainWindow)
    headers = (             ('#0', 'jobID', 5),
                            ('#1', 'Username', 6),
                            ('#2', 'Date', 6),
                            ('#3', 'Material', 5),
                            ('#4', 'V-R-C', 6),
                            ('#5', 'Speed', 5),
                            ('#6', 'Power', 5),
                            ('#7', 'DPI', 5),
                            ('#8', 'Freq', 5),
                            ('#9', '#Passes', 5),
                            ('#10', 'Depth', 5),
                            ('#11', 'VectSort',6),
                            ('#12','FreqAuto',5),
                            ('#13','EngraveDir',6),
                            ('#14','ImageDith',6),
                            ('#15', 'Others', 29))

    mw = MainWindow(0.95, 0.85)
    mw.setGuiController(gc)
    mw.populate(headers)
    gc.setActualWindow(mw)



    lc.setGuiController(gc)
    lc.loadJobsFromExcel()
    lc.start()


if __name__ == "__main__":
    main()
