import os
import tkinter
import ProgramMain
import tkinter.filedialog
from tkdnd_wrapper import TkDND


######################################################################################
#   The MainFrame is the block that holds all other GUI elements in the standard     #
#   program. add "self.windowAddRow()" lines to __init__ to increase the amount      #
#   of default fileinput rows that appear upon launch                                #
######################################################################################
class MainFrame(tkinter.Frame):

    def selectFile(self, obj):
        tkinter.Tk().withdraw()
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
        self.fileinput.selectedfilename.set(self.fileinput.fileinputresetmessage)
        self.templateinput.selectedfilename.set("")
        self.inputlist = []

    def handleTemplateInput(self, event):
        rawfilelist = event.data
        filelist = self.tcl.tk.splitlist(rawfilelist)
        ## IF THERE ARE MULTIPLE FILES OR THE OBJECT IS NOT A FILE, SEND INVALID ##
        if len(filelist)>1 or not(os.path.isfile(filelist[0])):
            self.templateinput.selectedfilename.set("INVALID INPUT. Only select one file.")
        else:
            self.templateinput.selectedfilename.set(filelist[0])

    def handleFileInput(self, event):
        rawfilelist = self.tcl.tk.splitlist(event.data)
        newfilelist = list(rawfilelist)
        newfilelist.sort()
        ## Sorted new data. Check for existing data ##
        if len(self.inputlist)>0:
            for item in newfilelist:
                if not item in self.inputlist:
                    self.inputlist.append(item)
            self.inputlist.sort()
        else:
            self.inputlist = newfilelist
        filenames = []
        for i, rawfilename in enumerate(self.inputlist):
            filename = os.path.basename(rawfilename)
            filenames.append("File "+str(i+1)+": "+filename)
        self.fileinput.selectedfilename.set("\n".join(filenames))

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.rows = 0
        #self.inputrowcount = 0
        self.inputlist = []

        self.tcl = tkinter.Tcl()
        self.infoblock = InfoBlock(self)
        self.templateinput = TemplateInput(self)
        self.fileinputheader = FileInputHeader(self)
        self.fileinput = FileInput(self)
        #self.windowAddRow()
        #self.windowAddRow()
        #self.windowAddRow()
        self.grid(padx=4, pady=5)

        dnd = TkDND(self.fileinput)
        dnd.bindtarget(self.fileinput.inputbox, self.handleFileInput, 'text/uri-list')
        dnd.bindtarget(self.templateinput.selectedtemplate, self.handleTemplateInput, 'text/uri-list')


######################################################################################
#    This InfoBlock appears at the top of the screen. Do not add more.               #
######################################################################################
class InfoBlock(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        rownum = parent.rows
        self.parent = parent

        self.infoblocktext = """Created by Bodin Punyaprateep
Designed for Caang @ JD

This app will only accept .txt files as input and will create a new excel file as output. The format of the .txt files is listed under the "Help" button."""

        self.infoblock = tkinter.Label(parent, text = self.infoblocktext, wraplength = 450)
        self.infoblock.grid(row=rownum, rowspan = 4, column=2, columnspan=3, sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        self.confirmfiles = tkinter.Button(parent, text = "Run Program", command=lambda: ProgramMain.programStart(self))
        self.confirmfiles.grid(row=rownum, column = 5, columnspan=2, sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W,)
        rownum += 1

        self.helpbutton = tkinter.Button(parent, text = "Show Help", command=lambda: parent.parent.changeFrame("HELP"))
        self.helpbutton.grid(row=rownum, column = 5, columnspan=2, sticky = tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        rownum +=3
        parent.rows = rownum


######################################################################################
#   This TemplateInput block is required. Do not add more.                           #
######################################################################################
class TemplateInput(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.selectedfilename = tkinter.StringVar()
        rownum = parent.rows

        self.spacer = tkinter.Canvas(parent, height = 30)
        self.spacer.grid(row=rownum, columnspan = 8, sticky = tkinter.W + tkinter.E)
        self.spacer.create_line(0, 26, 2000, 26, fill = "gray75")
        self.spacer.create_line(0, 29, 2000, 29, fill = "gray75")
        rownum += 1

        self.templateinfo = tkinter.Label(parent, text = "Select the template file. (REQUIRED)")
        self.templateinfo.grid(row=rownum, column=2, columnspan=3, sticky = tkinter.W)
        rownum += 1

        self.templatelabel = tkinter.Label(parent, text= "Template:")
        self.templatelabel.grid(row=rownum, column=0, columnspan=2, sticky = tkinter.W + tkinter.E)

        self.selectedtemplate = tkinter.Entry(parent, textvariable=self.selectedfilename, width=50)
        self.selectedtemplate.grid(row=rownum, column=2, columnspan = 3, sticky= tkinter.W + tkinter.E)

        self.templatebrowse = tkinter.Button(parent, text = "Browse files", command=lambda: parent.selectFile(self))
        self.templatebrowse.grid(row=rownum, column=5, columnspan = 2, sticky = tkinter.W + tkinter.E, padx = 5, ipadx = 4)
        rownum += 1

        self.spacer = tkinter.Canvas(parent, height = 20)
        self.spacer.grid(row=rownum, columnspan = 8, sticky = tkinter.W + tkinter.E)
        self.spacer.create_line(0, 16, 2000, 16, fill = "gray75")
        self.spacer.create_line(0, 19, 2000, 19, fill = "gray75")

        rownum += 1
        parent.rows = rownum


######################################################################################
#   FileInputHeader exists above the individual file input rows. Do not add more.    #
######################################################################################
class FileInputHeader(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        rownum = parent.rows
        self.fileheadertext = '''Drag and drop your files into both input boxes. (REQUIRED)'''

        self.fileheaderinfo = tkinter.Label(parent, text=self.fileheadertext)
        self.fileheaderinfo.grid(row=rownum, column=2, columnspan=3, sticky = tkinter.W, pady=0)
        #rownum += 1

        #self.rowincrease = tkinter.Button(parent, text = "Add New Field", command=lambda: parent.windowAddRow())
        #self.rowincrease.grid(row=rownum, column = 2, sticky = tkinter.W + tkinter.E, padx=10)

        #self.rowremove = tkinter.Button(parent, text = "Remove Last Field", command=lambda: parent.windowRemoveRow())
        #self.rowremove.grid(row=rownum, column = 3, sticky = tkinter.W + tkinter.E, padx=10)

        self.clearinputs = tkinter.Button(parent, text = "Reset filenames", command=lambda: parent.clearInputs())
        self.clearinputs.grid(row=rownum, column=5, columnspan=2, sticky = tkinter.W + tkinter.E, padx=5, ipadx=4)

        rownum += 1
        parent.rows = rownum


######################################################################################
#   The FileInput rows are added by calling windowAddRow() on the MainFrame object   #
#   The function allows for an unlimited amount of rows to be added. Do not add      #
#   rows by directly declaring new objects. Let the function do its work.            #
######################################################################################
class FileInput(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.selectedfilename = tkinter.StringVar()
        self.fileinputresetmessage = '''Drag and drop your log files in this box. They will appear like this:
File 1: ExampleLogABC.txt
File 2: ExampleLogDEF.txt
...
File 9: ExampleLogXYZ.txt'''
        self.selectedfilename.set(self.fileinputresetmessage)
        ##self.labelnum = str(parent.inputrowcount)
        ##if len(self.labelnum) < 2:
        ##    self.labelnum = "0" + self.labelnum

        rownum = parent.rows
        ##rowcount = parent.inputrowcount

        ##self.inputlabel = tkinter.Label(parent, text="File " + self.labelnum + ":")
        ##self.inputlabel.grid(row=rownum, column=0, columnspan=2)

        self.inputbox = tkinter.Message(parent, textvariable=self.selectedfilename, width=500, background="grey20", foreground="white", relief="sunken", anchor=tkinter.NW)
        self.inputbox.rowconfigure(0, weight=1)
        self.inputbox.grid(row=rownum, column=0, columnspan=7, sticky= tkinter.N + tkinter.S+ tkinter.W + tkinter.E, pady=5)

        ##self.inputbrowse = tkinter.Button(parent, text = "Browse", command=lambda: parent.selectFile(self))
        ##self.inputbrowse.grid(row=rownum, column = 5, columnspan=2, sticky = tkinter.W + tkinter.E, padx = 5, ipadx = 4)

        ##parent.inputlist.append(self)


######################################################################################
