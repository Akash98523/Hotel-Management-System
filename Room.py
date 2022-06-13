from tkinter import*
from typing import ValuesView
from PIL import Image,ImageTk
from tkinter import ttk
import random
import pymysql
from tkinter import messagebox 
from time import strptime
from datetime import datetime


class RoomBooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1293x565+232+220")
        
    ########## variables ###############
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_available=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_subtotal=StringVar()
        self.var_totalcost=StringVar()
        
        
    ######### title ################
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new version",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1293,height=50)
    
     ######### logo #################
        img1=Image.open(r"C:\Users\Akash Kumar\Desktop\hotel manage\logo4.jpg")
        img1=img1.resize((100,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=48)
    ########## label frame ##########
        labelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Booking Details",font=("times new roman",12,"bold"),padx=2)
        labelframe.place(x=5,y=55,width=425,height=490)
    
    ########## labels and entries #####
        #customer contact
        lbl_cust_contact=Label(labelframe,text="Customer contact", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(labelframe,width=22,textvariable=self.var_contact,font=("times new roman",12,"bold"))
        entry_ref.grid(row=0,column=1,sticky=W)
        #fetch button
        btnfetchdata=Button(labelframe,text="fetch data",command=self.fetch_data,font=("arial",9,"bold"),bg="black",fg="gold",width=9)
        btnfetchdata.grid(row=0,column=2)
        
        #check_in_date               
        check_in_date=Label(labelframe,text="check_in_date", font=("tiems new version",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1 ,column=0)
        txtcname=ttk.Entry(labelframe,width=22,textvariable=self.var_checkin,font=("times new roman",12,"bold"))
        txtcname.grid(row=1,column=1,sticky=W)
        
        #check_out_date
        check_out_date=Label(labelframe,text=" check_out_date", font=("tiems new version",12,"bold"),padx=2,pady=6)
        check_out_date.grid(row=2 ,column=0)
        txtcname=ttk.Entry(labelframe,width=22,textvariable=self.var_checkout,font=("times new roman",12,"bold"))
        txtcname.grid(row=2,column=1,sticky=W)
        
        #Room Type
        lbl_RoomType=Label(labelframe,text="Room Type", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=3,column=0)
        
        conn=pymysql.connect(host="localhost", port=3306,user="root",passwd="",database="project1")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT roomtype FROM detail")
        rows=my_cursor.fetchall()
        combo_RoomType=ttk.Combobox(labelframe,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=18,state="readonly")
        combo_RoomType["value"]=rows
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1,sticky=W)
        
        #Available Room
        lbl_RoomAvailable=Label(labelframe,text="Available Room", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lbl_RoomAvailable.grid(row=4,column=0)
        #entry_room=ttk.Entry(labelframe,width=22,textvariable=self.var_available,font=("times new roman",12,"bold"))
       # entry_room.grid(row=4,column=1,sticky=W)
       
        conn=pymysql.connect(host="localhost", port=3306,user="root",passwd="",database="project1")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT roomno FROM detail")
        rows=my_cursor.fetchall()
        
        combo_RoomType=ttk.Combobox(labelframe,textvariable=self.var_available,font=("arial",12,"bold"),width=18,state="readonly")
        combo_RoomType["value"]=rows
        combo_RoomType.current(0)
        combo_RoomType.grid(row=4,column=1,sticky=W)
        
       #Meal
        lbl_Meal=Label(labelframe,text="Meal", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lbl_Meal.grid(row=5,column=0)
        entry_meal=ttk.Entry(labelframe,width=22,textvariable=self.var_meal,font=("times new roman",12,"bold"))
        entry_meal.grid(row=5,column=1,sticky=W)
        
        #No of days               
        lblnodays=Label(labelframe,text="No of days", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lblnodays.grid(row=6 ,column=0)
        txtdays=ttk.Entry(labelframe,width=22,textvariable=self.var_noofdays,font=("times new roman",12,"bold"))
        txtdays.grid(row=6,column=1,sticky=W)
        
        #Paid Tax
        lblpaidtax=Label(labelframe,text="Paid Tax", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lblpaidtax.grid(row=7,column=0)
        txtpaidtax=ttk.Entry(labelframe,width=22,textvariable=self.var_paidtax,font=("times new roman",12,"bold"))
        txtpaidtax.grid(row=7,column=1,sticky=W)
        
        #Sub Total
        lbl_subtotal=Label(labelframe,text="Sub Total", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lbl_subtotal.grid(row=8,column=0)
        txtsubtotal=ttk.Entry(labelframe,width=22,textvariable=self.var_subtotal,font=("times new roman",12,"bold"))
        txtsubtotal.grid(row=8,column=1,sticky=W)
        
        #Total cost
        lbl_totalcost=Label(labelframe,text="Total_cost", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lbl_totalcost.grid(row=9,column=0)
        txttotalcost=ttk.Entry(labelframe,width=22,textvariable=self.var_totalcost,font=("times new roman",12,"bold"))
        txttotalcost.grid(row=9,column=1,sticky=W)
    
        #bill btn
        btnBill=Button(labelframe,text="Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,sticky=W)
        
        # Add, Update,delete,reset button
     ########### btn frame ################
        btn_frame=Frame(labelframe,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        
        
        btnAdd=Button(btn_frame,text="Add",width=7,command=self.add_data,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        btnAdd.grid(row=0,column=0,padx=7) 
        
        btnUpdate=Button(btn_frame,text="Update",width=7,command=self.update,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        btnUpdate.grid(row=0,column=1,padx=7) 
        
        btnDelete=Button(btn_frame,text="Delete",width=7,command=self.delete,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        btnDelete.grid(row=0,column=2,padx=7) 
        
        btnReset=Button(btn_frame,text="Reset",width=7,command=self.reset,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        btnReset.grid(row=0,column=3,pady=7) 
        
        
    ######## Right image ############

        img1=Image.open(r"C:\Users\Akash Kumar\Desktop\hotel manage\bed.jpg")
        img1=img1.resize((500,250),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=800,y=49,width=500,height=250)
        
    
     ##############Table frame ###########
        Table_frame=LabelFrame(self.root,text="View details and Search System",font=("arial",12,"bold"))
        Table_frame.place(x=435,y=245,width=860,height=494)
        lblSearch=Label(Table_frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearch.grid(row=0,column=0,sticky=W)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_var,width=24,font=("arial",12,"bold"),state="readonly")
        combo_search["value"]=("contact")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_frame,textvariable=self.txt_search,width=24,font=("arial",12,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_frame,text="Search",width=7,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        btnSearch.grid(row=0,column=3,padx=2) 
        
        btnShow=Button(Table_frame,text="Show All",width=7,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        btnShow.grid(row=0,column=4,padx=2)     
        
    
     ############# Show data Table ###########
        detail_table=Frame(self.root,bd=2,relief=RIDGE)
        detail_table.place(x=430,y=300,width=860,height=250)
        
        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)
        self.room_detail_table=(ttk.Treeview(detail_table,column=("customer_contact","check_in_date","check_out_date","room_type","available_room","meal","no_of_days","paid_tax","sub_total","total_cost"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set))
        scroll_x.pack(side=BOTTOM,fill=X)        
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_detail_table.xview) 
        scroll_y.config(command=self.room_detail_table.yview)  
        
        ############# view Table ###############
        
        self.room_detail_table.heading("customer_contact",text="Customer_contact") 
        self.room_detail_table.heading("check_in_date",text="Check_in_date")  
        self.room_detail_table.heading("check_out_date",text="Check_out_date")  
        self.room_detail_table.heading("room_type",text="Room_type")         
        self.room_detail_table.heading("available_room",text="Available_room")  
        self.room_detail_table.heading("meal",text="Meal")  
        self.room_detail_table.heading("no_of_days",text="No_of_days")  
        self.room_detail_table.heading("paid_tax",text="Paid_tax")  
        self.room_detail_table.heading("sub_total",text="Sub_total")  
        self.room_detail_table.heading("total_cost",text="Total_cost")
        self.room_detail_table["show"]="headings" 
        
        self.room_detail_table.column("customer_contact",width=100) 
        self.room_detail_table.column("check_in_date",width=100)  
        self.room_detail_table.column("check_out_date",width=100)  
        self.room_detail_table.column("room_type",width=100)    
        self.room_detail_table.column("available_room",width=100)  
        self.room_detail_table.column("meal",width=100) 
        self.room_detail_table.column("no_of_days",width=100) 
        self.room_detail_table.column("paid_tax",width=100) 
        self.room_detail_table.column("sub_total",width=100) 
        self.room_detail_table.column("total_cost",width=100) 
        
        self.room_detail_table.pack(fill=BOTH,expand=1)
        self.fetch_data1()
        self.room_detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        
    ########### connection to database ##########    
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        
        else:
            try:
                print("hello")
                conn=pymysql.connect(host="localhost", port=3306,user="root",passwd="",database="project1")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO `room` (contact, checkin, checkout, roomtype,available, meal,noofdays, paidtax, subtotal,totalcost) VALUES('"+self.var_contact.get()+"', '"+self.var_checkin.get()+"','"+self.var_checkout.get()+"','"+self.var_roomtype.get()+"','"+self.var_available.get()+"','"+self.var_meal.get()+"','"+self.var_noofdays.get()+"','"+self.var_paidtax.get()+"','"+self.var_subtotal.get()+"','"+self.var_totalcost.get()+"')")
                
                conn.commit()
                self.fetch_data1()
                conn.close()
                print("weldone") 
                messagebox.showinfo("Success","customer has been added successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showwarning("warning","Something went wrong:{str(es)}",parent=self.root)
    
    
    def fetch_data1(self):
        conn=pymysql.connect(host="localhost", port=3306,user="root",passwd="",database="project1")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM room")
        rows=my_cursor.fetchall()
        if len(rows) !=0:
            self.room_detail_table.delete(*self.room_detail_table.get_children())
            
        for i in rows:
            self.room_detail_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
             
    ###### after click on the put data into customner detail ######
     
    def get_cursor(self,event=""):
        cursor_row=self.room_detail_table.focus()
        content=self.room_detail_table.item(cursor_row)
        row=content["values"]
        
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_available.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])
        self.var_paidtax.set(row[7])
        self.var_subtotal.set(row[8])
        self.var_totalcost.set(row[9])
        
   # note3-after this bind the data in treeview table
                
    
    
        
    ## All fetch_data working#####
    
    def fetch_data(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please fill contact number")
        else:
            conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="project1")
            my_cursor=conn.cursor()
            
            query=("select name from customer where mobile='"+self.var_contact.get()+"'")
            my_cursor.execute(query)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","This number is not found",parent=self.root)
            else:
                
                conn.commit()
                conn.close()
                
                showDataframe=Frame(self.root,bd=4,relief=RIDGE)
                showDataframe.place(x=455,y=55,width=300,height=180)
                
                lblName=Label(showDataframe,text="Name",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)
                lblName=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lblName.place(x=80,y=0)
                
                ######## gender ##########
                conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="project1")
                my_cursor=conn.cursor()
                
                query=("select gender from customer where mobile='"+self.var_contact.get()+"'")
                my_cursor.execute(query)
                row=my_cursor.fetchone()
                
                lblgender=Label(showDataframe,text="gender",font=("arial",12,"bold"))
                lblgender.place(x=0,y=25)
                lblgender=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lblgender.place(x=80,y=25)
                
                ######## email ##########
                conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="project1")
                my_cursor=conn.cursor()
                
                query=("select email from customer where mobile='"+self.var_contact.get()+"'")
                my_cursor.execute(query)
                row=my_cursor.fetchone()
                
                lblgender=Label(showDataframe,text="email",font=("arial",12,"bold"))
                lblgender.place(x=0,y=50)
                lblgender=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lblgender.place(x=80,y=50)
                
                ######## nationality ##########
                conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="project1")
                my_cursor=conn.cursor()
                
                query=("select nationality from customer where mobile='"+self.var_contact.get()+"'")
                my_cursor.execute(query)
                row=my_cursor.fetchone()
                
                lblgender=Label(showDataframe,text="nationality",font=("arial",12,"bold"))
                lblgender.place(x=0,y=75)
                lblgender=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lblgender.place(x=80,y=75)
                
                ######## address ##########
                conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="project1")
                my_cursor=conn.cursor()
                
                query=("select address from customer where mobile='"+self.var_contact.get()+"'")
                my_cursor.execute(query)
                row=my_cursor.fetchone()
                
                lblgender=Label(showDataframe,text="address",font=("arial",12,"bold"))
                lblgender.place(x=0,y=100)
                lblgender=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lblgender.place(x=80,y=100)
                
                ######## id_number ##########
                conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="project1")
                my_cursor=conn.cursor()
                
                query=("select idnumber from customer where mobile='"+self.var_contact.get()+"'")
                my_cursor.execute(query)
                row=my_cursor.fetchone()
                
                lblgender=Label(showDataframe,text="idnumber",font=("arial",12,"bold"))
                lblgender.place(x=0,y=125)
                lblgender=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lblgender.place(x=80,y=125)
                
    ####### update the data #########
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
            
        else:
            conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="project1")
            my_cursor=conn.cursor()
            str="UPDATE `room` SET  `checkin`= '"+self.var_checkin.get()+"', `checkout`= '"+self.var_checkout.get()+"', `roomtype`= '"+self.var_roomtype.get()+"', `available`= '"+self.var_available.get()+"', `meal`= '"+self.var_meal.get()+"', `noofdays`= '"+self.var_noofdays.get()+"', `paidtax`=  '"+self.var_paidtax.get()+"', `subtotal`= '"+self.var_subtotal.get()+"', `totalcost`= '"+self.var_totalcost.get()+"' WHERE `contact`= '"+self.var_contact.get()+"' "
            my_cursor.execute(str)                                                                                                                                                        
    
            conn.commit()
            self.fetch_data1()
            conn.close()
            messagebox.showinfo("update","RoomBooking updated successfully",parent=self.root)
            #note4-after this give the command to update button
            
    ########## WORKING ON DELETE BUTTON ############
    
    def delete(self):
        Delete=messagebox.askyesno("Hotel Management System", "Do ypu want to delete",parent=self.root)
        
        if Delete>0:
           # print("yes not-----",self.var_ref.get())
            conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="project1")
            my_cursor=conn.cursor()
            query="delete from room where contact='"+self.var_contact.get()+"'"
            my_cursor.execute(query)
            conn.commit()
            
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data1()
        conn.close()
        
    ####### button Reset #######
    
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
       # self.var_roomtype.set("")
        self.var_available.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_subtotal.set("")
        self.var_totalcost.set("")
    
    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate))

        if (self.var_meal.get()=="breakfast" and self.var_roomtype=="laxary"):
            print("hii")
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            tax="Rs."+str("%.2f"%((q5)*.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(ST)
            self.var_totalcost.set(TT)
        
            
            
                
                
                
            
        
        

        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    root=Tk()
    obj=RoomBooking(root)
    root.mainloop()
    
    