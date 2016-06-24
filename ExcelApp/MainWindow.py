import tkinter as tk
import MainFrame as mf
import AuxillaryFrame as af


class MainApplication(tk.Frame):

    # changeFrame is used to handle the switches between the different frames.
    def changeFrame(self, frame):
        if frame == "MAIN":
            self.main.grid()
            self.help.grid_remove()
            self.msg.grid_remove()
            self.back.grid_remove()
        elif frame == "HELP":
            self.main.grid_remove()
            self.help.grid()
            self.msg.grid_remove()
            self.back.grid_remove()
        elif frame == "MSG":
            self.main.grid_remove()
            self.help.grid_remove()
            self.msg.grid()
            self.back.grid_remove()
        elif frame == "BACK":
            self.main.grid_remove()
            self.help.grid_remove()
            self.msg.grid_remove()
            self.back.grid()
        else:
            self.main.grid()
            self.help.grid_remove()
            self.msg.grid_remove()
            self.back.grid_remove()

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.workingmessage = tk.StringVar()

        self.main = mf.MainFrame(self)
        self.help = af.HelpFrame(self)
        self.msg = af.MessageFrame(self)
        self.back = af.ReturnFrame(self)

        self.grid()
