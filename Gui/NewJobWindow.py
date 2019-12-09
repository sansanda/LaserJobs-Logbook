"""

Creating a  window class GUI for entering the data of a new laser job

David SAnchez Sanchez


"""
import tkinter
from tkinter import *
from tkinter import ttk
from datetime import date

class NewJobWindow():

    # pixels
    width = 600
    height = 300

    def __init__(self, guiController):
        self.guiController = guiController
        self.root = tkinter.Tk()
        self.root.title('Laser-Jobs Manager. New Job Window.')
        self.root.iconbitmap('../icons/laserJobsManager_Icon5.ico')
        self.root.geometry(str(self.width) + 'x' + str(self.height))
        self.root.resizable(0, 0)
        self.createLabelsAndEntries()
        self.createOKAndCancelButtons()
        self.populate(
            [('0', 'b', 'c', 'd', 'b', 'c', 'd', 'b', 'c', 'd', ''), ('1', 'b', 'c', 'd'), ('2', 'b', 'c', 'd'),
             ('3', 'b', 'c', 'd')])
        self.root.mainloop()

    def createLabelsAndEntries(self):

        newJobData_frame = Frame(self.root)
        newJobData_frame.config(height=self.height-25, width=self.width)
        newJobData_frame.grid(row=0, columnspan=12, rowspan=10, padx=5, pady=5, sticky=W + E + N + S)

        Label(newJobData_frame, text='Username:',anchor=W, width=15).grid(row=0, column=0)
        Label(newJobData_frame, text='Date:',anchor=W, width=15).grid(row=1, column=0)
        Label(newJobData_frame, text='Material:',anchor=W, width=15).grid(row=2, column=0)
        Label(newJobData_frame, text='Cut/Raster:',anchor=W, width=15).grid(row=3, column=0)
        Label(newJobData_frame, text='Power(%):', anchor=W, width=15).grid(row=4, column=0)
        Label(newJobData_frame, text='DPI:', anchor=W, width=15).grid(row=5, column=0)
        Label(newJobData_frame, text='Freq(Hz):', anchor=W, width=15).grid(row=6, column=0)
        Label(newJobData_frame, text='#Passes:', anchor=W, width=15).grid(row=7, column=0)
        Label(newJobData_frame, text='RasterDepth(mm):', anchor=W, width=15).grid(row=8, column=0)
        Label(newJobData_frame, text='Others:', anchor=W, width=15).grid(row=9, column=0)

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



        # gc.configureMainWindow((('#0', 'jobID', 5),
        #                         ('#1', 'Username', 10),
        #                         ('#2', 'Date', 10),
        #                         ('#3', 'Material', 10),
        #                         ('#4', 'Cut/Raster', 10),
        #                         ('#5', 'Power(%)', 5),
        #                         ('#6', 'DPI', 5),
        #                         ('#7', 'Freq(Hz)', 5),
        #                         ('#8', '#Passes', 5),
        #                         ('#9', 'RasterDepth(mm)', 10),
        #                         ('#10', 'Others', 25))


        pass

    def createOKAndCancelButtons(self):
        okAndCancelButtons_frame = Frame(self.root)
        okAndCancelButtons_frame.config(width= self.width)
        okAndCancelButtons_frame.grid(row=10, column=0, columnspan=2, sticky=W + E + N + S)
        self.okButton = Button(okAndCancelButtons_frame, command=self.guiController.addRegister, text='Add Register', width=10)
        self.okButton.grid(row=0, column=0, padx=5, pady=2, sticky=E)
        self.cancelButton = Button(okAndCancelButtons_frame, command=self.guiController.cancelAddRegister, text='Cancel', width=10)
        self.cancelButton.grid(row=0, column=1, padx=5, pady=2, sticky=E)

    def populate(self, values):
        pass
        # for value in values:
        #     self.jobsTableTree.insert("", 'end', text="ID" + str(value[0]), values=value[1:])

    def onExit(self):
        print('Exiting...')

    def cancel(self):
        print('Adding new job...')

    def ok(self):
        print('Deleting existing job...')