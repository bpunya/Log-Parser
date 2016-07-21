import tkinter
import MainWindow

root = tkinter.Tk()
root.resizable(width=False, height=False)
root.geometry("635x320+100+100")
root.title("Excel Sheet Creator")
application = MainWindow.ApplicationWrapper(root)
application.pack(fill="both", expand=True)
root.mainloop()

# Format of the nested classes is as follows:
#
# "Parent"
# |
# |-- "Child1"
# |-- "Child2"
#
# root (TK instance)
# |
# |-- application (ApplicationWrapper)
#     |
#     |-- scrollbar (Scrollbar)
#     |-- main (MainWindow)
#         |-- changeFrame()
#         |
#         |-- msg (MessageFrame)
#         |-- help (HelpFrame)
#         |-- back (ReturnFrame)
#         |-- main (MainFrame)
#             |-- selectFile(), clearInputs(), handleTempalteInput(), handleFileInput()
#             |
#             |-- tcl (Tcl interpreter)
#             |-- infoblock (InfoBlock) >>> Accesses ProgramMain.programStart()
#             |-- templateinput (TemplateInput)
#             |-- fileinputheader (FileInputHeader)
#             |-- fileinput (FileInput)

