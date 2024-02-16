from tkinter import *
from PIL import Image, ImageTk


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x900+0+0")
        self.root.title("Help Desk")

        # bg image
        bgimg = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\help.png")
        bgimg = bgimg.resize((900, 900), Image.ANTIALIAS)
        self.root(bgimg)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
