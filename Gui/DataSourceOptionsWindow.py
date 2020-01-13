"""

Creating a  window class GUI for entering the data of a new laser job

David SAnchez Sanchez


"""
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

        self.laserJobsPath = StringVar(self.root)
        self.laserJobsFileName = StringVar(self.root)

        self.root.geometry(str(self.width) + 'x' + str(self.height) + "+" +str(positionRight) + "+" + str(positionDown))
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
        dataSourceOptions_frame.config(height=self.height-25, width=self.width)
        dataSourceOptions_frame.grid(row=0, columnspan=12, rowspan=10, padx=5, pady=5, sticky=W + E + N + S)


        self.pathLabel = Label(dataSourceOptions_frame, text='Data source path')
        self.pathLabel.config(width=20)
        self.pathLabel.grid(row=0, column=0, sticky=W)

        self.pathEntry = Entry(dataSourceOptions_frame, textvariable=self.laserJobsPath)
        self.pathEntry.grid(row=0, column=1, sticky=W)
        self.pathEntry.config(width=20)
        self.pathEntry.config(state='normal')

        Button(dataSourceOptions_frame, text="Browse", command=self.browsePathLabel)\
            .grid(row=0, column=2, sticky=W)

        self.filenameLabel = Label(dataSourceOptions_frame, text='Data source filename')
        self.filenameLabel.config(width=20)
        self.filenameLabel.grid(row=1, column=0, sticky=W)

        self.filenameEntry = Entry(dataSourceOptions_frame, textvariable=self.laserJobsFileName)
        self.filenameEntry.grid(row=0, column=1, sticky=W)
        self.filenameEntry.config(width=20)
        self.filenameEntry.config(state='normal')


        Button(dataSourceOptions_frame, text="Browse", command=self.browseFilename)\
            .grid(row=1, column=2, sticky=W)


    def createOKAndCancelButtons(self):
        okAndCancelButtons_frame = Frame(self.root)
        okAndCancelButtons_frame.config(width= self.width)
        okAndCancelButtons_frame.grid(row=2, column=0, columnspan=2, sticky=W + E + N + S)
        self.okButton = Button(okAndCancelButtons_frame, command=self.updateTextFilterOptions, text='OK', width=10)
        self.okButton.grid(row=0, column=0, padx=5, pady=2, sticky=E)
        self.cancelButton = Button(okAndCancelButtons_frame, command= lambda: self.guiController.closeWindow(self), text='Cancel', width=10)
        self.cancelButton.grid(row=0, column=1, padx=5, pady=2, sticky=E)

    def enable(self, enable):
        self.root.attributes('-disabled', not enable)

    def close(self):
        print('Exiting...')
        self.guiController.closeWindow(self)

    def updateTextFilterOptions(self):
        print('Applying filter options...')
        self.guiController.updateTextFilterOptions(self.case_sensitive_option.get(),self.and_option.get(),self.wholeword_option.get())
        self.close()

    def browsePathLabel(self):
        self.laserJobsPath = filedialog.askopenfilename()

    def browseFilename(self):
        self.laserJobsFileName = filedialog.askopenfilename()



    def show(self):
        self.enable(True)
        self.root.focus_force()
        self.root.mainloop()