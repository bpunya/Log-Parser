import tkinter

###############################################################################


class MessageFrame(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.label = tkinter.Label(self, textvariable=parent.workingmessage, width=86, height=20)
        self.label.grid(padx=3, pady=3)
        self.grid_remove()


###############################################################################
class ReturnFrame(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.returnbutton = tkinter.Button(self, textvariable=parent.workingmessage, wraplength=300, width=86, height=20, command=lambda: parent.changeFrame("MAIN"))
        self.returnbutton.grid(padx=1, pady=1)
        self.grid_remove()


###############################################################################
class HelpFrame(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent

        helptext = '''This Application was designed to quickly parse log files and update Job Docket information for JD employees. This application is not all-purpose and all non-text files that differ from the format listed below will break the program.


HOW THE DOCKET TEMPLATE PARSER WORKS:

1. It will ignore all lines above the first line that starts with the word "Docket". Case is not important.
2. After the first Docket is met, it will include all following lines as codes for that docket until it reads a blank line. The entire line is considered a separate code and it IS CASE SENSITIVE.
3. After the blank line, the program will ignore all lines until it reaches one that starts with the word "Docket". Again this is NOT case sensitive.
4. The process repeats, with the program considering all lines after a "Docket" as job codes until another blank line is met.


HOW THE LOG FILE PARSER WORKS:
The log files are also parsed very strictly and any variance will break the program. Both the filename and lines of text within are used. The program's method is as follows:
(Asterisks are character wildcards, each letter's purposes are described below.)

TITLE: ***************************************ZZZZZZZZZZZZZZ.txt
    If the title has less than 52 characters, the file is ignored.
    Z characters determine the label for the cycle name. They are the 40th to 53rd characters.

LINES: ***********CCCC*TTT**QQQQQQQ
    The program expects each line to be 28 characters long.
    C characters determine the code of the job. They are compared to the codes found in the docket template. They are the 12th to 15th characters.
    T characters determine whether the line is ignored or kept. QUA values are kept, the rest are ignored. They are the 17th to 19th characters.
    Q characters determine the quantity of the product that was processed. They are the 22nd to 28th characters.'''

        self.returnbutton = tkinter.Button(self, text="Click here to return to the input screen", width=40, command=lambda: parent.changeFrame("MAIN"))
        self.returnbutton.grid(row=2, pady=10, ipady=5)

        self.text = tkinter.Message(self, text=helptext, width=580)
        self.text.grid(row=3, padx=20, pady=10)

        self.grid(padx=4, pady=30)
        self.grid_remove()


###############################################################################
