from cgitb import text
from re import M
from tkinter import *
from tkinter import font
import smtplib
from turtle import width

root = Tk()
root.geometry("1920x1080")
blank_space = " "
root.title(220*blank_space +"SMTP email app" )  
root.configure(bg="#323232")

def send():
    try:   
        username1 = username.get()
        password1 = password.get()
        to = reciever.get()
        subject1 = subject.get()
        body1 = body.get()
        if username1=="" or password1=="" or to=="" or subject1=="" or body1=="":   #if statement to check if all the fields are filled or not
            noti.config(text = "ALL FILEDS ARE REQUIRED !!" , fg = "red")
            return
        else:
            finalMessage = 'Subject: {}\n\n{}'.format(subject1, body1) #this will recognise the mail to which we have to send the mail 
            server   = smtplib.SMTP('smtp.gmail.com',587)    #server address and the port number 
            server.starttls()
            server.login(username1, password1)
            server.sendmail(username1,to,finalMessage)
            noti.config(text="Email HAS BEEN SENT SUCCESSFULLY", fg="green")
    except Exception as e:
        noti.config(text="ERROR SENDING  Email", fg="red")
        print(e)

def reset():
    usernameentr.delete(0,'end')
    passentr.delete(0,'end')
    recieverentr.delete(0, 'end')
    subentr.delete(0,'end')
    bodyentr.delete(0,'end')


heading = Label(root , text="Email app", font=('Calibri' , 35),bg="#323232",fg="#FA4EAB").pack(padx=100, pady=25)


Label(root, text="Use the form below to send an email",font=('Calibri' , 25), bg="#323232",fg="#FA4EAB").pack(padx= 100 , pady =20)
Label(root, text="Email:",font=('Calibri' , 20),bg="#323232" ,fg="#FA4EAB").place(x= 500 , y =200,anchor="center")
Label(root , text="Password:", font=('Calibri' , 20),bg="#323232",fg="#FA4EAB").place(x= 480 , y =280,anchor="center")
Label(root , text="To:", font=('Calibri' , 20),bg="#323232",fg="#FA4EAB").place(x= 520 , y =360,anchor="center")
Label(root , text="Subject:", font=('Calibri' , 20),bg="#323232",fg="#FA4EAB").place(x= 495 , y =440,anchor="center")
Label(root , text="Body:", font=('Calibri' , 20),bg="#323232",fg="#FA4EAB").place(x= 505 , y =520,anchor="center")
noti= Label(root , text="", font=('Calibri' , 20),bg="#323232",fg="#FA4EAB") #notifications 
noti.place(x= 750 , y =700,anchor="center")
username = StringVar()
password = StringVar()
reciever = StringVar()
subject = StringVar()
body = StringVar()
var = IntVar()


usernameentr = Entry(root, textvariable=username, font=('Calibri', 15), bd=5)
# entry_box.place(height=40, width=100)
usernameentr.place(x=750, y=200, height=35, width=400, anchor="center")

passentr = Entry(root, textvariable=password,
                 show="*", font=('Calibri', 15), bd=5)
passentr.place(x=750, y=280, height=35, width=400, anchor="center")

recieverentr = Entry(root, textvariable=reciever, font=('Calibri', 15), bd=5)
recieverentr.place(x=750, y=360, height=35, width=400, anchor="center")
subentr = Entry(root, textvariable=subject, font=('Calibri', 15), bd=5)
subentr.place(x=750, y=440, height=35, width=400, anchor="center")

bodyentr = Entry(root, textvariable=body, font=('Calibri', 15), bd=5)
bodyentr.place(x=750, y=520, height=35, width=400, anchor="center")


sendbutton = Button(root, text="Send mail", command=send, fg="#FA4EAB", font=(
    'Calibri', 20)).place(x=750, y=600, height=35, width=300, anchor="center")
resetbutton = Button(root, text="Reset mail", command=reset, fg="#FA4EAB", font=(
    'Calibri', 20)).place(x=750, y=660, height=35, width=300, anchor="center")
root.mainloop()


