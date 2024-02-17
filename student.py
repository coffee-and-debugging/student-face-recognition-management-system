#pip install mysql-connector

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #variables
        self.var_fac=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()



        # first image
        img = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\student1.png")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second image
        img1 = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\student2.png")
        img1 = img1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # third image
        img2 = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\student3.png")
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

        # Main frame
        title_lbl = Label(bg_img, text="STUDENT DETAILS", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1275, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, width=1250, height=600)

        # left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Students Details", font=(
            "times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=650, height=480)

        img_left = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\student3.png")
        img_left = img_left.resize((640, 100), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=0, y=0, width=640, height=100)

        # current course section
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Current course info", font=(
            "times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=100, width=640, height=125)

        # Faculty
        fac_label = Label(current_course_frame, text="Faculty", font=(
            "times new roman", 13, "bold"), bg="white")
        fac_label.grid(row=0, column=0, padx=10)

        fac_combo = ttk.Combobox(current_course_frame, textvariable=self.var_fac, font=(
            "times new roman", 13, "bold"), state="readonly")
        fac_combo['values'] = ("Select Faculty",
                               "BSc.CSIT", "BIM", "BCA")
        fac_combo.current(0)
        fac_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course
        course_label = Label(current_course_frame, text="Course", font=(
            "times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=5, sticky=W)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, font=(
            "times new roman", 13, "bold"), state="readonly")
        course_combo['values'] = ("Select course", "Course by T.U", "Course by P.U", "Course by Foreign University")
        course_combo.current(0)
        course_combo.grid(row=0, column=2, padx=75, sticky=W)

        # year
        year_label = Label(current_course_frame, text="Year", font=(
            "times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=(
            "times new roman", 13, "bold"), state="readonly")
        year_combo['values'] = ("Year", "2020",
                                "2021", "2022", "2023", "2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=0, pady=10, sticky=W)

        # semester
        semester_label = Label(current_course_frame, text="Semester", font=(
            "times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, font=(
            "times new roman", 13, "bold"), state="readonly")
        semester_combo['values'] = (
            "Select semester", "First Semester", "Second Semester", "Third Semester", "Fourth Semester", "Fifth Semester", "Sixth Semester", "Seventh Semester", "Eight Semester")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=2, padx=90, pady=20, sticky=W)

        # student information section
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Class student info", font=(
            "times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=225, width=640, height=230)


        # student id
        studentId_label = Label(class_student_frame, text="StudentID:", font=(
            "times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id, width=20, font=(
            "times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)


        # student name
        student_name_label = Label(class_student_frame, text="Student name:", font=(
            "times new roman", 13, "bold"), bg="white")
        student_name_label.grid(row=0, column=2, padx=10, sticky=W)

        student_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name, width=16, font=(
            "times new roman", 13, "bold"))
        student_name_entry.grid(row=0, column=3, pady=5, sticky=W)
        


        # class division
        class_div_label = Label(class_student_frame, text="Class Division:", font=(
            "times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        class_div_entry = ttk.Entry(class_student_frame, textvariable=self.var_div, width=20, font=(
            "times new roman", 13, "bold"))
        class_div_entry.grid(row=1, column=1, padx=10, sticky=W)


        # roll no
        roll_no_label = Label(class_student_frame, text="Roll No:", font=(
            "times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, width=16, font=(
            "times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, pady=5, sticky=W)


        # gender
        gender_label = Label(class_student_frame, text="Gender:", font=(
            "times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, sticky=W)


        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender, font=("times new roman", 11, "bold"), state="readonly", width=20)
        gender_combo['values'] = ("Male","Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=13, pady=0, sticky=W)



        # date of birth
        dob_label = Label(class_student_frame, text="DOB:", font=(
            "times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, width=16, font=(
            "times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3,pady=5, sticky=W)




        # email
        email_label = Label(class_student_frame, text="Email:", font=(
            "times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, width=20, font=(
            "times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, sticky=W)



        # phone
        phone_label = Label(class_student_frame, text="Phone:", font=(
            "times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, width=16, font=(
            "times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, pady=5, sticky=W)



        # radio buttons
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take photo sample", value="yes")
        radiobtn1.grid(row=4, column=0)


        radiobtn2=ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No photo sample", value="No")
        radiobtn2.grid(row=4, column=1)

        # button frame
        btn_frame=Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=170, width=635, height=35)


        save_btn=Button(btn_frame, text="Save", command=self.add_data, font=("times new roman",13,"bold"), bg="green", fg="white", width=15, height=1)
        save_btn.grid(row=0, column=0, padx=1)


        update_btn =Button(btn_frame, text="Update", command=self.update_data, font=("times new roman", 13, "bold"), bg="blue", fg="white", width=15, height=1)

        update_btn.grid(row=0, column=1, padx=1)


        delete_btn=Button(btn_frame, text="Delete", command=self.delete_data,  font=("times new roman",13,"bold"), bg="red", fg="white", width=15, height=1)
        delete_btn.grid(row=0, column=2, padx=1)

        reset_btn=Button(btn_frame, text="Reset", command=self.reser_data, font=("times new roman",13,"bold"), bg="gray", fg="white", width=15, height=1)
        reset_btn.grid(row=0, column=3)


        # right frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Students Details", font=(
            "times new roman", 12, "bold"))
        right_frame.place(x=670, y=10, width=560, height=480)



        img_right = Image.open(
            r"C:\Users\adhik\Desktop\project SAS\Images\student2.png")
        img_right = img_right.resize((640, 100), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.photoimg_right)
        f_lbl.place(x=0, y=0, width=640, height=100)




        # searching system
        search_frame = LabelFrame(right_frame, bd=2, bg="white", relief=RIDGE, text="Search system", font=(
            "times new roman", 12, "bold"))
        search_frame.place(x=5, y=100, width=550, height=70)

        search_label = Label(search_frame, text="search by:", font=(
            "times new roman", 13, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), width=7, state="readonly")
        search_combo['values'] = ("Select", "Roll", "Phone")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


        search_entry = ttk.Entry(search_frame, width=21, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=2, sticky=W)



        search_btn=Button(search_frame, text="Search", font=("times new roman",13,"bold"), bg="red", fg="white", width=7, height=1)
        search_btn.grid(row=0, column=3, padx=2)

        showAll_btn=Button(search_frame, text="Show all", font=("times new roman",13,"bold"), bg="gray", fg="white", width=7, height=1)
        showAll_btn.grid(row=0, column=4, padx=2)


        # table frame
        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=175, width=550, height=280)

        scroll_x=Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame, orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame, column=("fac","course","year","sem","id","name","div","roll","gender","dob","email","phone"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


    

        self.student_table.heading("fac", text="Faculty")  # Corrected column name
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="ID")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")



        self.student_table["show"]="headings"

        self.student_table.column("fac", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)


        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()


        # function declaration

    def add_data(self):
        if self.var_fac.get()=="Select Faculty" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost", username="root", password="bhakari", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_fac.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added successfully!", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # fetch data from database
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", username="root", password="bhakari", database="face_recognizer")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    # get cursor
    
    def get_cursor(self, event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_fac.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_div.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])

            
    # update function
    def update_data(self):
        if self.var_fac.get() == "Select Faculty" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="bhakari", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "update student set Fac=%s, Course=%s, Year=%s, Semester=%s, Student_id=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s where Student_id=%s",
                        (
                            self.var_fac.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_id.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_std_id.get()
                        )
                    )
                    messagebox.showinfo("Success", "Student details successfully updated!", parent=self.root)
                    conn.commit()
                    self.fetch_data()
                    conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)




    #Delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must me required", parent = self.root)

        else:
            try:
                delete=messagebox.askyesno("Delete", "Do you want to delete this record", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="bhakari", database="face_recognizer")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Delete", "Record successfully deleted", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)




    #Reset function
    def reser_data(self):
        self.var_fac.set("Select Faculty")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")





        

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
