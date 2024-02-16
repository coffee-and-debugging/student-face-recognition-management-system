from tkinter import *
from PIL import Image, ImageTk


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x900")
        self.root.title("HDeveloper")

        # bg image
        img = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\banner.png")
        img = img.resize((900, 900), Image.ANTIALIAS)
        self.img1 = ImageTk.PhotoImage(img)
        lbl = Label(self.root, image=self.img1)
        lbl.place(x=100, y=100, width=500, height=500)

        # next image
        img2 = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\banner.png")
        img2 = img2.resize((200, 200), Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(img2)
        lbl = Label(self.root, image=self.img2)
        lbl.place(x=100, y=100, width=300, height=300)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
