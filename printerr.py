from tkinter import *
from tkinter import ttk
import win32printing



def installed_printer():
    printers = win32printing.EnumPrinters(2)
    return


def locprinter():
    pt = Toplevel()
    pt.geometry("250x250")
    pt.title("choose printer")
    LABEL = Label(pt, text="select Printer").pack()
    PRCOMBO = ttk.Combobox(pt, width=35, 
    textvariable=installed_printer).pack()
    BUTTON = ttk.Button(pt, text="refresh", 
    command=installed_printer).pack()


root = Tk()
root.title("printer selection in tkinter")
root.geometry("400x400")


menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="printer", command=locprinter)


LAB = Label(root, text="Comment")
T2 = Text(root, width=40, height=10)


def INFO():

	print(T2.get("1.0", END))


Print_Button = Button(root, text ="Print", command = 
INFO).place(x=180,y=250)

LAB.pack()
T2.pack()

root.mainloop()