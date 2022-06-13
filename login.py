from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from Hotel import HotelManagementSystem 

class Login_winhdow:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Akash Kumar\Desktop\hotel manage\img2.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)
    
        
        ######## frame #######
        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)
        
        img1=Image.open(r"C:\Users\Akash Kumar\Desktop\hotel manage\account.png")
        img1=img1.resize((90,90),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbl_img1=Label(frame,image=self.photoimage1,bg="black",bd=0)
        lbl_img1.place(x=120,y=20)
        
        
        ##### label and entry #####
        get_wel=Label(frame,text="Welcome",font=("times new roman",20,"bold"),fg="white",bg="black",bd=0)
        get_wel.place(x=95,y=102)
        
        self.user_entry=StringVar()
        user=Label(frame,text="Username",font=("times new roman",20,"bold"),fg="white",bg="black",bd=0)
        user.place(x=95,y=130,width=130,height=100)
        user_entry=ttk.Entry(frame,textvariable=self.user_entry,font=("times new roman",15,"bold"))
        user_entry.place(x=70,y=190)
        
        self.password_entry=StringVar()
        password=Label(frame,text="Password",font=("times new roman",20,"bold"),fg="white",bg="black",bd=0)
        password.place(x=95,y=230)
        password_entry=ttk.Entry(frame,textvariable= self.password_entry,show="*",font=("times new roman",15,"bold"))
        password_entry.place(x=70,y=260)
        
        ######username icon image#####
        img2=Image.open(r"C:\Users\Akash Kumar\Desktop\hotel manage\account.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(frame,image=self.photoimage2,bg="black",bd=0)
        lbl_img2.place(x=68,y=163)
        
        ##########password icon image #######
        img3=Image.open(r"C:\Users\Akash Kumar\Desktop\hotel manage\password icon.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(frame,image=self.photoimage3,bg="black",bd=0)
        lbl_img3.place(x=68,y=233)
        
        ########## Login Button #######
        lgnbtn=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bg="blue",fg="white",bd=2,activeforeground="white",activebackground="blue")
        lgnbtn.place(x=128,y=305)
        
        ########## register Button #######
        registerbtn=Button(frame,text="New User Registeration",font=("times new roman",15,"bold"),bg="black",fg="white",bd=0,activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=350)
        
        ########## forget Button #######
        forgetbtn=Button(frame,text="Forget Password",font=("times new roman",15,"bold"),bg="black",fg="white",bd=0,activeforeground="white",activebackground="black")
        forgetbtn.place(x=10,y=380)
        
        ######## work on Login button ######
    def login(self):
        if self.user_entry.get()=="" and self.password_entry.get()=="":
            messagebox.showerror("Error","All Fields are required")
        elif self.user_entry.get()=="Akash" and self.password_entry.get()=="12345":
            self.new_window=(Toplevel(self.root))
            self.app=HotelManagementSystem(self.new_window)
           # messagebox.showinfo("Successs","Welcome to our Hotel Regency",parent=self.root)
        else:
            messagebox.showwarning("Warning","Invalid username & password",parent=self.root)
                
                
                
if __name__ == '__main__':
    root=Tk()
    obj=Login_winhdow(root)
    root.mainloop()
    