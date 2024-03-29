from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import pypyodbc as odbc
class orderclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry(self.get_window_geometry())
        self.root.title("Inventory Management System")
        self.root.config(bg = "white")
        self.root.focus_force()
        #-----------------------variables---------------------
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        
        self.var_oid=int
        self.var_cid=int
        self.var_price = int
        self.var_quantity = int
        self.product_list=[]
        #self.fetch_products()

        order_Frame=Frame(self.root,bd=5,relief=RIDGE,bg="white")
        order_Frame.place(x=10,y=150,width=500,height=550)

        product_line_title  = Label(order_Frame,text = "MANAGE ORDER DETAILS",font = ("Bahnschrift Light Condensed",15,"bold"),bg = "black",fg = "white").pack(side=TOP,fill=X)
        #customer id
        label_cid  = Label(order_Frame,text = "CUSTOMER ID",font = ("Bahnschrift Light Condensed",14),fg="black").place(x=30,y=110)
        #price
        label_price  = Label(order_Frame,text = "PRICE",font = ("Bahnschrift Light Condensed",14,),fg="black").place(x=30,y=180)
        #products
        label_products  = Label(order_Frame,text = "PRODUCTS",font = ("Bahnschrift Light Condensed",14),fg="black").place(x=30,y=250)
        #quantity
        label_quantity  = Label(order_Frame,text = "QUANTITY",font = ("Bahnschrift Light Condensed",14),fg="black").place(x=30,y=310)

        #price textbox
        txt_price = Entry(order_Frame,textvariable=self.var_price,font=("Bahnschrift Light Condensed",12,"bold"),bg ='white').place(x=150,y=180,width=200)
        #quantity textbox
        txt_quantity= Entry(order_Frame,textvariable=self.var_quantity,font=("Bahnschrift Light Condensed",12,"bold"),bg ='white').place(x=150,y=310,width=200)
        
    def get_window_geometry(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = int(screen_width * 0.86)
        window_height = int(screen_height * 0.8)
        window_x = int((screen_width - window_width) / 2)
        window_y = int((screen_height - window_height) / 2)
        return f"{window_width}x{window_height}+{window_x}+{window_y}"
if __name__ == "__main__":
   root = Tk()
   obj = orderclass(root)
   root.mainloop()