from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PyPDF2 import PdfWriter, PdfReader
import os

root=Tk()
root.title("Pdf Protector")
root.geometry("600x430+300+100")
root.resizable(False,False)

def browse():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetype=(('PDF File','*.pdf'),('all files','*.*')))
    entry1.insert(END,filename)
    

def Protect():
    mainfile=source.get()
    protectfile=target.get() 
    code=password.get()
    
    print(mainfile)
    print(protectfile)
    print(code)
    
    if mainfile=="" and protectfile=="" and password.get()=="":
        messagebox.showerror("Invalid","All entries are empty!!")
        
    elif mainfile=="":
        messagebox.showerror("Invalid","PLease Type Source PDF FIlename")
        
    elif protectfile=="":
        messagebox.showerror("Invalid","Please Type Target PDF Filename!!")
        
    elif password.get() =="":
        messagebox.showerror('Invalid',"Please Type Password")
        
    else:
        try:
            out=PdfWriter()
            file = PdfReader(filename)
            num = len(file.pages)
            
            for idx in range(num):
                page = file.pages[idx]
                out.add_page(page)
                
            #password
            out.encrypt(code)
            
            with open(protectfile, "wb") as f:
                out.write(f)
            
            source.set("")
            target.set("")
            password.set("")
            
            messagebox.showinfo("info","Successfully done!!")
            
        
        except:
            messagebox.showerror("Invalid","Invaild Entry!!")
        
#icon
image_icon=PhotoImage(file="images/freepdfpasswordprotector_icon.png")
root.iconphoto(False,image_icon)

#mamin
Top_image=PhotoImage(file="images/jayesh.png")
Label(root,image=Top_image).pack()

frame=Frame(root,width=580,height=290,bd=5,relief=GROOVE)
frame.place(x=10,y=130)

######
source=StringVar()
Label(frame,text="Source PDF File:",font="arial 10 bold",fg="#4c4542").place(x=30,y=50)
entry1=Entry(frame,width=30,textvariable=source,font="arial 15",bd=1)
entry1.place(x=150,y=48)

Button_icon=PhotoImage(file="images/browse.png")
Button(frame,image=Button_icon,width=35,height=24,bg="#d3cdcd",command=browse).place(x=500,y=47)
 
######
target=StringVar()
Label(frame,text="Target PDF File:",font="arial 10 bold",fg="#4c4542").place(x=30,y=100)
entry2=Entry(frame,width=30,textvariable=target,font="arial 15",bd=1)
entry2.place(x=150,y=100)

######
password=StringVar()
Label(frame,text="Set User Password:",font="arial 10 bold",fg="#4c4542").place(x=15,y=150)
entry3=Entry(frame,width=30,textvariable=password,font="arial 15",bd=1)
entry3.place(x=150,y=150)


button_icon=PhotoImage(file="images/iconbutton.png")
Protect=Button(root,text="Protect PDF File",compound=LEFT,image=button_icon,width=230,height=50,bg="#bfb9b9",font="arial 14 bold",command=Protect)
Protect.pack(side=BOTTOM,pady=40)



root.mainloop()
