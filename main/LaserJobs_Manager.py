from Gui.GuiController import GuiController
from Logic.LogicController import LogicController
from Gui.MainWindow import MainWindow

def main():
    laserJobsPath = '..\\Data\\'
    laserJobsFileName = 'laserJobs_inxls.xls'
    lc = LogicController(laserJobsPath, laserJobsFileName)
    gc = GuiController()


    # ('#0','jobID',0.1) #0 es el id de la columna, 'jobID' es el texto del encabezado de dicha columna,
    # 10 es el procentaje de ancho de la columna (del total de MainWindow)
    headers = (             ('#0', 'jobID', 5),
                            ('#1', 'Username', 10),
                            ('#2', 'Date', 10),
                            ('#3', 'Material', 10),
                            ('#4', 'Cut_Raster', 10),
                            ('#5', 'Speed', 10),
                            ('#6', 'Power', 5),
                            ('#7', 'DPI', 5),
                            ('#8', 'Freq', 5),
                            ('#9', '#Passes', 5),
                            ('#10', 'RasterDepth', 10),
                            ('#11', 'Others', 25))
    mw = MainWindow(1400, 650)
    mw.setGuiController(gc)
    mw.populate(headers)
    gc.setActualWindow(mw)

    lc.setGuiController(gc)
    #add a observer
    lc.addObserver(gc.actualWindow)
    lc.loadJobsFromExcel()
    lc.start()


if __name__ == "__main__":
    main()
