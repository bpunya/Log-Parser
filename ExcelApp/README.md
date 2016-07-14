Application made for an unnamed company to help process log files into Excel Spreadsheets.
Runs in Python 3.5, requires Openpyxl (http://openpyxl.readthedocs.io/) and the tkdnd library (https://sourceforge.net/projects/tkdnd/)

tkdnd_wrapper.py taken from mmpg on stackoverflow.

Starts through main.py


Format of the nested classes is as follows:
# Parent
# |
# |-- Child


root (TK instance)
|
|-- application (ApplicationWrapper)
    |
    |-- scrollbar (Scrollbar)
    |-- main (MainWindow)
        |-- changeFrame()
        |
        |-- msg (MessageFrame)
        |-- help (HelpFrame)
        |-- back (ReturnFrame)
        |-- main (MainFrame)
            |-- selectFile(), clearInputs(), handleTempalteInput(), handleFileInput()
            |
            |-- tcl (Tcl interpreter)
            |-- infoblock (InfoBlock) >>> Accesses ProgramMain.startProgram()
            |-- templateinput (TemplateInput)
            |-- fileinputheader (FileInputHeader)
            |-- fileinput (FileInput)
                
