from tkinter import *
from tkinter import messagebox
ws=Tk()
ws.title("Python guide")
ws.state("zoomed")

menubar=Menu(ws,background="green",foreground="yellow",activebackground="red",activeforeground="blue",activeborderwidth=50)
file=Menu(menubar,tearoff=1,background="pink",foreground="blue")
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as")
file.add_separator()
file.add_command(label="Exit",command=ws.quit)
menubar.add_cascade(label="File",menu=file)


edit=Menu(menubar,tearoff=0,background="black",foreground="white")
edit.add_command(label="Undo")
edit.add_command(label="Redo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")
menubar.add_cascade(label="Edit",menu=edit)
def about():
    messagebox.showinfo("About","menu Guide")
def darkMode():
    if dmode.get()==1:
        ws.config(background="black")
    elif dmode.get()==0:
        ws.config(background="White")
    else:
        messagebox.showerror("menu bar Guides","Somthing went wrong")

minimap=BooleanVar()
minimap.set(True)
dmode=BooleanVar()
dmode.set(False)

view=Menu(menubar,tearoff=0)
view.add_checkbutton(label="Show minimap",onvalue=1,offvalue=0,variable=minimap)
view.add_checkbutton(label="Dark Mode",onvalue=1,offvalue=0,variable=dmode,command=darkMode)
menubar.add_cascade(label="View",menu=view)

help=Menu(menubar,tearoff=0)
help.add_command(label="About",command=about)
menubar.add_cascade(label="Help",menu=help)
ws.config(menu=menubar)
mainloop()