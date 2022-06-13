from tkinter import*
from typing import ValuesView
from PIL import Image,ImageTk
from tkinter import ttk
import random
import pymysql
from tkinter import messagebox 


class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Travel Management System")
        self.root.geometry("1293x565+232+220")
        
    ########### variable ##########
    
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        self.var_address=StringVar()
        
    
    ######### title ################
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new version",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1293,height=60)
    
    ######### logo #################
        img1=Image.open(r"C:\Users\Akash Kumar\Desktop\hotel manage\logo4.jpg")
        img1=img1.resize((100,40),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=5,y=2,width=100,height=58)
    
    
    ########## label frame ##########
        labelframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman",12,"bold"),padx=2)
        labelframe.place(x=5,y=55,width=425,height=490)
    
    ########## labels and entries #####

        lbl_cust_ref=Label(labelframe,text="Customer Ref:", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0)
        entry_ref=ttk.Entry(labelframe,width=22,textvariable=self.var_ref,font=("times new roman",12,"bold"))
        entry_ref.grid(row=0,column=1)
                       
        cname=Label(labelframe,text="Customer Name:", font=("tiems new version",12,"bold"),padx=2,pady=6)
        cname.grid(row=1 ,column=0)
        txtcname=ttk.Entry(labelframe,width=22,textvariable=self.var_cust_name,font=("times new roman",12,"bold"))
        txtcname.grid(row=1,column=1)
        
        lblmname=Label(labelframe,text="Mother's Name:", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0)
        txtmname=ttk.Entry(labelframe,width=22,textvariable=self.var_mother,font=("times new roman",12,"bold"))
        txtmname.grid(row=2,column=1)
    
        lbl_gender=Label(labelframe,text="Gender:", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0)
        combo_gender=ttk.Combobox(labelframe,textvariable=self.var_gender,font=("arial",12,"bold"),width=18,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

    
        lblmobile=Label(labelframe,text="Mobile:",font=("tiems new version",12,"bold"),padx=2,pady=6)
        lblmobile.grid(row=4,column=0)
        txtmobile=ttk.Entry(labelframe,width=22,textvariable=self.var_mobile,font=("times new roman",12,"bold"))
        txtmobile.grid(row=4,column=1)
        
        lblemail=Label(labelframe,text="Email:", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=5,column=0)
        txtemail=ttk.Entry(labelframe,width=22,textvariable=self.var_email,font=("times new roman",12,"bold"))
        txtemail.grid(row=5,column=1)

        lblNatinality=Label(labelframe,text="Natinality:", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lblNatinality.grid(row=6,column=0)
        combo_nationality=ttk.Combobox(labelframe,textvariable=self.var_nationality,font=("arial",12,"bold"),width=18,state="readonly")
        combo_nationality["value"]=("Indian","American","British")
        combo_nationality.current(0)
        combo_nationality.grid(row=6,column=1)
        
        lblIdproof=Label(labelframe,text="Idproof:", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lblIdproof.grid(row=7,column=0)
        combo_Idproof=ttk.Combobox(labelframe,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=18)
        combo_Idproof["value"]=("Adharcard","Drivinglicence","Passport")
        combo_Idproof.current(0)
        combo_Idproof.grid(row=7,column=1)
        
        lblIdnumber=Label(labelframe,text="Idnumber:", font=("tiems new version",12,"bold"),padx=2,pady=6)
        lblIdnumber.grid(row=8,column=0)
        txtidnumber=ttk.Entry(labelframe,width=22,textvariable=self.var_id_number,font=("times new roman",12,"bold"))
        txtidnumber.grid(row=8,column=1)
        
        
        
        lblAddress=Label(labelframe,text="Address:",font=("tiems new version",12,"bold"),padx=2,pady=6)
        lblAddress.grid(row=9,column=0)
        txtAddress=ttk.Entry(labelframe,width=22,textvariable=self.var_address,font=("times new roman",12,"bold"))
        txtAddress.grid(row=9,column=1)
        
        
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
        
        
        ##############Table frame ###########
        Table_frame=LabelFrame(self.root,text="View details and Search System",font=("arial",12,"bold"))
        Table_frame.place(x=435,y=52,width=860,height=494)
        lblSearch=Label(Table_frame,text="Search By",font=("arial",12,"bold"),bg="red",fg="white")
        lblSearch.grid(row=0,column=0,sticky=W)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_frame,textvariable=self.search_var,width=24,font=("arial",12,"bold"),state="readonly")
        combo_search["value"]=("Mobile","Ref")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_frame,textvariable=self.txt_search,width=24,font=("arial",12,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(Table_frame,text="Search",command=self.search,width=7,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        btnSearch.grid(row=0,column=3,padx=2) 
        
        btnShow=Button(Table_frame,text="Show All",width=7,command=self.fetch_data,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        btnShow.grid(row=0,column=4,padx=2) 
        
        ############# Show data Table ###########
        detail_table=Frame(Table_frame,bd=2,relief=RIDGE)
        detail_table.place(x=0,y=50,width=860,height=350)
        
        scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)
        self.cust_detail_table=(ttk.Treeview(detail_table,column=("ref","name","mother","gender","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set))
        scroll_x.pack(side=BOTTOM,fill=X)        
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.cust_detail_table.xview) 
        scroll_y.config(command=self.cust_detail_table.yview)  
        
        ############# view Table ###############
        
        self.cust_detail_table.heading("ref",text="Ref No") 
        self.cust_detail_table.heading("name",text="Customer Name")  
        self.cust_detail_table.heading("mother",text="Moteher Name")  
        self.cust_detail_table.heading("gender",text="Gender")         
        self.cust_detail_table.heading("mobile",text="Mobile")  
        self.cust_detail_table.heading("email",text="Email")  
        self.cust_detail_table.heading("nationality",text="Natinality")  
        self.cust_detail_table.heading("idproof",text="IdProof")  
        self.cust_detail_table.heading("idnumber",text="Idnumber")  
        self.cust_detail_table.heading("address",text="Address")
        self.cust_detail_table["show"]="headings"  
        
        self.cust_detail_table.column("ref",width=100) 
        self.cust_detail_table.column("name",width=100)  
        self.cust_detail_table.column("mother",width=100)  
        self.cust_detail_table.column("gender",width=100)    
        self.cust_detail_table.column("mobile",width=100)  
        self.cust_detail_table.column("email",width=100) 
        self.cust_detail_table.column("nationality",width=100) 
        self.cust_detail_table.column("idproof",width=100) 
        self.cust_detail_table.column("idnumber",width=100) 
        self.cust_detail_table.column("address",width=100) 
      #  self.cust_detail_table.column("address",width=100)
        
        self.cust_detail_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.cust_detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        
    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="" or self.var_cust_name.get()=="" or self.var_email.get()=="" or self.var_id_number.get()=="" or self.var_address.get()=="":
            messagebox.showerror("Error","All field are required",parent=self.root)
        
        else:
            try:
                conn=pymysql.connect(host="localhost", port=3306,user="root",passwd="",database="project1")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO `customer` (ref, name, mother, gender, mobile, email, nationality, idproof, idnumber, address) VALUES('"+self.var_ref.get()+"', '"+self.var_cust_name.get()+"','"+self.var_mother.get()+"','"+self.var_gender.get()+"','"+self.var_mobile.get()+"','"+self.var_email.get()+"','"+self.var_nationality.get()+"','"+self.var_id_proof.get()+"','"+self.var_id_number.get()+"','"+self.var_address.get()+"')")
                
                conn.commit()
                self.fetch_data()
                conn.close()
                print("weldone") 
                messagebox.showinfo("Success","customer has been added successfully",parent=self.root)
                
            except Exception as es:
                messagebox.showwarning("warning","Something went wrong:{str(es)}",parent=self.root)
                         
    
    #ref, name, mother, gender, mobile, email, nationality, idproof, idnumber, address
 
    #'"+self.var_ref.get()+", "+self.var_cust_name.get()+","+self.var_mother.get()+","+self.var_gender.get()+","+self.var_mobile.get()+","+self.var_email.get()+","+self.var_nationality.get()+","+self.var_id_proof.get()+","+self.var_id_number.get()+","+self.var_address.get()+" '

    def fetch_data(self):
        conn=pymysql.connect(host="localhost", port=3306,user="root",passwd="",database="project1")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM customer")
        rows=my_cursor.fetchall()
        if len(rows) >=0:
            self.cust_detail_table.delete(*self.cust_detail_table.get_children())
            
        for i in rows:
            self.cust_detail_table.insert("",END,values=i)
            conn.commit()
        conn.close()
            
    ###### after click on the put data into customner detail ######
     
    def get_cursor(self,event=""):
        cursor_row=self.cust_detail_table.focus()
        content=self.cust_detail_table.item(cursor_row)
        row=content["values"]
        
        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_mobile.set(row[4])
        self.var_email.set(row[5])
        self.var_nationality.set(row[6])
        self.var_id_proof.set(row[7])
        self.var_id_number.set(row[8])
        self.var_address.set(row[9])
   # note3-after this bind the data in treeview table
   
   ####### update the data #########
    def update(self):
        if self.var_mobile=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)
            
        else:
            conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="project1")
            my_cursor=conn.cursor()
            str="UPDATE `customer` SET `name`= '"+self.var_cust_name.get()+"', `mother`= '"+self.var_mother.get()+"', `gender`= '"+self.var_gender.get()+"', `mobile`= '"+self.var_mobile.get()+"', `email`= '"+self.var_email.get()+"', `nationality`= '"+self.var_nationality.get()+"', `idproof`= '"+self.var_id_proof.get()+"', `idnumber`=  '"+self.var_id_number.get()+"', `address`= '"+self.var_address.get()+"' WHERE `ref`=  '"+self.var_ref.get()+"'"
            my_cursor.execute(str)                                                                                                                                                        
    
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","customer updated successfully",parent=self.root)
            #note4-after this give the command to update button
            
    ########## WORKING ON DELETE BUTTON ############
    
    def delete(self):
        Delete=messagebox.askyesno("Hotel Management System", "Do ypu want to delete",parent=self.root)
        
        if Delete>0:
           # print("yes not-----",self.var_ref.get())
            conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="project1")
            my_cursor=conn.cursor()
            query="delete from customer where Ref='"+self.var_ref.get()+"'"
            my_cursor.execute(query)
            conn.commit()
            
        else:
            if not Delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
            
    def reset(self):
        self.var_ref.set("")
        self.var_cust_name.set("")
        self.var_mother.set("")
      #  self.var_gender.set("")
        self.var_mobile.set("")
        self.var_email.set("")
      #  self.var_nationality.set("")
     #   self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        
        
    ######## work on search  & search all #######
    
    def search(self):
         print(str(self.search_var.get()),self.txt_search.get())
         conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",database="project1")
         my_cursor=conn.cursor()
         
         my_cursor.execute("select * from `customer` where `Ref`='"+str(self.txt_search.get())+"' or `Mobile`='"+str(self.txt_search.get())+"'")
         
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             print("test")
             self.cust_detail_table.delete(*self.cust_detail_table.get_children())
         for i in rows:
             self.cust_detail_table.insert("",END,values=i)
         conn.commit()
         conn.close()
        
        
            
        
            
    


        
    
        
        
        


if __name__ == '__main__':
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()
    