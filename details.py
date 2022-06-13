from tkinter import*
from typing import ValuesView
from PIL import Image,ImageTk
from tkinter import ttk
import random
import pymysql
from tkinter import messagebox 


class Details:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1293x565+232+220")
        
  
    ######### title ################
        lbl_title=Label(self.root,text="BOOKING DETAILS",font=("times new version",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1293,height=60)
    
    ######### logo #################
        img1=Image.open(r"C:\Users\Akash Kumar\Desktop\hotel manage\logo4.jpg")
        img1=img1.resize((100,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=58)
        
    ########## label frame ##########
        labelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add Details",font=("times new roman",12,"bold"),padx=2)
        labelframe.place(x=5,y=70,width=450,height=350)
        
    ########## images ##########
        img1=Image.open(r"C:\Users\Akash Kumar\Desktop\hotel manage\bed1.jpg")
        img1=img1.resize((150,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbling=Label(labelframe,image=self.photoimg1,bd=0,relief=RIDGE)
        lbling.grid(row=0,column=0)
        
        img2=Image.open(r"C:\Users\Akash Kumar\Desktop\hotel manage\bed2.jpg")
        img2=img2.resize((150,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lbling=Label(labelframe,image=self.photoimg2,bd=0,relief=RIDGE)
        lbling.grid(row=0,column=1,sticky=W)
        
        img3=Image.open(r"C:\Users\Akash Kumar\Desktop\hotel manage\bed1.jpg")
        img3=img3.resize((150,100),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lbling=Label(labelframe,image=self.photoimg3,bd=0,relief=RIDGE)
        lbling.grid(row=0,column=2,sticky=W)
        
      
        
    
     ########## labels and entries #####

        lbl_floor=Label(labelframe,text="Floor", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=1,column=0)
        
        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframe,width=22,textvariable=self.var_floor,font=("times new roman",12,"bold"))
        entry_floor.grid(row=1,column=1,sticky=W)
                       
        RoomNO=Label(labelframe,text="RoomNo", font=("tiems new version",12,"bold"),padx=2,pady=6)
        RoomNO.grid(row=2 ,column=0)
        
        self.var_roomno=StringVar()
        entry_room=ttk.Entry(labelframe,width=22,textvariable=self.var_roomno,font=("times new roman",12,"bold"))
        entry_room.grid(row=2,column=1,sticky=W)
        
        lbl_Roomtype=Label(labelframe,text="RoomType", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lbl_Roomtype.grid(row=3,column=0)
        
        self.var_roomtype=StringVar()
        combo_roomtype=ttk.Combobox(labelframe,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=18,state="readonly")
        combo_roomtype["value"]=("single","double","laxary")
        combo_roomtype.current(0)
        combo_roomtype.grid(row=3,column=1,sticky=W)
        
     ########### btn frame ################
        btn_frame=Frame(labelframe,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=250,width=412,height=40)
        
        
        btnAdd=Button(btn_frame,text="Add",width=7,command=self.add_data,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        btnAdd.grid(row=0,column=0,padx=7) 
        
        btnUpdate=Button(btn_frame,text="Update",width=7,command=self.update,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        btnUpdate.grid(row=0,column=1,padx=7) 
        
        btnDelete=Button(btn_frame,text="Delete",width=7,command=self.delete,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        btnDelete.grid(row=0,column=2,padx=7) 
        
        btnReset=Button(btn_frame,text="Reset",width=7,command=self.reset,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        btnReset.grid(row=0,column=3,pady=7) 
    
    ########### Room_deatil frame ################
        Room_frame=LabelFrame(self.root,text="Show Room Details",font=("times new roman",12,"bold"),padx=2)
        Room_frame.place(x=500,y=70,width=480,height=350)
        
        scroll_x=ttk.Scrollbar(Room_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Room_frame,orient=VERTICAL)
        self.room_detail_table=(ttk.Treeview(Room_frame,column=("floor","roomno.","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set))
        scroll_x.pack(side=BOTTOM,fill=X)        
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.room_detail_table.xview) 
        scroll_y.config(command=self.room_detail_table.yview) 
        
      ############# view Table ###############
        
        self.room_detail_table.heading("floor",text="Floor") 
        self.room_detail_table.heading("roomno.",text="RoomNo")  
        self.room_detail_table.heading("roomtype",text="RoomType")  
        self.room_detail_table["show"]="headings" 
        
        self.room_detail_table.column("floor",width=100) 
        self.room_detail_table.column("roomno.",width=100)  
        self.room_detail_table.column("roomtype",width=100)  
        self.room_detail_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.room_detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
    ########### connection to database ##########    
    def add_data(self):
        if  self.var_floor.get()=="" or self.var_roomtype.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        
        else:
            try:
                print("hello")
                conn=pymysql.connect(host="localhost", port=3306,user="root",passwd="",database="project1")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO `detail` (floor, roomno, roomtype) VALUES('"+self.var_floor.get()+"', '"+self.var_roomno.get()+"','"+self.var_roomtype.get()+"')")
                
                conn.commit()
                self.fetch_data()
                conn.close()
                print("weldone") 
                messagebox.showinfo("Success","Room has been added successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showwarning("warning","Something went wrong:{str(es)}",parent=self.root)
    
    ######## fetch data  from database ################  
    def fetch_data(self):
        conn=pymysql.connect(host="localhost", port=3306,user="root",passwd="",database="project1")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM detail")
        rows=my_cursor.fetchall()
        if len(rows) !=0:
            self.room_detail_table.delete(*self.room_detail_table.get_children())
            
        for i in rows:
            self.room_detail_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    ######## get cursor ##########
    def get_cursor(self,event=""):
        cursor_row=self.room_detail_table.focus()
        content=self.room_detail_table.item(cursor_row)
        row=content["values"]
        
        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])
    # note3-after this bind the data in treeview table
    
    
     ####### update the data #########
    def update(self):
        if self.var_floor=="":
            messagebox.showerror("Error","Please enter floor number",parent=self.root)
            
        else:
            conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="project1")
            my_cursor=conn.cursor()
            str="UPDATE `detail` SET  `roomno`= '"+self.var_roomno.get()+"', `roomtype`= '"+self.var_roomtype.get()+"' WHERE `floor`= '"+self.var_floor.get()+"'"
            my_cursor.execute(str)                                                                                                                                                        
    
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","Room Detail updated successfully",parent=self.root)
            #note4-after this give the command to update button
            
     ########## WORKING ON DELETE BUTTON ############
    
    def delete(self):
        Delete=messagebox.askyesno("Hotel Management System", "Do ypu want to delete",parent=self.root)
        
        if Delete>0:
           # print("yes not-----",self.var_ref.get())
            conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="project1")
            my_cursor=conn.cursor()
            query="delete from detail where floor='"+self.var_floor.get()+"'"
            my_cursor.execute(query)
            conn.commit()
            
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
     #note4-after this give the command to delete button
     
     
     ######### Reset button ##########
    def reset(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("")
    #note4-after this give the command to delete button
      
        
        
        
        
        
        
        
        
        
    
        



if __name__ == '__main__':
    root=Tk()
    obj=Details(root)
    root.mainloop()
    