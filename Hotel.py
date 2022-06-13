#from _typeshed import Self
from tkinter import*
from tkinter.font import BOLD
from PIL import Image,ImageTk
from customer import Cust_win
import time
from Room import RoomBooking
from details import Details
from report import Report




class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management Stystem")
        self.root.geometry("1550x800+0+0")
    
    ######### 1st image ############
        img1=Image.open(r"C:\Users\Akash Kumar\Desktop\hotel manage\DUBAI.jpg")
        img1=img1.resize((1550,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=1550,height=140)

    ####### logo ##############
        img2=Image.open(r"C:\Users\Akash Kumar\Desktop\hotel manage\logo4.jpg")
        img2=img2.resize((230,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=230,height=140)
    
    ######## title ############
        lbl_title=Label(self.root,text="TRAVEL MANAGEMENT SYSTEM", font=("tiems new version",40,BOLD),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)
    
    ######## main frame ########
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=640)
        

    ####### menu ###############
        lbl_menu=Label(main_frame,text="MENU", font=("tiems new version",40,BOLD),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230,height=50)
    
    
    ####### Btn_frame###########
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=50,width=228,height=210)
        
    ####### btn in btn_frame ####
        cust_btn=Button(btn_frame,text="CUSTOMER",width=22, command=self.cust_details,font=("times new roman",14,BOLD),bg="black",fg="gold",bd=3,relief=RIDGE)
        cust_btn.grid(row=0,column=0,pady=1) 
        
        room_btn=Button(btn_frame,text="ROOM",width=22,command=self.Room_detail,font=("times new roman",14,BOLD),bg="black",fg="gold",bd=3,relief=RIDGE)
        room_btn.grid(row=1,column=0,pady=1) 
        
        detail_btn=Button(btn_frame,text="DETAIL",width=22,command=self.bookdetail,font=("times new roman",14,BOLD),bg="black",fg="gold",bd=3,relief=RIDGE)
        detail_btn.grid(row=2,column=0,pady=1) 
        
        report_btn=Button(btn_frame,text="REPORT",width=22,command=self.reporthere,font=("times new roman",14,BOLD),bg="black",fg="gold",bd=3,relief=RIDGE)
        report_btn.grid(row=3,column=0,pady=1) 
        
        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,BOLD),bg="black",fg="gold",bd=3,relief=RIDGE)
        logout_btn.grid(row=4,column=0,pady=1) 
        
    ######## right image ##########

        img3=Image.open(r"\Users\Akash Kumar\Desktop\hotel manage\img1.jpg")
        img3=img3.resize((1310,650),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lbling=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lbling.place(x=225,y=0,width=1320,height=650)
        
    ####### down image #############
        img4=Image.open(r"\Users\Akash Kumar\Desktop\hotel manage\img3.jpg")
        img4=img4.resize((230,210),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lbling1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lbling1.place(x=0,y=260,width=228,height=180)

        img5=Image.open(r"C:\Users\Akash Kumar\Desktop\hotel manage\img4.jpg")
        img5=img5.resize((230,210),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        lbling2=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lbling2.place(x=0,y=410,width=228,height=180)

    

    
    ######### func of customer.py ##########
    def cust_details(self):
        self.new_window=(Toplevel(self.root))
        self.app=Cust_win(self.new_window)
        
    ######### func of Room.py ##########
    def Room_detail(self):
        self.new_window=(Toplevel(self.root))
        self.app=RoomBooking(self.new_window)
    
    ######### func of details.py ##########
    def bookdetail(self):
        self.new_window=(Toplevel(self.root))
        self.app=Details(self.new_window)
    ########### fuct on report ########
    def reporthere(self):
        self.new_window=(Toplevel(self.root))
        self.app=Report(self.new_window)
    
    ############  working on Logout Button #######
    def logout(self):
        self.root.destroy()
            
        






if __name__=="__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()