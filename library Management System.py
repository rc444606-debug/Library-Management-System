from tkinter import *
from tkinter import ttk
import mysql.connector



import tkinter
from tkinter import messagebox
import datetime

class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")

        self.member_var = StringVar()
        self.prn_no_var = StringVar()
        self.id_no_var = StringVar()
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.mobile_no_var = StringVar()
        self.book_id_var = StringVar()
        self.book_title_var = StringVar()
        self.Author_var=StringVar()
        self.date_borrowed_var = StringVar()
        self.date_due_var = StringVar()
        self.late_return_fine_var = StringVar()
        self.date_overdue_var = StringVar()
        self.actual_price_var = StringVar()

        #  -- Title ---
        lbltitle = Label(self.root, text="LIBRARY MANAGEMENT SYSTEM", bg="powder blue", 
                         fg="green", bd=20, relief=RIDGE, font=("times new roman", 50, "bold"), 
                         padx=2, pady=6)
        lbltitle.pack(side=TOP, fill=X)

        # --- Main Frame ---
        frame = Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)

        # --- Left Data Frame (LabelFrame is used for the title border) ---
        DataFrameLeft = LabelFrame(frame, text="Library Membership Information", fg="green", 
                                   bd=12, relief=RIDGE, bg="powder blue", 
                                   font=("times new roman", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        lblMembr = Label(DataFrameLeft, text="Member Type", font=("Times new roman", 15,"bold"),textvariable=self.member_var
                        , bg="powder blue", padx=2, pady=6)
        lblMembr.grid(row=0, column=0, sticky=W)


        comMember=ttk.Combobox(DataFrameLeft, font=("Times new roman", 15, "bold"), width=27,state="readonly",textvariable=self.member_var)
        comMember['values']=("Admin Staff", "Student", "Lecturer")                                 
        comMember.grid(row=0, column=1)

        lblPRN_No = Label(DataFrameLeft, text="PRN No:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6) 
        lblPRN_No.grid(row=1, column=0, sticky=W)
        txtPRN_No = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.prn_no_var)
        txtPRN_No.grid(row=1, column=1)

        lblID_No = Label(DataFrameLeft, text="ID No:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6)
        lblID_No.grid(row=2, column=0, sticky=W)
        txtID_No = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.id_no_var)
        txtID_No.grid(row=2, column=1)

        lblFirstName = Label(DataFrameLeft, text="First Name:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6) 
        lblFirstName.grid(row=3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.first_name_var)
        txtFirstName.grid(row=3, column=1)

        lblLastName = Label(DataFrameLeft, text="Last Name:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6) 
        lblLastName.grid(row=4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.last_name_var)
        txtLastName.grid(row=4, column=1)

        lblAddress1 = Label(DataFrameLeft, text="Address 1:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6) 
        lblAddress1.grid(row=5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.address1_var)
        txtAddress1.grid(row=5, column=1)


        lblAddress2 = Label(DataFrameLeft, text="Address 2:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6) 
        lblAddress2.grid(row=6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.address2_var)
        txtAddress2.grid(row=6, column=1)

        lblMobileNo = Label(DataFrameLeft, text="Mobile No:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6) 
        lblMobileNo.grid(row=7, column=0, sticky=W)
        txtMobileNo = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.mobile_no_var)
        txtMobileNo.grid(row=7, column=1)

        
        lblBook_id=Label(DataFrameLeft, text="Book_id:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6)
        lblBook_id.grid(row=0, column=2, sticky=W)
        txtBook_id = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.book_id_var)
        txtBook_id.grid(row=0, column=3)


        lblBookTitle=Label(DataFrameLeft, text="BookTitle:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6) 
        lblBookTitle.grid(row=1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.book_title_var)
        txtBookTitle.grid(row=1, column=3)


        lblAuther=Label(DataFrameLeft, text="Author:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6) 
        lblAuther.grid(row=2, column=2, sticky=W)
        txtAuther = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.Author_var)
        txtAuther.grid(row=2, column=3)

        
        lblDateBorrowed=Label(DataFrameLeft, text="Date Borrowed:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6)
        lblDateBorrowed.grid(row=3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.date_borrowed_var)
        txtDateBorrowed.grid(row=3, column=3)

        
        lblDateDue=Label(DataFrameLeft, text="Date Due:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6) 
        lblDateDue.grid(row=4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.date_due_var)
        txtDateDue.grid(row=4, column=3)

        lblLateReturnFine=Label(DataFrameLeft, text="Late Return Fine:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6) 
        lblLateReturnFine.grid(row=6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.late_return_fine_var)
        txtLateReturnFine.grid(row=6, column=3)


        lblDateOverDate=Label(DataFrameLeft, text="Date Over Due:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6) 
        lblDateOverDate.grid(row=7, column=2, sticky=W)
        txtDateOverDate = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.date_overdue_var)
        txtDateOverDate.grid(row=7, column=3)

        
        lblActualPrice=Label(DataFrameLeft, text="Actual Price:", font=("Times new roman", 15, "bold"), bg="powder blue", padx=2, pady=6)
        lblActualPrice.grid(row=5, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft, font=("Times new roman", 15, "bold"),width=29,textvariable=self.actual_price_var)
        txtActualPrice.grid(row=5, column=3)








        DataFrameRight = LabelFrame(frame, text="Book Details", fg="green", 
                                    bd=12, relief=RIDGE, bg="powder blue", 
                                    font=("times new roman", 12, "bold"))
        DataFrameRight.place(x=910, y=5, width=540, height=350)

        self.txtBox=Text(DataFrameRight, font=("Times new roman", 12, "bold"), width=32, height=16, padx=2, pady=6)
        self.txtBox.grid(row=0, column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")





        listBooks=['Head Firt Book','Python Programming','Data Science','Machine Learning','Artificial Intelligence','Deep Learning','Computer Vision','Natural Language Processing','Big Data','Cloud Computing','Cyber Security','Internet of Things','Blockchain Technology','Augmented Reality','Virtual Reality','Quantum Computing','5G Technology','Edge Computing','Robotics','Automation']

        def selectBook(event=""):
            value=str(listbox.get(listbox.curselection()))
            x=value
            
            if x=="Head Firt Book":
                self.book_id_var.set("BK001")
                self.book_title_var.set("Head First Book")
                self.Author_var.set("Author: Paul Barry")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 500")
                
                
            elif x=="Python Programming":
                self.book_id_var.set("BK002")
                self.book_title_var.set("Python Programming")
                self.Author_var.set(" John Zelle")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 500")
                
            elif x=="Data Science":
                self.book_id_var.set("BK003")
                self.book_title_var.set("Data Science")
                self.Author_var.set("Joel Grus")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 700")
                
            elif x=="Machine Learning":
                self.book_id_var.set("BK004")
                self.book_title_var.set("Machine Learning")
                self.Author_var.set(" Tom M. Mitchell")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 799")
           
            elif x=="Artificial Intelligence":
                self.book_id_var.set("BK005")
                self.book_title_var.set("Artificial Intelligence")
                self.Author_var.set(" Stuart Russell")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 400")
                
                
            elif x=="Deep Learning":
                self.book_id_var.set("BK006")
                self.book_title_var.set("Deep Learning")
                self.Author_var.set(" Ian Goodfellow")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 100")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 800")
              
            elif x=="Computer Vision":
                self.book_id_var.set("BK007")
                self.book_title_var.set("Computer Vision")
                self.Author_var.set(" Richard Szeliski")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 300")
                
            elif x=="Natural Language Processing":
                self.book_id_var.set("BK008")
                self.book_title_var.set("Natural Language Processing")
                self.Author_var.set(" Jurafsky & Martin")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 100")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 845")
                
            elif x=="Big Data":
                self.book_id_var.set("BK009")
                self.book_title_var.set("Big Data")
                self.Author_var.set(" Viktor Mayer-Schönberger")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 100")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 645")
                
            elif x=="Cloud Computing":
                self.book_id_var.set("BK010")
                self.book_title_var.set("Cloud Computing")
                self.Author_var.set(" Anthony Velte")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 100")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 845")   
                
                
            elif x=="Cyber Security":
                self.book_id_var.set("BK0011")
                self.book_title_var.set("Cyber Security")
                self.Author_var.set(" William Stallings")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 100")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 785")
                
            elif x=="Internet of Things":
                self.book_id_var.set("BK0012")
                self.book_title_var.set("Internet of Things")
                self.Author_var.set(" Eve M. Schooler")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 865")        
                
                
            elif x=="Blockchain Technology":
                self.book_id_var.set("BK0013")
                self.book_title_var.set("Blockchain Technology")
                self.Author_var.set(" Andreas M. Antonopoulos")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs.459")
            
            elif x=="Augmented Reality":
                self.book_id_var.set("BK0014")
                self.book_title_var.set("Augmented Reality")
                self.Author_var.set(" developer: Dieter Schmalstieg")
                
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 445")
           
            elif x=="Virtual Reality":
                self.book_id_var.set("BK0015")
                self.book_title_var.set("Virtual Reality")
                self.Author_var.set(" steve M. LaValle")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 655")
           
            elif x=="Quantum Computing":
                self.book_id_var.set("BK0016")
                self.book_title_var.set("Quantum Computing")
                self.Author_var.set(" Michael A. Nielsen")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 865")
                
            elif x=="5G Technology":
                self.book_id_var.set("BK0017")
                self.book_title_var.set("5G Technology")
                self.Author_var.set(" Erik Dahlman")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 765")
                
            elif x=="Edge Computing":
                self.book_id_var.set("BK0018")
                self.book_title_var.set("Edge Computing")
                self.Author_var.set(" Rajkumar Buyya")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 645")
                
            elif x=="Robotics":
                self.book_id_var.set("BK0019")
                self.book_title_var.set("Robotics")
                self.Author_var.set(" John J. Craig")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 545")  
                 
            elif x=="Automation":
                self.book_id_var.set("BK0020")
                self.book_title_var.set("Automation")
                self.Author_var.set(" Frank Lambrecht")

                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=12)
                d3=d1+d2
                self.date_borrowed_var.set(d1)
                self.date_due_var.set(d3)
                self.late_return_fine_var.set("Rs. 50")
                self.date_overdue_var.set("No")
                self.actual_price_var.set("Rs. 555")
                 
        listbox=Listbox(DataFrameRight, font=("Times new roman", 12, "bold"), width=20 ,height=16)
        listbox.bind("<<ListboxSelect>>", selectBook)
        listbox.grid(row=0, column=0, padx=4)    
        listScrollbar.config(command=listbox.yview)    

        for item in listBooks:
            listbox.insert(END, item)          



        framebutton=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        framebutton.place(x=0, y=530, width=1530, height=70)
        
        btnAddData=Button(framebutton,command=self.adda_data,text="Add Data", font=("Times new roman", 12, "bold"), width=28, bg="blue", fg="white")
        btnAddData.grid(row=0, column=0) 

        btnShowData=Button(framebutton, text="Show Data",command=self.showData , font=("Times new roman", 12, "bold"), width=26, bg="blue", fg="white")
        btnShowData.grid(row=0, column=1)

        btnUpdate=Button(framebutton,command=self.update_data, text="Update", font=("Times new roman", 12, "bold"), width=26, bg="blue", fg="white")
        btnUpdate.grid(row=0, column=2) 

        btnDelete=Button(framebutton, text="Delete",command=self.delete, font=("Times new roman", 12, "bold"), width=26, bg="blue", fg="white")
        btnDelete.grid(row=0, column=3) 
 
        btnExit=Button(framebutton,command=self.iExit, text="Exit", font=("Times new roman", 12, "bold"), width=26, bg="blue", fg="white")
        btnExit.grid(row=0, column=4) 

        btnReset=Button(framebutton,command=self.reset,text="Reset", font=("Times new roman", 12, "bold"), width=26, bg="blue", fg="white")
        btnReset.grid(row=0, column=5) 

        FrameDetails=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        FrameDetails.place(x=0, y=590, width=1530, height=210)

        Table_Frame=Frame(FrameDetails, bd=6, relief=RIDGE, bg="Powder blue")
        Table_Frame.place(x=0, y=2, width=1460, height=190)

        xscroll=ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        yscroll=Scrollbar(Table_Frame, orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_Frame, columns=("membertype", "prn_no", "id_no", "first_name", "last_name", "address1", "address2", "mobile_no", "book_id", "book_title", "Author", "date_borrowed", "date_due", "late_return_fine", "date_overdue", "actual_price"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        
        
        
        
        
        
          
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)



        self.library_table.heading("membertype", text="Member Type")
        self.library_table.heading("prn_no", text="PRN No")
        self.library_table.heading("id_no", text="ID No")
        self.library_table.heading("first_name", text="First Name")
        self.library_table.heading("last_name", text="Last Name")
        self.library_table.heading("address1", text="Address 1")
        self.library_table.heading("address2", text="Address 2")
        self.library_table.heading("mobile_no", text="Mobile No")
        self.library_table.heading("book_id", text="Book ID")
        self.library_table.heading("book_title", text="Book Title")
        self.library_table.heading("Author", text="Author")
        self.library_table.heading("date_borrowed", text="Date Borrowed")
        self.library_table.heading("date_due", text="Date Due")
        self.library_table.heading("late_return_fine", text="Late Return Fine")
        self.library_table.heading("date_overdue", text="Date Over Due")
        self.library_table.heading("actual_price", text="Actual Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH, expand=1)

        self.library_table.column("membertype", width=100)
        self.library_table.column("prn_no", width=100)
        self.library_table.column("id_no", width=100)
        self.library_table.column("first_name", width=100)
        self.library_table.column("last_name", width=100)
        self.library_table.column("address1", width=100)
        self.library_table.column("address2", width=100)
        self.library_table.column("mobile_no", width=100)
        self.library_table.column("book_id", width=100)
        self.library_table.column("book_title", width=100)
        self.library_table.column("Author", width=100)
        self.library_table.column("date_borrowed", width=100)
        self.library_table.column("date_due", width=100)
        self.library_table.column("late_return_fine", width=100)
        self.library_table.column("date_overdue", width=100)
        self.library_table.column("actual_price", width=100)

        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)

    def adda_data(self):
       
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="110620",
            database="mydatalibrary"
        )

        my_cursor = conn.cursor()

        my_cursor.execute(
            "INSERT INTO library VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                self.member_var.get(),
                self.prn_no_var.get(),
                self.id_no_var.get(),
                self.first_name_var.get(),
                self.last_name_var.get(),
                self.address1_var.get(),
                self.address2_var.get(),
                self.mobile_no_var.get(),
                self.book_id_var.get(),
                self.book_title_var.get(),
                self.Author_var.get(),
                self.date_borrowed_var.get(),
                self.date_due_var.get(),
                self.late_return_fine_var.get(),
                self.date_overdue_var.get(),
                self.actual_price_var.get()
            )
        )

        conn.commit()
        self.fetch_data()
        conn.close()


        messagebox.showinfo("Success", "Record inserted successfully")
        
    def update_data(self):
     try:
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="110620",
            database="mydatalibrary"
        )

        my_cursor = conn.cursor()

        my_cursor.execute("""
            UPDATE library SET 
            membertype=%s,
            prn_no=%s,
            id_no=%s,
            first_name=%s,
            last_name=%s,
            address1=%s,
            address2=%s,
            mobile_no=%s,
            book_title=%s,
            Author=%s,
            date_borrowed=%s,
            date_due=%s,
            late_return_fine=%s,
            date_overdue=%s,
            actual_price=%s
            WHERE book_id=%s
        """, (
            self.member_var.get(),
            self.prn_no_var.get(),
            self.id_no_var.get(),
            self.first_name_var.get(),
            self.last_name_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.mobile_no_var.get(),
            self.book_title_var.get(),
            self.Author_var.get(),
            self.date_borrowed_var.get(),
            self.date_due_var.get(),
            self.late_return_fine_var.get(),
            self.date_overdue_var.get(),
            self.actual_price_var.get(),
            self.book_id_var.get()
        ))

        conn.commit()
        self.fetch_data()
        conn.close()

        messagebox.showinfo("Success", "Record Updated")


     except Exception as e:
          messagebox.showerror("Error", str(e))
                    
     conn.commit()
     self.fetch_data()
     conn.close()

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            port=3306,
            username="root",
            password="110620",
            database="mydatalibrary"
        )

        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM library")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)

        conn.commit()
        conn.close() 

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']
        
        self.member_var.set(row[0])
        self.prn_no_var.set(row[1])
        self.id_no_var.set(row[2])
        self.first_name_var.set(row[3])
        self.last_name_var.set(row[4])
        self.address1_var.set(row[5])
        self.address2_var.set(row[6])
        self.mobile_no_var.set(row[7])
        self.book_id_var.set(row[8])
        self.book_title_var.set(row[9])
        self.Author_var.set(row[10])
        self.date_borrowed_var.set(row[11])
        self.date_due_var.set(row[12])
        self.late_return_fine_var.set(row[13])
        self.date_overdue_var.set(row[14])
        self.actual_price_var.set(row[15])
        
    def showData(self):
        self.txtBox.insert(END, "Member Type:\t\t" + self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No:\t\t" + self.prn_no_var.get() + "\n")
        self.txtBox.insert(END, "ID No:\t\t" + self.id_no_var.get() + "\n")
        self.txtBox.insert(END, "First Name:\t\t" + self.first_name_var.get() + "\n")
        self.txtBox.insert(END, "Last Name:\t\t" + self.last_name_var.get() + "\n")
        self.txtBox.insert(END, "Address 1:\t\t" + self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address 2:\t\t" + self.address2_var.get() + "\n")
        self.txtBox.insert(END, "Mobile No:\t\t" + self.mobile_no_var.get() + "\n")
        self.txtBox.insert(END, "Book ID:\t\t" + self.book_id_var.get() + "\n")
        self.txtBox.insert(END, "Book Title:\t\t" + self.book_title_var.get() + "\n")
        self.txtBox.insert(END, "Author:\t\t" + self.Author_var.get() + "\n")
        self.txtBox.insert(END, "Date Borrowed:\t\t" + self.date_borrowed_var.get() + "\n")
        self.txtBox.insert(END, "Date Due:\t\t" + self.date_due_var.get() + "\n")
        self.txtBox.insert(END, "Late Return Fine:\t\t" + self.late_return_fine_var.get() + "\n")
        self.txtBox.insert(END, "Date Overdue:\t\t" + self.date_overdue_var.get() + "\n")
        self.txtBox.insert(END, "Actual Price:\t\t" + self.actual_price_var.get() + "\n")

   
    def reset(self):
        self.member_var.set("")
        self.prn_no_var.set("")
        self.id_no_var.set("")
        self.first_name_var.set("")
        self.last_name_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.mobile_no_var.set("")
        self.book_id_var.set("")
        self.book_title_var.set("")
        self.Author_var.set("")
        self.date_borrowed_var.set("")
        self.date_due_var.set("")
        self.late_return_fine_var.set("")
        self.date_overdue_var.set("")
        self.actual_price_var.set("")
        
        
    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System", "Do you want to exit?")
        if iExit > 0:
            self.root.destroy()
            return
        
        
    def delete(self):
        if self.prn_no_var.get()=="" or self.id_no_var.get()=="":
            messagebox.showerror("Error", "First select a record to delete")
      
        else:     
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="110620",
            database="mydatalibrary"
        )

        my_cursor = conn.cursor()
        query = "DELETE FROM library WHERE prn_no=%s AND id_no=%s"
        values = (self.prn_no_var.get(), self.id_no_var.get())
        my_cursor.execute(query, values)
        
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Record deleted successfully")
            
if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
    