"""

Creating a  window class GUI for entering the data of a new laser job

David SAnchez Sanchez


"""
import tkinter
from tkinter import *
from tkinter import ttk
from datetime import date

class NewJobWindow():

    # pixels of the window
    width = 600
    height = 300

    def __init__(self, guiController):
        self.guiController = guiController
        self.root = tkinter.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.root.title('Laser-Jobs Manager. New Job Window.')
        self.root.iconbitmap('../icons/laserJobsManager_Icon5.ico')

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.root.winfo_screenwidth() / 2 - self.width / 2)
        positionDown = int(self.root.winfo_screenheight() / 2 - self.height / 2)

        self.root.geometry(str(self.width) + 'x' + str(self.height) + "+" +str(positionRight) + "+" + str(positionDown))
        self.root.resizable(0, 0)
        self.createLabelsAndEntries()
        self.createOKAndCancelButtons()

    def createLabelsAndEntries(self):

        newJobData_frame = Frame(self.root)
        newJobData_frame.config(height=self.height-25, width=self.width)
        newJobData_frame.grid(row=0, columnspan=12, rowspan=10, padx=5, pady=5, sticky=W + E + N + S)

        Label(newJobData_frame, text='Username:',anchor=W, width=20).grid(row=0, column=0)
        Label(newJobData_frame, text='Date:',anchor=W, width=20).grid(row=1, column=0)
        Label(newJobData_frame, text='Material:',anchor=W, width=20).grid(row=2, column=0)
        Label(newJobData_frame, text='Cut/Raster:',anchor=W, width=20).grid(row=3, column=0)
        Label(newJobData_frame, text='Power(%):', anchor=W, width=20).grid(row=4, column=0)
        Label(newJobData_frame, text='DPI:', anchor=W, width=20).grid(row=5, column=0)
        Label(newJobData_frame, text='Freq(Hz):', anchor=W, width=20).grid(row=6, column=0)
        Label(newJobData_frame, text='#Passes (Cut/Raster):', anchor=W, width=20).grid(row=7, column=0)
        Label(newJobData_frame, text='RasterDepth(mm):', anchor=W, width=20).grid(row=8, column=0)
        Label(newJobData_frame, text='Others:', anchor=W, width=20).grid(row=9, column=0)

        #Username entry
        self.username = StringVar(newJobData_frame)
        self.username_entry = Entry(newJobData_frame,textvariable=self.username)
        self.username_entry.config(width=15)
        self.username_entry.grid(row=0, column=1, sticky=W)

        #Date entry
        self.date = StringVar(newJobData_frame)
        self.date_entry = Entry(newJobData_frame,textvariable=self.date)
        self.date_entry.config(width=15)
        self.date_entry.insert(0,date.today())
        self.date_entry.config(state='disabled')
        self.date_entry.grid(row=1,column=1,sticky=W)

        #Material Entry
        self.material = StringVar(newJobData_frame)
        self.material_entry = Entry(newJobData_frame, textvariable=self.material)
        self.material_entry.config(width=15)
        self.material_entry.grid(row=2, column=1, sticky=W)

        #Dropdown list for job type
        self.jobType = StringVar(newJobData_frame)
        choices = ('Cut', 'Raster', 'Cut/Raster')
        self.jobType.set(choices[0])  # default value
        JobTypeMenu = OptionMenu(newJobData_frame, self.jobType, *choices)
        JobTypeMenu.config(width=8, anchor=W)
        JobTypeMenu.grid(row=3, column=1, sticky=W)

        #Power Entry
        self.power = IntVar(newJobData_frame,90)
        self.power_entry = Entry(newJobData_frame, textvariable=self.power)
        self.power_entry.config(width=15)
        self.power_entry.grid(row=4, column=1, sticky=W)

        #dpi entry (dots per icnh)
        self.dpi = IntVar(newJobData_frame, 900)
        self.dpi_entry = Entry(newJobData_frame, textvariable=self.dpi)
        self.dpi_entry.config(width=15)
        self.dpi_entry.grid(row=5, column=1, sticky=W)

        # Frequency entry (in Hz)
        self.freq = IntVar(newJobData_frame, 5000)
        self.freq_entry = Entry(newJobData_frame, textvariable=self.freq)
        self.freq_entry.config(width=15)
        self.freq_entry.grid(row=6, column=1, sticky=W)

        # Number of passes entry
        self.nPasses = StringVar(newJobData_frame, '1/0')
        self.nPasses_entry = Entry(newJobData_frame, textvariable=self.nPasses)
        self.nPasses_entry.config(width=15)
        self.nPasses_entry.grid(row=7, column=1, sticky=W)

        # Raster depth entry (in mm)
        self.rasterDepth = IntVar(newJobData_frame, 1)
        self.rasterDepth_entry = Entry(newJobData_frame, textvariable=self.rasterDepth)
        self.rasterDepth_entry.config(width=15)
        self.rasterDepth_entry.grid(row=8, column=1, sticky=W)

        # Observations entry
        self.observations = StringVar(newJobData_frame, 'Enter here useful comments for the future')
        self.observations_entry = Entry(newJobData_frame, textvariable=self.observations)
        self.observations_entry.bind('<FocusIn>',lambda event: self.observations_entry.delete(0,END))
        self.observations_entry.config(width=60)
        self.observations_entry.grid(row=9, column=1, sticky=W)

    def createOKAndCancelButtons(self):
        okAndCancelButtons_frame = Frame(self.root)
        okAndCancelButtons_frame.config(width= self.width)
        okAndCancelButtons_frame.grid(row=10, column=0, columnspan=2, sticky=W + E + N + S)
        self.okButton = Button(okAndCancelButtons_frame, command=self.guiController.addJob, text='Add Register', width=10)
        self.okButton.grid(row=0, column=0, padx=5, pady=2, sticky=E)
        self.cancelButton = Button(okAndCancelButtons_frame, command=self.guiController.cancelAddJob, text='Cancel', width=10)
        self.cancelButton.grid(row=0, column=1, padx=5, pady=2, sticky=E)

    def close(self):
        print('Exiting...')
        self.guiController.closeWindow(self.root)

    def cancel(self):
        print('Adding new job...')

    def ok(self):
        print('Deleting existing job...')

    def show(self):
        self.root.mainloop()