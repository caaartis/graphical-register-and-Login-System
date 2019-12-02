from tkinter import *
import os
def view_notes1():
    filename1=raw_filename1.get()
    data=open(filename1,"r")
    data1=data.read()
    screen12=Toplevel(screen)
    screen12.title("Info")
    screen12.geometry("400x400")
    Label(screen12,text="Datat1").pack()
    Label(screen12,text=data1).pack()
    data.close()
def deleted_note():
    screen14=Toplevel(screen)
    screen14.title("Deleted Note")
    screen14.geometry("400x400")
    filename3=raw_filename2.get()
    os.remove(filename3)
    Label(screen14,text=filename3+"Removed").pack()


def delete_note():
    screen13=Toplevel(screen)
    screen13.title("Delete Note")
    screen13.geometry("400x400")
    global raw_filename2
    raw_filename2=StringVar()
    Label(screen13,text="enter the file name ").pack()
    Entry(screen13,textvariable=raw_filename2).pack()
    Button(screen13,text="Ok",command=deleted_note).pack()


def delete2():
    screen3.destroy()
def delete3():
    screen4.destroy()
def delete4():
    screen5.destroy()
def logout():
    screen7.destroy()
def session():
    screen8=Toplevel(screen)
    screen8.title("Dashboard")
    screen8.geometry("400x400")
    Label(screen8,text="Welcome to thee dashboard").pack()
    Button(screen8,text="Create Note",command=create_notes).pack()
    Button(screen8,text="View Note",command=view_notes).pack()
    Button(screen8,text="Delete Note",command=delete_note).pack()
def view_notes():
    screen11=Toplevel(screen)
    screen11.title("Info")
    screen11.geometry("300x200")
    Label(screen11,text="Welcome to view Note").pack()
    #show exisiting files to user
    existing_files=os.listdir()
    Label(screen11,text="Please use one of the file names below").pack()
    Label(screen11,text=existing_files).pack()
    global raw_filename1
    raw_filename1=StringVar()

    Entry(screen11,textvariable=raw_filename1).pack()
    Button(screen11,command=view_notes1,text="OK").pack()


def saved():
    screen10=Toplevel(screen)
    screen10.title("Dashboard")
    screen10.geometry("100x100")
    #Gather from the user name of the file and its content
    Label(screen10,text="Please enter a file name for the notes below: ").pack()

def save():
    filename=raw_filename.get()
    notes=raw_notes.get()
    data=open(filename,"w")
    data.write(notes)
    data.close()
    saved()
def create_notes():
    global raw_filename
    raw_filename=StringVar()
    global raw_notes
    raw_notes=StringVar()
    screen9=Toplevel(screen)
    screen9.title("Dashboard")
    screen9.geometry("300x200")
    #Gather from the user name of the file and its content
    Label(screen9,text="Please enter a file name for the notes below: ").pack()
    Entry(screen9,textvariable=raw_filename).pack()
    Label(screen9,text="Please enter the notes for the file below").pack()
    Entry(screen9,textvariable=raw_notes).pack()
    Button(screen9,text="Save",command=save).pack()





def login_success():
    global screen3
    screen3=Toplevel(screen)
    screen3.title("Login Success!")
    screen3.geometry("300x250")
    Label(screen3,text="Login Success").pack()
    Button(screen3, text="ok",command=session).pack()
def password_not_recognized():
    global screen4
    screen4=Toplevel(screen)
    screen4.title("Password failed!")
    screen4.geometry("300x250")
    Label(screen4,text="Password error").pack()
    Button(screen4, text="ok",command=delete3).pack()

def user_not_found():
    global screen5
    screen5=Toplevel(screen)
    screen5.title("User not recognized")
    screen5.geometry("300x250")
    Label(screen5,text="User not reconized").pack()
    Button(screen5, text="ok",command=delete4).pack()


def login_verify():
    username1=username_verify.get()
    password1=password_verify.get()
    username_entry1.delete(0,END)
    password_entry1.delete(0,END)

    list_of_files=os.listdir()
    if username1 in list_of_files:
        file1=open(username1,"r")
        verify=file1.read().splitlines()
        if password1 in verify:
             login_success()
        else:
            password_not_recognized()
    else:
        user_not_found()

def register_user():

    username_info=username.get()
    password_info=password.get()

    file=open(username_info,"w")
    file.write(username_info+"\n")
    file.write(password_info)
    file.close()
    #two entry below to clear the entry when registered
    username_entry.delete(0,END)
    password_entry.delete(0,END)

    Label(screen1, text="REgsiteration successful",fg="yellow",bg="red",font=("Calibri",11)).pack()



def register():
    global screen1
    screen1=Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    #we will need user name and password
    global username
    global password
    global username_entry
    global password_entry
    username=StringVar()
    password=StringVar()
    #Now create the entry
    Label(screen1,text="Please enter details below*").pack()
    Label(screen1,text=" ").pack()
    Label(screen1,text="Username *").pack()
    global username_entry
    global password_entry
    username_entry=Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1,text="Password *").pack()
    password_entry=Entry(screen1,textvariable=password)
    password_entry.pack()



    Label(screen1,text="Password *").pack()
    password_entry=Entry(screen1,textvariable=password)
    Button(screen1,text="REgister",width=10,height=1,bg="green",command=register_user).pack()



def login():
    global screen2;
    screen2=Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2,text="Please enter details below to login in").pack()
    Label(screen2,text="").pack()
    global username_verify
    global password_verify
    username_verify=StringVar()

    password_verify=StringVar()

    global username_entry1
    global password_entry1




    Label(screen2,text="Username *").pack()
    username_entry1=Entry(screen2,textvariable=username_verify)
    username_entry1.pack()
    Label(screen2,text="Password").pack()
    password_entry1=Entry(screen2,textvariable=password_verify)
    password_entry1.pack()
    Label(screen2,text="").pack()
    Button(screen2,text="Login",width=10,height=1,command=login_verify).pack()



def main_screen():
    global screen
    screen=Tk()
    screen.geometry("300x250");
    screen.title("Notes");
    Label(text="Notes 1.0",bg="grey",width="300",height="2",font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="Login",bg="yellow",height="2",width="30",command=login).pack()
    Label(text="").pack()
    Button(text="Register",bg="red",height="2",width="30",command=register).pack()
    screen.mainloop()
main_screen()
