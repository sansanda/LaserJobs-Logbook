"""

Creating a main window class GUI manage the Laser Jobs

David SAnchez Sanchez


"""
import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from Logic.LaserJobs_Book import LaserJobs_Book


class MainWindow():

    def __init__(self, w_scale, h_scale):

        self.root = tkinter.Tk(className='MainWindow')  # we need this for identifying the
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.title('Laser-Jobs Manager. Main Window. v1.0')
        self.root.iconbitmap('../Gui/icons/laserJobsManager_Icon5.ico')

        self.width = int(self.root.winfo_screenwidth() * w_scale)
        self.height = int(self.root.winfo_screenheight() * h_scale)


        # Gets both half the screen width/height and window width/height
        positionRight = int(self.width*(1-w_scale))
        positionDown = int(self.height*(1-h_scale))
        self.root.geometry(
            str(self.width) + 'x' + str(self.height) + "+" + str(positionRight) + "+" + str(positionDown)
        )

        self.state = NORMAL

        # self.root.resizable(0,0)

    def setGuiController(self, guiController):
        self.guiController = guiController

    def populate(self, jobsTableHeaders):
        self.create_menu_bar()
        self.create_filter_bar()
        self.create_jobsTable_frame(jobsTableHeaders)
        self.create_tool_bar()
        self.create_contextual_menu()
        self.create_Command_Shortcuts()

    def create_filter_bar(self):

        self.filter_bar_frame = Frame(self.root)
        self.filter_bar_frame.grid(row=0, column=0, columnspan=6, sticky=W + E + N + S)
        Label(self.filter_bar_frame, text='Filter:', anchor=W, width=20, padx=10, pady=10).grid(row=0, column=0)

        # Filter text entry
        self.filterText = StringVar(self.filter_bar_frame)
        self.filterText.trace("w", lambda name, index, mode, sv=self.filterText: self.filterTreeView(self.filterText))

        self.filter_entry = Entry(self.filter_bar_frame, textvariable=self.filterText)
        self.filter_entry.config(width=30)
        self.filter_entry.grid(row=0, column=1, sticky=W)

    def create_contextual_menu(self):
        # TODO: Create contextual menu. Edit and delete job
        self.popup_menu = Menu(self.root, tearoff=0)
        self.popup_menu.add_command(label="Delete job", command=self.deleteJob)
        self.popup_menu.add_command(label="Edit job...", command=self.editJob, state='disable')

        self.root.bind("<Button-3>", self.showPopupMenu)  # Button-2 on Aqua

    def showPopupMenu(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def create_tool_bar(self):

        self.tool_bar_frame = Frame(self.root)
        self.tool_bar_frame.grid(row=2, column=0, columnspan=6, sticky=W + E + N + S)
        addRegisterIcon = PhotoImage(file='../Gui/icons/addRegisterIcon_30x30.gif')
        deleteRegisterIcon = PhotoImage(file='../Gui/icons/deleteRegisterIcon_30x30.gif')
        self.addNewJobButton = Button(self.tool_bar_frame, image=addRegisterIcon,
                                      command=self.guiController.showNewJobWindow)
        self.addNewJobButton.image = addRegisterIcon
        self.addNewJobButton.grid(row=1, column=0, padx=5, pady=2)
        self.deleteJobButton = Button(self.tool_bar_frame, image=deleteRegisterIcon, command=self.deleteJob)
        self.deleteJobButton.image = deleteRegisterIcon
        self.deleteJobButton.grid(row=1, column=1, padx=5, pady=2)

    def create_Command_Shortcuts(self):
        # create command shortcuts
        self.root.bind('<Delete>', lambda e: self.deleteJob())
        self.root.bind('<Insert>', lambda e: self.guiController.showNewJobWindow())

    def create_menu_bar(self):

        self.menubar = Menu(self.root)

        self.fileMenu = Menu(self.root, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.close)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)

        self.jobMenu = Menu(self.root, tearoff=0)
        self.jobMenu.add_command(label="New job...", command=self.guiController.showNewJobWindow)
        self.jobMenu.add_command(label="Delete job", command=self.deleteJob)
        self.jobMenu.add_command(label="Edit job...", command=self.editJob, state='disable')
        self.menubar.add_cascade(label="Job", menu=self.jobMenu)

        self.filterMenu = Menu(self.root, tearoff=0)
        self.filterMenu.add_command(label="Filter Jobs Options", command=self.guiController.showFilterJobsOptionsWindow)
        self.menubar.add_cascade(label="View", menu=self.filterMenu)

        self.root.config(menu=self.menubar)

    def create_jobsTable_frame(self, jobsTableHeaders):

        rowHeight = 20  # pixels
        nRows = 25
        style = ttk.Style(self.root)

        style.configure('Treeview', rowheight=rowHeight)  # rowheight in pixels
        self.jobsTableTree = ttk.Treeview(self.root, height=nRows)  # height in rows
        self.jobsTableTree.configure(selectmode="browse")  # configure the tree view for only select one row at time
        self.jobsTableTree.grid(row=1, column=0, columnspan=6, sticky=W + E + N + S)

        jobsTableHeaders_Order = tuple(x[0] for x in jobsTableHeaders)
        jobsTableHeaders_Text = tuple(x[1] for x in jobsTableHeaders)
        jobsTableHeaders_WidthInPercent = tuple(x[2] for x in jobsTableHeaders)

        self.jobsTableTree["columns"] = jobsTableHeaders_Order  # creamos las columnas

        # Configuramos el texto del encabezado de cada columna
        for order, text in zip(jobsTableHeaders_Order, jobsTableHeaders_Text):
            self.jobsTableTree.heading(order, text=text, anchor=W)

        # Configuramos la anchura de las columnas
        for order, w in zip(jobsTableHeaders_Order, jobsTableHeaders_WidthInPercent):
            self.jobsTableTree.column(order, width=int((w / 100.0) * self.width),
                                      minwidth=int((w / 100.0) * self.width), stretch=True)

        # Adding scroll bars
        ysb = Scrollbar(self.root, orient=VERTICAL, command=self.jobsTableTree.yview)
        ysb.grid(row=0, column=0, sticky='ns')
        ysb.place(x=self.width - 20, y=20, height=nRows * rowHeight, width=20)  # number of rows x rowheight
        self.jobsTableTree.configure(yscroll=ysb.set)

        self.detached_children = {}

    # jobs is a list of dictionaries
    # each jobData is a dictionary

    def loadJobsData(self, jobs):
        for jobData in jobs:
            jobDataAsList = LaserJobs_Book.getJobDataAsList(jobData)
            self.jobsTableTree.insert("", 'end', text=str(jobDataAsList[0]), values=jobDataAsList[1:])
        self.detached_children = {}
        self.filterTreeView(self.filterText)

    def deleteJob(self):
        selectedJob = self.jobsTableTree.selection()
        if len(selectedJob) == 0:
            messagebox.showerror("No job have been selected!!!!!",
                                 "Please, first select the job you want to delete!!!!!")
        else:
            selectedJob_jobId = self.jobsTableTree.item(selectedJob, 'text')
            self.guiController.deleteJob(selectedJob_jobId)

    def editJob(self):
        selectedJob = self.jobsTableTree.selection()
        if len(selectedJob) == 0:
            messagebox.showerror("No job have been selected!!!!!",
                                 "Please, first select the job you want to delete!!!!!")
        else:
            selectedJob_jobId = self.jobsTableTree.item(selectedJob, 'text')
            self.guiController.editJob(selectedJob_jobId)

    def close(self):
        print('Exiting...')
        self.guiController.closeWindow(self)

    def enable(self, enable):
        self.root.attributes('-disabled', not enable)

    def show(self):
        self.enable(True)
        self.root.mainloop()

    def filterTreeView(self, filterText):
        # TODO: implements filtering of the tree view (at level of LaserJobs_Book)
        # The idea is to use two data structures one for the filter matching jobs and the other for the not filter matching jobs

        caseSensitive_Option = self.guiController.logicController.filterOptions['Casesensitive']
        and_Option = self.guiController.logicController.filterOptions['And']

        filterTextCS = filterText.get()
        if not caseSensitive_Option:
            filterTextCS = str.upper(filterText.get())

        #reatach
        for child_id in list(self.detached_children.keys()): #avoid the dictionary changed size during iteration error
            for value in self.detached_children[child_id]:

                if filterText.get() in str(value):
                    #TODO: reorder the list does not work very well
                    self.jobsTableTree.reattach(child_id,'',int(child_id[1:],16)-1) #reattach in the same original position
                    del self.detached_children[child_id]
                    break

        #detach
        for child_id in self.jobsTableTree.get_children():
            matched = False
            child_values = self.jobsTableTree.item(child_id)['values']
            for value in child_values:
                valueCS = str(value)
                if not caseSensitive_Option:
                    valueCS = str.upper(str(value))

                if filterTextCS in valueCS:
                    matched = True
                    break

            if not matched:
                self.detached_children[child_id] = child_values
                self.jobsTableTree.detach(child_id)


    # part of the Observer design pattern implementation
    # values could be a list of dicts which contains updated jobs data
    def notify(self, values):

        if isinstance(values, list):
            # first clear the treeview
            self.jobsTableTree.delete(*self.jobsTableTree.get_children())
            # after reload the data
            self.loadJobsData(values)