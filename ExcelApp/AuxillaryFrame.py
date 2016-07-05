import tkinter

######################################################################################
class MessageFrame(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.label = tkinter.Label(self, textvariable=parent.workingmessage, width = 86, height = 20)
        self.label.grid(padx=3, pady=3)
        self.grid_remove()


######################################################################################
class ReturnFrame(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self,parent)
        self.parent = parent
        self.returnbutton = tkinter.Button(self, textvariable=parent.workingmessage, wraplength=300, width = 86, height = 20, command=lambda: parent.changeFrame("MAIN"))
        self.returnbutton.grid(padx=1, pady=1)
        self.grid_remove()


######################################################################################
class HelpFrame(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent

        helptext = '''This Application was designed to quickly parse log files and create or update Job Dockets for JD employees. This application is not all-purpose and all non-text files that differ from the format listed below will break the program.


HOW THE DOCKET TEMPLATE PARSER WORKS:

1. It will ignore all lines above the first line that starts with the word "Docket". Case is not important.
2. After the first Docket is met, it will include all lines as codes for that docket until it reads a blank line. This is CASE SENSITIVE. The entire line is considered a separate code.
3. After the blank line, the program will wait for another line that starts with the word "Docket". Again this is not case sensitive.
4. The process repeats, with the program considering all separate lines as individual job codes until another blank line is met.
Because of these restrictions, the docket template file MUST END WITH A BLANK LINE. You may write text after the blank line, but if it ends on a code in a docket, the program will not recognize the last docket and it will be forgotten.


HOW THE LOG FILE PARSER WORKS:
The log files are also parsed very strictly and any variance will break the program. Both the title and lines of text are parsed for information. The program's method is as follows:
(Asterisks are character wildcards, each letter's purposes are described below.)

TITLE: ***************************************ZZZZZZZZZZZZZZ.txt
    Z characters determine the label for the cycle name

LINES: ***********CCCC*TTT**QQQQQQQ
    C characters determine the code of the job. They are compared to the codes found in the docket template
    T characters determine whether the line is ignored or kept. QUA values are kept, the rest are ignored
    Q characters determine the quantity of the product that was processed'''

        self.returnbutton = tkinter.Button(self, text="Click here to return to the input screen", width = 40, command=lambda: parent.changeFrame("MAIN"))
        self.returnbutton.grid(row=2, pady=10, ipady=5)

        self.text = tkinter.Message(self, text=helptext, width = 580)
        self.text.grid(row=3, padx=20, pady=10)

        self.grid(padx=4, pady=30)
        self.grid_remove()


######################################################################################
