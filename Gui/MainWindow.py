"""

Creating a main window class GUI manage the Laser Jobs

David SAnchez Sanchez


"""
import tkinter
from tkinter import *
from tkinter import ttk

class MainWindow():

    width = 1200
    height = 600
    def __init__(self, guiController):
        self.guiController = guiController
        self.root = tkinter.Tk()
        self.root.title('Laser-Jobs Manager. Main Window.')
        self.root.iconbitmap('../icons/laserJobsManager_Icon5.ico')
        self.root.geometry(str(self.width)+'x'+str(self.height))
        self.root.resizable(0,0)
        self.create_menu_bar()
        self.create_jobsTable_frame()
        self.create_tool_bar()
        self.loadJobsData([('a','b','c','d'),('a','b','c','d'),('a','b','c','d'),('a','b','c','d')])

        self.root.mainloop()

    def create_tool_bar(self):

        tool_bar_frame = Frame(self.root)
        tool_bar_frame.grid(row=10, column=0, columnspan=6,sticky=W+E+N+S)
        addRegisterIcon = PhotoImage(file='../icons/addRegisterIcon_30x30.gif')
        deleteRegisterIcon = PhotoImage(file='../icons/deleteRegisterIcon_30x30.gif')
        self.addRegisterButton = Button(tool_bar_frame, image=addRegisterIcon, command= self.guiController.addRegister)
        self.addRegisterButton.image = addRegisterIcon
        self.addRegisterButton.grid(row=1, column=0,  padx=5,pady=2)
        self.deleteRegisterButton = Button(tool_bar_frame, image=deleteRegisterIcon, command=self.guiController.deleteRegister)
        self.deleteRegisterButton.image = deleteRegisterIcon
        self.deleteRegisterButton.grid(row=1, column=1, padx=5, pady=2)

    def create_menu_bar(self):

        menubar = Menu(self.root)
        self.fileMenu = Menu(self.root, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=self.fileMenu)
        self.root.config(menu=menubar)

    def create_jobsTable_frame(self):

        self.jobsTableTree = ttk.Treeview(self.root)
        self.jobsTableTree.grid(row=0, column=0, columnspan=6, sticky=W + E + N + S)

        ysb = Scrollbar(self.root, orient='vertical', command=self.jobsTableTree.yview)
        ysb.grid(row=0, column=20, sticky='ns')
        self.jobsTableTree.configure(yscroll=ysb.set)

        self.jobsTableTree["columns"] = ("one", "two", "three")

        self.jobsTableTree.column("#0", width=int(0.1*self.width), minwidth=int(0.1*self.width), stretch=NO)
        self.jobsTableTree.column("one", width=int(0.3*self.width), minwidth=int(0.3*self.width), stretch=NO)
        self.jobsTableTree.column("two", width=int(0.3*self.width), minwidth=int(0.3*self.width))
        self.jobsTableTree.column("three", width=int(0.3*self.width), minwidth=int(0.3*self.width), stretch=NO)

        self.jobsTableTree.heading("#0", text="Name", anchor=W)
        self.jobsTableTree.heading("one", text="Date modified", anchor=W)
        self.jobsTableTree.heading("two", text="Type", anchor=W)
        self.jobsTableTree.heading("three", text="Size", anchor=W)


    def loadJobsData(self, values):
        for value in values:
            self.jobsTableTree.insert("", 'end', text="Elemento "+str(value[0]), values=value[1:])

    def onExit(self):
        pass