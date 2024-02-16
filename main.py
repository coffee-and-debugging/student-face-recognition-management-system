# pip install Pillow==9.5.0


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # first image
        img = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\unique adhikari.png")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second image
        img1 = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\unique adhikari.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\unique adhikari.png")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=500, height=130)

        # background image
        img3 = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\banner.png")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # title
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1275, height=45)

        # student button
        img4 = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\students.png")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=75, y=50, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",  font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=75, y=250, width=220, height=40)

        # Face detect button
        img5 = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\facedetection.png")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=375, y=50, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detectetion", cursor="hand2",  font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=375, y=250, width=220, height=40)

        # Attendance button
        img6 = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\attendance.png")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=675, y=50, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",  font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=675, y=250, width=220, height=40)

        # Help button
        img7 = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\help.png")

        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=975, y=50, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=975, y=250, width=220, height=40)

        # Help button
        img8 = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\traindata.png")

        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b1.place(x=75, y=300, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=75, y=500, width=220, height=40)

        # photos button
        img9 = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\photos.png")

        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b1.place(x=375, y=300, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=375, y=500, width=220, height=40)

        # developer button
        img10 = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\developer.png")

        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b1.place(x=675, y=300, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=675, y=500, width=220, height=40)

        # exit button
        img11 = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\exit.png")

        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b1.place(x=975, y=300, width=220, height=220)

        b1_1 = Button(bg_img, text="exit", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=975, y=500, width=220, height=40)



    # function buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
