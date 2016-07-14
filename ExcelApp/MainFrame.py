import os
import tkinter
import ProgramMain
import tkinter.filedialog
from tkdnd_wrapper import TkDND


###############################################################################
#   The MainFrame is the block that holds all other GUI elements in the       #
#   standard program. A bunch of the functions in this class rely on the      #
#   existence of all of the objects on this page within the MainFrame object. #
#                                                                             #
#   I know that it is a terrible coding approach, but this is my first real   #
#   project ever. I'll fix this in my next application :)                     #
###############################################################################
class MainFrame(tkinter.Frame):

    def selectFile(self, obj):
        # This function is in case the user wants to use the browse button to
        # select their template file. The log files must be click+dragged.

        tkinter.Tk().withdraw()
        newfile = tkinter.filedialog.askopenfilename(title="Select a .txt file")
        obj.selectedfilename.set(newfile)

    def clearInputs(self):
        # Called whenever the "Reset Filenames" button is used.

        self.fileinput.selectedfilename.set(self.fileinput.fileinputresetmessage)
        self.templateinput.selectedfilename.set("")
        self.inputlist = []

    def handleTemplateInput(self, event):
        # This function is called everytime items are dragged onto the template
        # selection box.

        rawfilelist = event.data
        # Use Tcl_SplitList to split the string
        filelist = self.tcl.tk.splitlist(rawfilelist)
        # IF THERE ARE MULTIPLE FILES OR THE OBJECT IS NOT A FILE, SEND INVALID
        if len(filelist) > 1 or not(os.path.isfile(filelist[0])):
            self.templateinput.selectedfilename.set("INVALID INPUT. You must select one file.")
        else:
            self.templateinput.selectedfilename.set(filelist[0])

    def handleFileInput(self, event):
        # This function is called everytime items are dragged onto the black
        # file input box at the bottom of the window.

        rawfilelist = event.data
        # Make into a proper list #
        newfilelist = list(self.tcl.tk.splitlist(rawfilelist))

        # Check to see if the item doesn't already exist in the list and is a
        # file. If both are true, add it to the inputlist array
        for item in newfilelist:
            if item not in self.inputlist and os.path.isfile(item):
                self.inputlist.append(item)

        self.inputlist.sort()

        # filenames is an array that will hold all of the formatted filenames
        # from inputlist.
        filenames = []

        for i, rawfilename in enumerate(self.inputlist):
            # Format the string so it looks nice #
            name = os.path.basename(rawfilename)
            filenames.append("File "+str(i+1)+": "+name)
        # Set the black box to display the formatted input string #
        if len(filenames) > 0:
            self.fileinput.selectedfilename.set("\n".join(filenames))

    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.rows = 0
        self.inputlist = []

        # This is a Tcl interpreter
        self.tcl = tkinter.Tcl()
        self.infoblock = InfoBlock(self)
        self.templateinput = TemplateInput(self)
        self.fileinputheader = FileInputHeader(self)
        self.fileinput = FileInput(self)
        self.grid(padx=4, pady=5)

        # Bind drag and drop events to the proper objects
        dnd = TkDND(self.fileinput)
        dnd.bindtarget(self.fileinput.inputbox, self.handleFileInput, 'text/uri-list')
        dnd.bindtarget(self.templateinput.selectedtemplate, self.handleTemplateInput, 'text/uri-list')


###############################################################################
#    This InfoBlock appears at the top of the screen.                         #
###############################################################################
class InfoBlock(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        rownum = parent.rows
        self.parent = parent

        self.infoblocktext = """Created by Bodin Punyaprateep
Designed for Caang @ JD

This app will only accept .txt files as input and will create a new excel file as output. The format of the .txt files is listed under the "Help" button."""

        self.infoblock = tkinter.Label(parent, text=self.infoblocktext, wraplength=450)
        self.infoblock.grid(row=rownum, rowspan=4, column=2, columnspan=3, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        self.confirmfiles = tkinter.Button(parent, text="Run Program", command=lambda: ProgramMain.programStart(parent))
        self.confirmfiles.grid(row=rownum, column=5, columnspan=2, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W,)
        rownum += 1

        self.helpbutton = tkinter.Button(parent, text="Show Help", command=lambda: parent.parent.changeFrame("HELP"))
        self.helpbutton.grid(row=rownum, column=5, columnspan=2, sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)

        rownum += 3
        parent.rows = rownum


###############################################################################
#   This TemplateInput block is below the InfoBlock                           #
###############################################################################
class TemplateInput(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.selectedfilename = tkinter.StringVar()
        rownum = parent.rows

        self.spacer = tkinter.Canvas(parent, height=30)
        self.spacer.grid(row=rownum, columnspan=8, sticky=tkinter.W + tkinter.E)
        self.spacer.create_line(0, 26, 2000, 26, fill="gray75")
        self.spacer.create_line(0, 29, 2000, 29, fill="gray75")
        rownum += 1

        self.templateinfo = tkinter.Label(parent, text="Select the template file. (REQUIRED)")
        self.templateinfo.grid(row=rownum, column=2, columnspan=3, sticky=tkinter.W)
        rownum += 1

        self.templatelabel = tkinter.Label(parent, text="Template:")
        self.templatelabel.grid(row=rownum, column=0, columnspan=2, sticky=tkinter.W + tkinter.E)

        self.selectedtemplate = tkinter.Entry(parent, textvariable=self.selectedfilename, width=50)
        self.selectedtemplate.grid(row=rownum, column=2, columnspan=3, sticky=tkinter.W + tkinter.E)

        self.templatebrowse = tkinter.Button(parent, text="Browse files", command=lambda: parent.selectFile(self))
        self.templatebrowse.grid(row=rownum, column=5, columnspan=2, sticky=tkinter.W + tkinter.E, padx=5, ipadx=4)
        rownum += 1

        self.spacer = tkinter.Canvas(parent, height=20)
        self.spacer.grid(row=rownum, columnspan=8, sticky=tkinter.W + tkinter.E)
        self.spacer.create_line(0, 16, 2000, 16, fill="gray75")
        self.spacer.create_line(0, 19, 2000, 19, fill="gray75")

        rownum += 1
        parent.rows = rownum


###############################################################################
#   FileInputHeader exists above the black box. List instructions here.       #
###############################################################################
class FileInputHeader(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        rownum = parent.rows
        self.fileheadertext = '''Drag and drop your files into both input boxes. (REQUIRED)'''

        self.fileheaderinfo = tkinter.Label(parent, text=self.fileheadertext)
        self.fileheaderinfo.grid(row=rownum, column=2, columnspan=3, sticky=tkinter.W, pady=0)

        self.clearinputs = tkinter.Button(parent, text="Reset filenames", command=lambda: parent.clearInputs())
        self.clearinputs.grid(row=rownum, column=5, columnspan=2, sticky=tkinter.W + tkinter.E, padx=5, ipadx=4)

        rownum += 1
        parent.rows = rownum


###############################################################################
#   FileInput is a black box that users will drag and drop their files onto.  #
###############################################################################
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
        rownum = parent.rows
        self.inputbox = tkinter.Message(parent, textvariable=self.selectedfilename, width=500, background="grey20", foreground="white", relief="sunken", anchor=tkinter.NW)
        self.inputbox.rowconfigure(0, weight=1)
        self.inputbox.grid(row=rownum, column=0, columnspan=7, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E, pady=5)

###############################################################################
