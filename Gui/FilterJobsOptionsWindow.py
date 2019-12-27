"""

Creating a  window class GUI for entering the data of a new laser job

David SAnchez Sanchez


"""
import tkinter
from tkinter import *
from tkinter import ttk
from datetime import date

class FilterJobsOptionsWindow():

    def __init__(self, w, h, guiController, filterOptions):


        # pixels of the window
        self.width = w
        self.height = h

        self.guiController = guiController
        self.root = tkinter.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.root.title('Laser-Jobs Manager. Filter Jobs Options.')
        self.root.iconbitmap('../Gui/icons/laserJobsManager_Icon5.ico')

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.root.winfo_screenwidth() / 2 - self.width / 2)
        positionDown = int(self.root.winfo_screenheight() / 2 - self.height / 2)

        self.filterOptions = filterOptions
        self.root.geometry(str(self.width) + 'x' + str(self.height) + "+" +str(positionRight) + "+" + str(positionDown))
        self.root.resizable(0, 0)
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

        filterJobsOptions_frame = Frame(self.root)
        filterJobsOptions_frame.config(height=self.height-25, width=self.width)
        filterJobsOptions_frame.grid(row=0, columnspan=12, rowspan=10, padx=5, pady=5, sticky=W + E + N + S)

        Label(filterJobsOptions_frame, text='Case sensitive?',anchor=W, width=20).grid(row=0, column=0)
        Label(filterJobsOptions_frame, text='And?',anchor=W, width=20).grid(row=1, column=0)

        #case sensitive check button
        self.case_sensitive_option = BooleanVar(filterJobsOptions_frame)
        self.case_sensitive_option.set(self.filterOptions['Casesensitive'])
        self.case_sensitive_checkbutton = Checkbutton(filterJobsOptions_frame,variable=self.case_sensitive_option)
        self.case_sensitive_checkbutton.config(width=15)
        self.case_sensitive_checkbutton.grid(row=0, column=1, sticky=W)

        #and check button
        self.and_option = BooleanVar(filterJobsOptions_frame)
        self.and_option.set(self.filterOptions['And'])
        self.and_checkbutton = Checkbutton(filterJobsOptions_frame, variable=self.and_option)
        self.and_checkbutton.config(width=15)
        self.and_checkbutton.grid(row=1, column=1, sticky=W)

    def createOKAndCancelButtons(self):
        okAndCancelButtons_frame = Frame(self.root)
        okAndCancelButtons_frame.config(width= self.width)
        okAndCancelButtons_frame.grid(row=10, column=0, columnspan=2, sticky=W + E + N + S)
        self.okButton = Button(okAndCancelButtons_frame, command=self.saveFilterOptions, text='OK', width=10)
        self.okButton.grid(row=0, column=0, padx=5, pady=2, sticky=E)
        self.cancelButton = Button(okAndCancelButtons_frame, command= lambda: self.guiController.closeWindow(self), text='Cancel', width=10)
        self.cancelButton.grid(row=0, column=1, padx=5, pady=2, sticky=E)

    def enable(self, enable):
        self.root.attributes('-disabled', not enable)

    def close(self):
        print('Exiting...')
        self.guiController.closeWindow(self)

    def saveFilterOptions(self):
        print('Applying filter options...')
        filterOptions = {}
        filterOptions['Casesensitive'] = self.case_sensitive_option.get()
        filterOptions['And'] = self.and_option.get()
        self.guiController.saveFilterOptions(filterOptions)
        self.close()

    def show(self):
        self.enable(True)
        self.root.focus_force()
        self.root.mainloop()