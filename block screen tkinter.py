from tkinter import *

root = Tk()
root.focus_force()
root.title("IUNAK 1.0")
root.geometry("2400x2000+0+0")
root.overrideredirect(True)
root.wm_attributes("-topmost", 1)
#root.attributes('-disabled', True)
root['bg'] = "#4B6C75"
#filename = PhotoImage(file = "base.png")
#background_label = Label(root, image=filename)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

texto = """
For a safer day
"""
texto2 = "It is easy to be brave from a safe distance"

label = Label(root,text=texto, fg="#ffffff",bg="#4B6C75",font=("Times", 30,"bold"))
label.focus_force()
label.place(x=100,y=100)
user = Label(root,text="Security Key", fg="#ddeeee",bg="#4B6C75",font=("Times", 30,"bold"))
#user = Label(root,text="User", fg="#ffffff",bg="#4B6C75",font=("Times", 30,"bold"))
user.place(x=380,y=290)
def baixo(event):
    label.config(text=texto2)
root.bind('<Any-Key>', baixo)

def pp():
    senha = entree.get()
    #Entre com uma senha
    if senha == "aaaa":
        root.destroy()
    else:
        pass
    
entree = Entry(root, show="*")
entree.place(x=610,y=310)
simm = Button(text="Entrar",command=pp)
simm.place(x=640,y=350)

root.mainloop()
