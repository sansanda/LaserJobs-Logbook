from Gui.GuiController import GuiController
from Logic.LogicController import LogicController
from Gui.MainWindow import MainWindow
from tkinter import Tk

def main():
    laserJobsPath = '..\\persistence\\data\\'
    laserJobsFileName = 'laserJobs.xlsx'
    filterOptionsPath = '..\\persistence\\config\\'
    filterOptionsFileName = 'config.json'

    lc = LogicController(laserJobsPath, laserJobsFileName, filterOptionsPath,filterOptionsFileName)

    gc = GuiController()


    # ('#0','jobID',0.1) #0 es el id de la columna, 'jobID' es el texto del encabezado de dicha columna,
    # 10 es el procentaje de ancho de la columna (del total de MainWindow)
    headers = (             ('#0', 'jobID', 5),
                            ('#1', 'Username', 5),
                            ('#2', 'Date', 5),
                            ('#3', 'Material', 5),
                            ('#4', 'V-R-C', 5),
                            ('#5', 'Speed', 5),
                            ('#6', 'Power', 5),
                            ('#7', 'DPI', 5),
                            ('#8', 'Freq', 5),
                            ('#9', '#Passes', 5),
                            ('#10', 'Depth', 5),
                            ('#11', 'VectSort',5),
                            ('#12','FreqAuto',5),
                            ('#13','EngraveDir',5),
                            ('#14','ImageDith',5),
                            ('#15', 'Others', 35))
    mw = MainWindow(0.9, 0.65)
    mw.setGuiController(gc)
    mw.populate(headers)
    gc.setActualWindow(mw)



    lc.setGuiController(gc)
    lc.loadJobsFromExcel()
    lc.start()


if __name__ == "__main__":
    main()
