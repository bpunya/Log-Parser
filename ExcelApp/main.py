import tkinter
import MainWindow

root = tkinter.Tk()
root.resizable(width=False, height=False)
root.geometry("635x320+100+100")
root.title("Excel Sheet Creator")
application = MainWindow.ApplicationWrapper(root)
application.pack(fill="both", expand=True)
root.mainloop()
