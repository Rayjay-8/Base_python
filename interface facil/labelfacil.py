from tkinter import *

def button(textoBotao,info,funcao):
    root = Tk()
    root.geometry("1200x60+0+0")
    root.config(bg="#343434")
    root.overrideredirect(1)
    root.wm_attributes('-topmost','true')
    for i in range(0,len(textoBotao)):
        print(i)
        var = StringVar()
        label = Label( root, textvariable=info )
        button= Button(root, text=textoBotao[i],
        fg="#eeeeee",bg="#343434",
        activebackground="#454545",
        font=('', 32), border = "0",
        compound="center",command=funcao[i])
        button.pack(side=LEFT,anchor=NW, expand=NO, fill=NONE)
    root.mainloop()
