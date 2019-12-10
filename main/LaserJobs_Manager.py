from Gui.GuiController import GuiController
from Logic.LogicController import LogicController

def main():
    lc = LogicController()
    gc = GuiController()
    #('#0','jobID',0.1) #0 es el id de la columna, 'jobID' es el texto del encabezado de dicha columna, 10 es el procentaje de ancho de la columna (del total de MainWindow)
    gc.configureMainWindow((('#0','jobID',5),
                            ('#1','Username',10),
                            ('#2','Date',10),
                            ('#3','Material',10),
                            ('#4','Cut/Raster',10),
                            ('#5','Power(%)',5),
                            ('#6','DPI',5),
                            ('#7','Freq(Hz)',5),
                            ('#8','#Passes',5),
                            ('#9','RasterDepth(mm)',10),
                            ('#10','Others',25))
                           )

    lc.setGuiController(gc)
    lc.start()
    print(gc.actualWindow)

if __name__ == "__main__":
    main()