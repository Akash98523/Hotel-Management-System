from tkinter import*
from typing import ValuesView
from PIL import Image,ImageTk
from tkinter import ttk
import random
import pymysql
from tkinter import messagebox 


class Report:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1293x565+232+220")
        
    
    ######## image ###########
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Akash Kumar\Desktop\hotel manage\query.png")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=20,y=0,relwidth=1,relheight=1)
        
        
        
if __name__ == '__main__':
    root=Tk()
    obj=Report(root)
    root.mainloop()