import tkinter as tk
import ProgramMain
import tkinter.filedialog
from tkdnd_wrapper import TkDND


######################################################################################
#   The MainFrame is the block that holds all other GUI elements in the standard     #
#   program. add "self.windowAddRow()" lines to __init__ to increase the amount      #
#   of default fileinput rows that appear upon launch                                #
######################################################################################
class MainFrame(tk.Frame):

    def selectFile(self, obj):
        tk.Tk().withdraw()
        newfile = tkinter.filedialog.askopenfilename(title = "Select a .txt file")
        obj.selectedfilename.set(newfile)

    #def windowAddRow(self):
    #    self.rows += 1
    #    self.inputrowcount += 1
    #    self.fileinput = FileInput(self)

    #def windowRemoveRow(self):
    #    if len(self.inputlist) > 1:
    #        todelete = self.inputlist[-1]
    #        todelete.inputfile.destroy()
    #        todelete.inputlabel.destroy()
    #        todelete.inputbrowse.destroy()
    #        self.rows -= 1
    #        del self.inputlist[-1]

    def clearInputs(self):
        self.fileinput.selectedfilenames.set("Your files will show up here.")
        self.inputlist = []

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.rows = 0
        self.inputrowcount = 0
        self.inputlist = []

        self.infoblock = InfoBlock(self)
        self.templateinput = TemplateInput(self)
        self.fileinputheader = FileInputHeader(self)
        self.fileinput = FileInput(self)
        #self.windowAddRow()
        #self.windowAddRow()
        #self.windowAddRow()
        self.grid(padx=4, pady=5)





######################################################################################
#    This InfoBlock appears at the top of the screen. Do not add more.               #
######################################################################################
class InfoBlock(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        rownum = parent.rows
        self.parent = parent

        self.infoblocktext = """Created by Bodin Punyaprateep
Designed for Caang @ JD

This app will only accept .txt files as input and will create a new excel file as output. The format of the .txt files is listed under the "Help" button."""

        self.infoblock = tk.Label(parent, text = self.infoblocktext, wraplength = 450)
        self.infoblock.grid(row=rownum, rowspan = 4, column=2, columnspan=3, sticky = tk.N + tk.E + tk.S + tk.W)

        self.confirmfiles = tk.Button(parent, text = "Run Program", command=lambda: ProgramMain.programStart(self))
        self.confirmfiles.grid(row=rownum, column = 5, columnspan=2, sticky = tk.N + tk.E + tk.S + tk.W,)
        rownum += 1

        self.helpbutton = tk.Button(parent, text = "Show Help", command=lambda: parent.parent.changeFrame("HELP"))
        self.helpbutton.grid(row=rownum, column = 5, columnspan=2, sticky = tk.N + tk.E + tk.S + tk.W)

        rownum +=3
        parent.rows = rownum


######################################################################################
#   This TemplateInput block is required. Do not add more.                           #
######################################################################################
class TemplateInput(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.selectedfilename = tk.StringVar()
        rownum = parent.rows

        self.spacer = tk.Canvas(parent, height = 30)
        self.spacer.grid(row=rownum, columnspan = 8, sticky = tk.W + tk.E)
        self.spacer.create_line(0, 26, 2000, 26, fill = "gray75")
        self.spacer.create_line(0, 29, 2000, 29, fill = "gray75")
        rownum += 1

        self.templateinfo = tk.Label(parent, text = "Select the template file. (REQUIRED)")
        self.templateinfo.grid(row=rownum, column=2, columnspan=3, sticky = tk.W)
        rownum += 1

        self.templatelabel = tk.Label(parent, text= "Template:")
        self.templatelabel.grid(row=rownum, column=0, columnspan=2, sticky = tk.W + tk.E)

        self.selectedtemplate = tk.Entry(parent, textvariable=self.selectedfilename, width=50)
        self.selectedtemplate.grid(row=rownum, column=2, columnspan = 3, sticky= tk.W + tk.E)

        self.templatebrowse = tk.Button(parent, text = "Browse", command=lambda: parent.selectFile(self))
        self.templatebrowse.grid(row=rownum, column=5, columnspan = 2, sticky = tk.W + tk.E, padx = 5, ipadx = 4)
        rownum += 1

        self.spacer = tk.Canvas(parent, height = 20)
        self.spacer.grid(row=rownum, columnspan = 8, sticky = tk.W + tk.E)
        self.spacer.create_line(0, 16, 2000, 16, fill = "gray75")
        self.spacer.create_line(0, 19, 2000, 19, fill = "gray75")

        rownum += 1
        parent.rows = rownum


######################################################################################
#   FileInputHeader exists above the individual file input rows. Do not add more.    #
######################################################################################
class FileInputHeader(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        rownum = parent.rows

        self.fileheaderinfo = tk.Label(parent, text = "Drag and drop all log files into the black box below.")
        self.fileheaderinfo.grid(row=rownum, column=2, columnspan=3, sticky = tk.W, pady=0)
        #rownum += 1

        #self.rowincrease = tk.Button(parent, text = "Add New Field", command=lambda: parent.windowAddRow())
        #self.rowincrease.grid(row=rownum, column = 2, sticky = tk.W + tk.E, padx=10)

        #self.rowremove = tk.Button(parent, text = "Remove Last Field", command=lambda: parent.windowRemoveRow())
        #self.rowremove.grid(row=rownum, column = 3, sticky = tk.W + tk.E, padx=10)

        self.clearinputs = tk.Button(parent, text = "Clear filenames", command=lambda: parent.clearInputs())
        self.clearinputs.grid(row=rownum, column=5, columnspan=2, sticky = tk.W + tk.E, padx=5, ipadx=4)

        rownum += 1
        parent.rows = rownum


######################################################################################
#   The FileInput rows are added by calling windowAddRow() on the MainFrame object   #
#   The function allows for an unlimited amount of rows to be added. Do not add      #
#   rows by directly declaring new objects. Let the function do its work.            #
######################################################################################
class FileInput(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.selectedfilenames = tk.StringVar()
        self.selectedfilenames.set("Your files will show up here.")
        ##self.labelnum = str(parent.inputrowcount)
        ##if len(self.labelnum) < 2:
        ##    self.labelnum = "0" + self.labelnum

        rownum = parent.rows
        rowcount = parent.inputrowcount

        ##self.inputlabel = tk.Label(parent, text="File " + self.labelnum + ":")
        ##self.inputlabel.grid(row=rownum, column=0, columnspan=2)

        self.inputbox = tk.Message(parent, textvariable=self.selectedfilenames, width=500, background="grey20", foreground="white", relief="sunken", anchor=tkinter.NW)
        self.inputbox.grid(row=rownum, column=0, columnspan=7, sticky= tk.N + tk.S+ tk.W + tk.E, pady=5)

        ##self.inputbrowse = tk.Button(parent, text = "Browse", command=lambda: parent.selectFile(self))
        ##self.inputbrowse.grid(row=rownum, column = 5, columnspan=2, sticky = tk.W + tk.E, padx = 5, ipadx = 4)

        ##parent.inputlist.append(self)


######################################################################################
