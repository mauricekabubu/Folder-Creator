from cProfile import label
from os import rename
from tkinter import *
from tkinter import messagebox
import os

class Main:
    def __init__(self,app):
        self.app = app
        app.config(bg="beige")
        app.title("File-creator")
        app.geometry("500x400")

        label = Label(app,text="Folder/file creator",bg="beige",fg="magenta",font=("Arial bold",20))
        label.pack(pady=10)
        label0 = Label(app,text="This Gui application is to make it easier\n"
                                " for users to be able to create folders and files\n"
                                "in the background without technical knowledge.\n"
                                "Its more fast and efficient enabling a user to\n"
                                "delete, rename an existing folder/file.\n",font=("arial bold",15),
                       bg="beige",fg="green")
        label0.place(x=30,y=50)
        button = Button(app,text="Start",bg="blue",fg="white",
                        font=("arial bold",15),width=20,bd=0,command=lambda :self.create())
        button.place(x=130,y=200)

    def create(self):
        self.delete()
        app.geometry("500x500")
        label1 = Label(app,text="Enter name of folder",bg="beige",fg="black",
                       font=("arial bold",13))
        label1.place(x=160,y=10)
        entry = Entry(app,bg="cyan",fg="black",font=("arial bold",13),width=40,bd=0)
        entry.place(x=70,y=50)
        button0 = Button(app, text="create", bg="green", fg="white",
                        font=("arial bold", 15), width=20, bd=0,command=lambda :self.folder(entry))
        button0.place(x=120, y=80)
        label2 = Label(app, text="Enter name of file", bg="beige", fg="black",
                       font=("arial bold", 13))
        label2.place(x=160, y=130)
        entry0 = Entry(app, bg="cyan", fg="black", font=("arial bold", 13), width=40, bd=0)
        entry0.place(x=70, y=160)
        button1 = Button(app, text="create", bg="green", fg="white",
                        font=("arial bold", 15),width=20,bd=0,command=lambda :self.file(entry0))
        button1.place(x=120, y=190)
        label3 = Label(app, text="Delete existing file/folder", bg="beige", fg="black",
                       font=("arial bold", 13))
        label3.place(x=160, y=230)
        entry1 = Entry(app, bg="cyan", fg="black", font=("arial bold", 13), width=40, bd=0)
        entry1.place(x=70, y=260)
        button2 = Button(app, text="Delete", bg="red", fg="white",
                         font=("arial bold", 15), width=20, bd=0,command=lambda :self.delete_folder(entry1))
        button2.place(x=120, y=290)
        label4 = Label(app, text="Rename existing file/folder", bg="beige", fg="black",
                       font=("arial bold", 13))
        label4.place(x=160, y=330)
        entry2 = Entry(app, bg="cyan", fg="black", font=("arial bold", 13), width=40, bd=0)
        entry2.place(x=70, y=360)
        entry3 = Entry(app, bg="cyan", fg="black", font=("arial bold", 13), width=40, bd=0)
        entry3.place(x=70, y=390)
        button3 = Button(app, text="Rename", bg="blue", fg="white",
                         font=("arial bold", 15), width=20, bd=0,command=lambda :self.rename(entry2,entry3))
        button3.place(x=120, y=420)
        button4 = Button(app, text="cancel", bg="magenta", fg="white",
                         font=("arial bold", 15), width=20, bd=0,command=exit)
        button4.place(x=120, y=460)

    def folder(self,entry):
        result0 = entry.get()
        if os.path.exists(result0):
            messagebox.showerror("File-creator",f"{result0} folder already exists!")
        else:
            os.mkdir(result0)
            messagebox.showinfo("File-creator",f"{result0} folder created successfully...")

    def file(self,entry0):
        result1 = entry0.get()
        if os.path.exists(result1):
            messagebox.showerror("File-creator",f"{result1} file already exists!")
        else:
            os.makedirs(result1)
            messagebox.showinfo("File-creator",f"{result1} file created successfully")

    def delete_folder(self,entry1):
        result0 = entry1.get()
        if os.path.exists(result0):
            os.rmdir(result0)
            messagebox.showinfo("File-creator",f"{result0} successfully deleted")
        else:
            messagebox.showerror("File-creator",f"{result0} does not exist")

    def rename(self,entry2,entry3):
        result = entry2.get()
        result0 = entry3.get()

        if os.path.exists(result):
            os.renames(result,result0)
            messagebox.showinfo("File-creator",f"{result} successfully renamed to {result0}")

        else:
            messagebox.showerror("File-creator",f"{result} does not exists!")



    def delete(self):
        for item in app.winfo_children():
            item.destroy()


app = Tk()
obj = Main(app)
app.mainloop()