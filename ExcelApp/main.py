import tkinter as tk
import MainWindow as m
import os
from tkdnd_wrapper import TkDND

root = tk.Tk()
dnd = TkDND(root)
root.title("Excel Sheet Creator")
application = m.MainApplication(root)

def handle(event):
    filelist = root.tk.splitlist(event.data)
    application.main.inputlist = list(filelist)
    filenames = []
    for filename in filelist:
        filenames.append(os.path.basename(filename))
    application.main.fileinput.selectedfilenames.set(", ".join(filenames))

dnd.bindtarget(application.main.fileinput.inputbox, handle, 'text/uri-list')
root.mainloop()
