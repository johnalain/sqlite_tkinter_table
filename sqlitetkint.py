#https://youtu.be/geDjQUaTKAY?list=PLlvFEn0NKwXKqRBEMaCY6f7CDatHceeYL
from tkinter import *
import sqlite3

with sqlite3.connect("details.db") as db:
    cursor = db.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS users
               (id integer PRIMARY KEY AUTOINCREMENT,
               username text NOT NULL,password text NOT NULL);""")

def add_new_user():
    newUsername = username.get()
    newPassword = password.get()
    cursor.execute("SELECT COUNT(*) from users WHERE username = '" +newUsername +" '")
    result = cursor.fetchone()
    if int(result[0])>0:
     error["text"]= "Error:Usename already exists"
    else:
     error["text"]="added new user"
     cursor.execute("INSERT INTO users (username,password) VALUES(?,?)",(newUsername,newPassword))
     db.commit()




   
    
    
window = Tk()
window.geometry('450x180')
error = Message(text="",width=160)
error.place(x=30,y=10)
error.config(padx=0)



label1 = Label(text="enter username: ")
label1.place(x=30,y=40)
label1.config(bg = 'lightgreen',padx = 0)

username = Entry(text=" ")
username.place (x=150,y=40,width=200,height=25)

label2 = Label(text="enter password: ")
label2.place(x=30,y=80)
label2.config(bg='lightgreen',padx=0)

password = Entry(text= "")
password.place(x=150,y=80,width=200,height=25)
button = Button(text="add",command = add_new_user)
button.place(x=150,y=120,width=25,height=35)

window.mainloop()
