from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
##photo=PhotoImage(file="C:\\Users\\usha3\Desktop\\890.png")
##l=Label(root)
##l.configure(image=photo)
##l.place(x=0,y=0)
root.attributes("-fullscreen",True)
root.geometry("600x500")
root['bg']='yellow'
root.title("Stock Entry Screen")
txtserial=StringVar()
txtname=StringVar()
txtfees=StringVar()
txtmode=StringVar()

def getserial():
    con=sqlite3.connect("invent.sqlite")
    c=con.cursor()
    c.execute("select serial from admin")
    data=c.fetchall()
    print(data)
    if len(data)==0:
        serial=1
    else:
        se=data[-1][0]+1
    txtserial.set(str(se))
    con.close()

def insert_clicked():
    con=sqlite3.connect("invent.sqlite")
    c=con.cursor()
    se=int(txtserial.get())
    nm=txtname.get()
    fe=txtfees.get()
    mo=txtmode.get()
    c.execute("insert into admin(serial,name,fees,mode) values (?,?,?,?)",(se,nm,fe,mo))
    con.commit()
    messagebox.showinfo("Great","1 item inserted...")
    clear_clicked()
    getserial()
    t2.focus()

def clear_clicked():
    txtserial.set("")
    txtname.set("")
    txtfees.set("")
    txtmode.set("")


l0=Label(root,text="ENTRY SCREEN",fg="red",bg="lavender",font=("Arial Black",40))
l1=Label(root,text="Serial Number",bg="black",fg="white",font=("Arial Black",30))
l2=Label(root,text="Name",bg="black",fg="white",font=("Arial Black",30))
l3=Label(root,text="Fees",bg="black",fg="white",font=("Arial Black",30))
l4=Label(root,text="Mode",fg="white",bg="black",font=("Arial Black",30))
l0.place(x=450,y=30)
l1.place(x=400,y=200)
l2.place(x=400,y=300)
l3.place(x=400,y=400)
l4.place(x=400,y=500)
t1=Entry(root,textvariable=txtserial,font=("Lucida Handwriting",25))
t2=Entry(root,textvariable=txtname,font=("Lucida Handwriting",25))
t3=Entry(root,textvariable=txtfees,font=("Lucida Handwriting",25))
t4=Entry(root,textvariable=txtmode,font=("Lucida Handwriting",25))
t1.place(x=750,y=200)
t2.place(x=680,y=300)
t3.place(x=680,y=400)
t4.place(x=680,y=500)

b1=Button(root,text="Insert",command=insert_clicked,width=20,bg="red",fg="white",font=("Arial Black",12))
b2=Button(root,text="Clear",command=clear_clicked,width=20,bg="red",fg="white",font=("Arial Black",12))
b3=Button(root,text="Exit",command=root.destroy,width=20,bg="red",fg="white",font=("Arial Black",12))
b1.place(x=500,y=600)
b2.place(x=750,y=600)
b3.place(x=1000,y=600)
getserial()
t2.focus()
root.mainloop()

