import tkinter
import MainFrame
import AuxillaryFrame


class ApplicationWrapper(tkinter.Frame):

    # This forces the widget to update its own size for the scrollbar
    def onWrapperSizeChange(self, event):
        self.wrapper.config(scrollregion=self.application.bbox("all"))

    # This wrapper is to allow the scrollbar to work
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent)
        self.parent = parent

        self.wrapper = tkinter.Canvas(self, bd=0, width=619, height=380)
        self.scrollbar = tkinter.Scrollbar(self, command=self.wrapper.yview)
        self.applicationframe = tkinter.Frame(self.wrapper, bd=0)
        self.application = MainWindow(self.applicationframe)

        self.wrapper.config(yscrollcommand=self.scrollbar.set, scrollregion=self.application.bbox("all"))
        self.scrollingframe = self.wrapper.create_window(0, 0, window=self.applicationframe, anchor=tkinter.NW)

        self.wrapper.pack(side="left")
        self.scrollbar.pack(side="right", fill="both")
        self.application.pack(side="left", fill="both", expand=True)

        self.applicationframe.bind("<Configure>", self.onWrapperSizeChange)


class MainWindow(tkinter.Frame):

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
        tkinter.Frame.__init__(self, parent)
        self.parent = parent
        self.workingmessage = tkinter.StringVar()

        self.main = MainFrame.MainFrame(self)
        self.help = AuxillaryFrame.HelpFrame(self)
        self.msg = AuxillaryFrame.MessageFrame(self)
        self.back = AuxillaryFrame.ReturnFrame(self)
