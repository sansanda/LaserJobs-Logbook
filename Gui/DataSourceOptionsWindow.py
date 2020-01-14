"""

Creating a  window class GUI for entering the data of a new laser job

David SAnchez Sanchez


"""
import os
import tkinter
from tkinter import *
from tkinter import filedialog


class DataSourceOptionsWindow():

    def __init__(self, w, h, guiController, laserJobsPath, laserJobsFileName):
        # pixels of the window
        self.width = w
        self.height = h

        self.guiController = guiController
        self.root = tkinter.Tk(className='DataSourceOptionsWindow')
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.root.title('Laser-Jobs Manager. Data Source Options.')
        self.root.iconbitmap('../Gui/icons/laserJobsManager_Icon5.ico')

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.root.winfo_screenwidth() / 2 - self.width / 2)
        positionDown = int(self.root.winfo_screenheight() / 2 - self.height / 2)

        self.laserJobsLocation = StringVar(self.root, laserJobsPath + laserJobsFileName)

        self.root.geometry(
            str(self.width) + 'x' + str(self.height) + "+" + str(positionRight) + "+" + str(positionDown))
        self.root.resizable(1, 1)
        self.populate()

    def populate(self):
        self.create_menu_bar()
        self.createLabelsAndEntries()
        self.createOKAndCancelButtons()

    def create_menu_bar(self):
        self.menubar = Menu(self.root)
        self.fileMenu = Menu(self.root, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.close)

        self.root.config(menu=self.menubar)

    def createLabelsAndEntries(self):
        dataSourceOptions_frame = Frame(self.root)
        dataSourceOptions_frame.config(width=self.width)
        dataSourceOptions_frame.grid(row=0, padx=2, pady=5, sticky=W + E + N + S)

        pathLabelText = 'Data source path'
        self.pathLabel = Label(dataSourceOptions_frame, text=pathLabelText)
        self.pathLabel.config(width=len(pathLabelText))
        self.pathLabel.grid(row=0, column=0, padx=2, pady=5, sticky=W)

        self.pathEntry = Entry(dataSourceOptions_frame, textvariable=self.laserJobsLocation)
        self.pathEntry.grid(row=0, column=1, padx=5, pady=5, sticky=W)
        self.pathEntry.config(width=int(len(self.laserJobsLocation.get()) * 0.6))
        self.pathEntry.config(state='readonly')

        Button(dataSourceOptions_frame, text="Browse", command=self.browseLaserJobsFile_Location) \
            .grid(row=0, column=2, padx=5, pady=5, sticky=W)

    def createOKAndCancelButtons(self):
        okAndCancelButtons_frame = Frame(self.root)
        okAndCancelButtons_frame.config(width=self.width)
        okAndCancelButtons_frame.grid(row=1, column=0, padx=2, pady=5, sticky=W + E + N + S)
        self.okButton = Button(okAndCancelButtons_frame, command=self.updateLaserJobsFileLocation, text='OK', width=10)
        self.okButton.grid(row=0, column=0, padx=5, pady=2, sticky=E)
        self.cancelButton = Button(okAndCancelButtons_frame, command=lambda: self.guiController.closeWindow(self),
                                   text='Cancel', width=10)
        self.cancelButton.grid(row=0, column=1, padx=5, pady=2, sticky=E)


    def updateLaserJobsFileLocation(self):
        print('Updating the laser jobs file location...')
        self.guiController.updateLaserJobsFileLocation(os.path.split(self.laserJobsLocation.get())[0]+'/',
                                                       os.path.split(self.laserJobsLocation.get())[1]) #first parameter the file path, second parameter the filename with its extension
        self.close()

    def browseLaserJobsFile_Location(self):
        filenameLocation = filedialog.askopenfilename(initialdir=os.path.split(self.laserJobsLocation.get())[0]+'/')
        if len(filenameLocation) == 0: filenameLocation = self.laserJobsLocation.get()
        self.laserJobsLocation.set(filenameLocation)
        self.root.focus_force()

    def show(self):
        self.enable(True)
        self.root.focus_force()
        self.root.mainloop()

    def enable(self, enable):
        self.root.attributes('-disabled', not enable)

    def close(self):
        print('Exiting...')
        self.guiController.closeWindow(self)