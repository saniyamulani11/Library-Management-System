from tkinter import *
#from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql
from main import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *

def userRegister():

     global SubmitBtn,labelFrame,lb1,lb2,bookInfo1,bookInfo2,quitBtn,root,Canvas1,status
    
     Userid = bookInfo1.get()
     Password = bookInfo2.get()

     SubmitBtn.destory()
     lb1.destroy()
     lb2.destroy()
     bookInfo1.destroy()
     bookInfo2.destroy()


    
     insertUserDetails = "insert into "+Tables+" values('"+Userid+"','"+Password+"')"

     try:
        cur.execute(insertUserDetails)
        con.commit()
        messagebox.showinfo('Success',"Login successfully")


     except:
        messagebox.showinfo("Error","Can't add data into Database")
    
     print(Userid)
     print(Password)



     root.destroy()
    
def adduser():
    
    global bookInfo1,bookInfo2,Canvas1,con,cur,Tables,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    # Add your own database name and password here to reflect in the code
    mypass = "mysql@123"
    mydatabase="db"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    # Enter Table Names here



    Tables = "user_details"

    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#7FFFD4")
    Canvas1.config(bg="#7FFFD4")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Login", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
        
    # User ID
    lb1 = Label(labelFrame,text="User ID : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2, relheight=0.08)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
        
    # Password
    lb2 = Label(labelFrame,text="PassWord : ", bg='black', fg='white')
    lb2.place(relx=0.05,rely=0.35, relheight=0.08)
        
    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
        

        
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=main)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)

    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)

    root.mainloop()
