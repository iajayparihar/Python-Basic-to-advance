from tkinter import *
ws=Tk()
ws.config(bg='red')
message='''     qcxbuhknewrfc          '''
txt_box=Text(ws,height=12,width=40)
txt_box.pack(expand=True)
txt_box.insert(END,message)
txt_box.config(state="disable")
ws.mainloop()