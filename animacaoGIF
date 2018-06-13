import tkinter
from PIL import Image, ImageTk, ImageSequence
Height = 200
Width = 200
class App:
    def __init__(self,parent):
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width = Width, height = Height)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                                for img in ImageSequence.Iterator(
                                    Image.open(
                                        r'C:\Users\ray\Desktop\globo.gif'))]
        self.image = self.canvas.create_image(100,100, image=self.sequence[0])
        self.animating = True
        self.animate(0)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        if not self.animating:
            return
        self.parent.after(33, lambda: self.animate((counter+1) % len(self.sequence)))

root = tkinter.Tk()
root.title("STARTING...")
root.overrideredirect(True)
root.geometry("+0+0")
root.lift()
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "#f8ece9")
app = App(root)

root.mainloop()
