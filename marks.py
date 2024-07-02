from tkinter import *
from PIL import ImageTk
import pymysql
from tkinter import messagebox

def connect_database():
    if nameEntry.get() == '' or rollnoEntry.get() == '' or m1Entry.get() == '' or m2Entry.get() == '' or m3Entry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='saloni')
            mycursor = con.cursor()

            try:
                mycursor.execute('CREATE DATABASE IF NOT EXISTS marks')
                mycursor.execute('USE marks')
                mycursor.execute('''
                    CREATE TABLE IF NOT EXISTS student (
                        rollno INT PRIMARY KEY,
                        name VARCHAR(35),
                        m1 VARCHAR(10),
                        m2 VARCHAR(20),
                        m3 VARCHAR(20)
                    )
                ''')

                query = 'INSERT INTO student (rollno, name, m1, m2, m3) VALUES (%s, %s, %s, %s, %s)'
                mycursor.execute(query, (
                    rollnoEntry.get(),
                    nameEntry.get(),
                    m1Entry.get(),
                    m2Entry.get(),
                    m3Entry.get()
                ))

                con.commit()
                marks_subject1 = int(m1Entry.get())
                marks_subject2 = int(m2Entry.get())
                marks_subject3 = int(m3Entry.get())

                total_marks = marks_subject1 + marks_subject2 + marks_subject3
                percentage = (total_marks / 300) * 100

                marksheet_text = f"Name: {nameEntry.get()}\nRoll No: {rollnoEntry.get()}\n\n"
                marksheet_text += f"Subject 1: {marks_subject1}\nSubject 2: {marks_subject2}\nSubject 3: {marks_subject3}\n"
                marksheet_text += f"\nTotal Marks: {total_marks}\nPercentage: {percentage:.2f}%"

                messagebox.showinfo("Marksheet", marksheet_text)
                marksheet.destroy()
            except ValueError:
                messagebox.showerror("Input Error", "Please enter valid marks for all subjects.")



            except pymysql.MySQLError as e:
                messagebox.showerror('Database Error', f'Error executing query: {e}')
                con.rollback()

            finally:
                con.close()

        except pymysql.MySQLError as e:
            messagebox.showerror('Connection Error', f'Error connecting to database: {e}')




marksheet = Tk()
marksheet.configure(background='violet')
marksheet.geometry('1300x600')

marksheet.title("SINGUP PAGE ")




frame = Frame(marksheet, bg='white')
frame.place(x=900, y=150)

heading = Label(frame, text='Create Account', width=15, font=('Microsoft Yahei UI Light', 23, 'bold'), bg='white',
                fg='firebrick1')
heading.grid(row=0, column=0, padx=10, pady=10)

name = Label(frame, text='name', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                    fg='firebrick1')
name.grid(row=1, column=0, sticky='w', padx=25, pady=(10, 0))
nameEntry = Entry(frame, width=30,  font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white',
                   bg='firebrick1')
nameEntry.grid(row=2, column=0, sticky='w', padx=25)


rollno = Label(frame, text='rollno', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                    fg='firebrick1')
rollno.grid(row=3, column=0, sticky='w', padx=25, pady=(10, 0))
rollnoEntry = Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white',
                   bg='firebrick1')
rollnoEntry.grid(row=4, column=0, sticky='w', padx=25)


m1 = Label(frame, text='m1', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                    fg='firebrick1')
m1.grid(row=5, column=0, sticky='w', padx=25, pady=(10, 0))
m1Entry = Entry(frame, width=30,  font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white',
                   bg='firebrick1')
m1Entry.grid(row=6, column=0, sticky='w', padx=25)


m2 = Label(frame, text='m2', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                    fg='firebrick1')
m2.grid(row=7, column=0, sticky='w', padx=25, pady=(10, 0))
m2Entry = Entry(frame, width=30,  font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white',
                   bg='firebrick1')
m2Entry.grid(row=8, column=0, sticky='w', padx=25)

m3 = Label(frame, text='m3', font=('Microsoft Yahei UI Light', 10, 'bold'), bg='white',
                    fg='firebrick1')
m3.grid(row=9, column=0, sticky='w', padx=25, pady=(10, 0))
m3Entry = Entry(frame, width=30,  font=('Microsoft Yahei UI Light', 10, 'bold'), fg='white',
                   bg='firebrick1')
m3Entry.grid(row=10, column=0, sticky='w', padx=25)



signupButton = Button(frame, text='signup ', font=('Microsoft Yahei UI Light', 12, 'bold'), fg='white', bg='firebrick1',
                      activeforeground='white', activebackground='firebrick1', width=17, command=connect_database)
signupButton.grid(row=12, column=0, pady=10)


marksheet.mainloop()
