"""

Creating a main window class GUI manage the Laser Jobs

David SAnchez Sanchez


"""
import tkinter
from tkinter import *
from tkinter import ttk

class MainWindow():

    #pixels
    width = 1200
    height = 600

    def __init__(self, guiController):
        self.guiController = guiController
        self.root = tkinter.Tk(className='MainWindow') # we need this for identifying the
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.title('Laser-Jobs Manager. Main Window.')
        self.root.iconbitmap('../icons/laserJobsManager_Icon5.ico')

        # Gets both half the screen width/height and window width/height
        positionRight = int(self.root.winfo_screenwidth() / 2 - self.width / 2)
        positionDown = int(self.root.winfo_screenheight() / 2 - self.height / 2)
        self.root.geometry(str(self.width) + 'x' + str(self.height) + "+" +str(positionRight) + "+" + str(positionDown))

        self.root.resizable(0,0)
        self.create_menu_bar()
        self.create_jobsTable_frame(self.guiController.jobsTableHeaders)
        self.create_tool_bar()
        self.loadJobsData([('0','b','c','d','b','c','d','b','c','d',''),('1','b','c','d'),('2','b','c','d'),('3','b','c','d')])

        self.root.mainloop()

    def create_tool_bar(self):

        tool_bar_frame = Frame(self.root)
        tool_bar_frame.grid(row=1, column=0, columnspan=6,sticky=W+E+N+S)
        addRegisterIcon = PhotoImage(file='../icons/addRegisterIcon_30x30.gif')
        deleteRegisterIcon = PhotoImage(file='../icons/deleteRegisterIcon_30x30.gif')
        self.addRegisterButton = Button(tool_bar_frame, image=addRegisterIcon, command= self.addNewJob)
        self.addRegisterButton.image = addRegisterIcon
        self.addRegisterButton.grid(row=1, column=0,  padx=5,pady=2)
        self.deleteRegisterButton = Button(tool_bar_frame, image=deleteRegisterIcon, command=self.guiController.deleteRegister)
        self.deleteRegisterButton.image = deleteRegisterIcon
        self.deleteRegisterButton.grid(row=1, column=1, padx=5, pady=2)

    def create_menu_bar(self):

        menubar = Menu(self.root)
        self.appMenu = Menu(self.root, tearoff=0)
        self.appMenu.add_command(label="Exit", command=self.close)
        menubar.add_cascade(label="App", menu=self.appMenu)

        self.jobMenu = Menu(self.root, tearoff=0)
        self.jobMenu.add_command(label="New job...", command=self.addNewJob)
        self.jobMenu.add_command(label="Delete job", command=self.deleteJob)
        menubar.add_cascade(label="Job", menu=self.jobMenu)

        self.root.config(menu=menubar)

    def create_jobsTable_frame(self, jobsTableHeaders):

        rowHeight = 20 #pixels
        nRows = 25
        style = ttk.Style(self.root)
        style.configure('Treeview', rowheight=rowHeight) #rowheight in pixels

        self.jobsTableTree = ttk.Treeview(self.root, height=nRows) #height in rows



        self.jobsTableTree.grid(row=0, column=0, columnspan=6, sticky=W + E + N + S)

        jobsTableHeaders_Order = tuple(x[0] for x in jobsTableHeaders)
        jobsTableHeaders_Text = tuple(x[1] for x in jobsTableHeaders)
        jobsTableHeaders_WidthInPercent = tuple(x[2] for x in jobsTableHeaders)

        self.jobsTableTree["columns"] = jobsTableHeaders_Order #creamos las columnas

        #Configuramos el texto del encabezado de cada columna
        for order, text in zip(jobsTableHeaders_Order, jobsTableHeaders_Text):
            self.jobsTableTree.heading(order, text=text, anchor=W)

        #Configuramos la anchura de las columnas
        for order, w in zip(jobsTableHeaders_Order,jobsTableHeaders_WidthInPercent):
            self.jobsTableTree.column(order, width=int((w/100.0) * self.width), minwidth=int((w/100.0) * self.width), stretch=True)

        #Adding scroll bars
        ysb = Scrollbar(self.root, orient=VERTICAL, command=self.jobsTableTree.yview)
        ysb.grid(row=0, column=0, sticky='ns')
        ysb.place(x=self.width-20,y=20, height=nRows*rowHeight, width=20) #number of rows x rowheight
        self.jobsTableTree.configure(yscroll=ysb.set)

        xsb = Scrollbar(self.root, orient=HORIZONTAL, command=self.jobsTableTree.xview)
        xsb.grid(row=0, column=0, sticky='we')
        xsb.place(x=1, y=nRows*rowHeight, height=20, width=self.width-20)  # number of rows x rowheight
        self.jobsTableTree.configure(xscroll=xsb.set)

    def loadJobsData(self, values):
        for value in values:
            self.jobsTableTree.insert("", 'end', text="ID"+str(value[0]), values=value[1:])

    def close(self):
        print('Exiting...')
        self.guiController.closeWindow(self)

    def addNewJob(self):
        self.guiController.showNewJobWindow()

    def deleteJob(self):
        print('Deleting existing job...')