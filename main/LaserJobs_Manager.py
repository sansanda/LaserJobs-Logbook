from Gui.GuiController import GuiController
from Logic.LogicController import LogicController
from Gui.MainWindow import MainWindow
from Logic.LaserJobs import LaserJob
import os

from tkinter import Tk

def main():

    #TODO: create standalone exe and liberate it
    configFilePath = '..\\persistence\\config\\'
    configFileName = 'config.json'

    lc = LogicController(configFilePath,configFileName)

    gc = GuiController()


    # ('#0','jobID',10) #0 es el id de la columna, 'jobID' es el texto del encabezado de dicha columna,
    # 10 es el procentaje de ancho de la columna (del total de MainWindow)


    mw = MainWindow(0.9, 0.7)
    mw.setGuiController(gc)
    mw.populate(LaserJob.keys)
    gc.setActualWindow(mw)

    lc.setGuiController(gc)
    lc.start()


if __name__ == "__main__":
    main()
