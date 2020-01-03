from Gui.GuiController import GuiController
from Logic.LogicController import LogicController
from Gui.MainWindow import MainWindow
from tkinter import Tk

def main():
    laserJobsPath = '..\\Data\\'
    laserJobsFileName = 'laserJobs.xlsx'
    filterOptionsPath = '..\\persistence\\config\\'
    filterOptionsFileName = 'config.json'

    lc = LogicController(laserJobsPath, laserJobsFileName, filterOptionsPath,filterOptionsFileName)

    gc = GuiController()


    # ('#0','jobID',0.1) #0 es el id de la columna, 'jobID' es el texto del encabezado de dicha columna,
    # 10 es el procentaje de ancho de la columna (del total de MainWindow)
    headers = (             ('#0', 'jobID', 5),
                            ('#1', 'Username', 10),
                            ('#2', 'Date', 7),
                            ('#3', 'Material', 5),
                            ('#4', 'Cut_Raster', 7),
                            ('#5', 'Speed', 5),
                            ('#6', 'Power', 5),
                            ('#7', 'DPI', 5),
                            ('#8', 'Freq', 5),
                            ('#9', '#Passes', 5),
                            ('#10', 'RasterDepth', 7),
                            ('#11', 'Others', 44))
    mw = MainWindow(0.8, 0.7)
    mw.setGuiController(gc)
    mw.populate(headers)
    gc.setActualWindow(mw)



    lc.setGuiController(gc)
    lc.loadJobsFromExcel()
    lc.start()


if __name__ == "__main__":
    main()
