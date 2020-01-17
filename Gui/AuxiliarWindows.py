"""

Creating an auxiliar windows generator

David SAnchez Sanchez


"""

from tkinter import Toplevel, Message

class AuxiliarWindows():

    def __init__(self):
        pass

    @classmethod
    def showTemporalProcessInfoWindow(cls, destroyTime, title, message):

        infoWindow = Toplevel()
        infoWindow.title(title)
        infoWindow.geometry("%dx%d+%d+%d" % (300, 100, 100, 100))
        Message(infoWindow, text=message, padx=20, pady=20, width=200).pack()
        infoWindow.after(destroyTime, infoWindow.destroy)

    @classmethod
    def showProcessInfoWindow(cls, title, message):
        infoWindow = Toplevel()
        infoWindow.title(title)
        infoWindow.geometry("%dx%d+%d+%d" % (300, 100, 100, 100))
        Message(infoWindow, text=message, padx=20, pady=20, width=200).pack()
        return infoWindow