from Gui.GuiController import GuiController
from Logic.LogicController import LogicController


def main():
    laserJobsURL = '..\Data\laserJobs_inxls.xls'
    lc = LogicController(laserJobsURL)
    gc = GuiController()
    # ('#0','jobID',0.1) #0 es el id de la columna, 'jobID' es el texto del encabezado de dicha columna,
    # 10 es el procentaje de ancho de la columna (del total de MainWindow)
    gc.configureMainWindow((('#0', 'jobID', 5),
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
                           )

    lc.setGuiController(gc)
    lc.start()
    jd = {'jobId':'1'}
    lc.newJob(jd)

if __name__ == "__main__":
    main()
