from tkinter import *
from tkinter.ttk import *
import mysql.connector as mysql
from tkinter import messagebox
from idlelib.tooltip import Hovertip
from PIL import Image, ImageTk

import os
from tkinter import filedialog
import math

#from PIL import ImageTk, Image

try:

    con = mysql.connect(host="localhost", user="root", passwd="Aamir@21i")

    #db_create = con.execute(query_db)
    mycursor = con.cursor()
    query_db = "CREATE DATABASE maindb1"
    mycursor.execute(query_db)
    #mycursor.execute("commit")
    print("DATABASE CREATED!!!")

except:
    print("Database Already Exist with this name")

amount_list = []
actual_amount_list = []

def db_creation():

    try:

        con_table = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")
        con_table2 = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")
        con_table3 = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")
        con_table4 = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")
        con_table4_2 = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")


        mycursor_table3 = con_table3.cursor()
        query_table3 = "CREATE TABLE product (pro_id VARCHAR(255), pro_name VARCHAR(255), pro_weight INT(255), pro_unit_price INT(255) )"
        mycursor_table3.execute(query_table3)
        mycursor_table3.execute("COMMIT")
        print("TABLES CREATED!")

        mycursor_table4 = con_table4.cursor()
        query_table4 = "CREATE TABLE sales (customer VARCHAR(255), mobile VARCHAR(255), pro_list VARCHAR(255), total_amount INT(255), due_amount INT(255), invoice VARCHAR(255) )"
        mycursor_table4.execute(query_table4)
        mycursor_table4.execute("COMMIT")
        print("TABLES CREATED!!")

        query_table = "CREATE TABLE signup_data (owner VARCHAR(255), business VARCHAR(255), contact VARCHAR(255), email VARCHAR(255), password VARCHAR(255), cpassword VARCHAR(255), question VARCHAR(255), answer VARCHAR(255)  )"
        cursor_table = con_table.cursor()
        cursor_table.execute(query_table)
        cursor_table.execute("COMMIT")
        print("TABLE CREATED")

        mycursor_table4_2 = con_table4_2.cursor()
        query_table4_2 = "CREATE TABLE due_table (due_amount FLOAT(255,2), invoice VARCHAR(255), cust_mobile VARCHAR(255), cust_address VARCHAR(255)  )"
        mycursor_table4_2.execute(query_table4_2)
        mycursor_table4_2.execute("COMMIT")
        print("TABLE CREATED")



        splash.destroy()

    except:

        print("Table based issues with this!")
        splash.destroy()

    con.close()
    con_table.close()

splash = Tk()                                                   #splash Display
splash.geometry("430x200+200+100")
splash.title("WELCOME")
splash_b1 = Button(splash, text="NEXT", command=db_creation)
splash_b1.place(x=320, y=160)
splash.config(background="white")

splash.overrideredirect(1)
splash.mainloop()



root = Tk()
root.geometry("800x540")
root.maxsize(800,540)
root.minsize(800,540)
root.title("PRODUCT NAME")
#root.config(background="white")


pic = Image.open("vector1.png")
img3 = ImageTk.PhotoImage(Image.open("vector1.png"))
resized1 = pic.resize((600, 513), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resized1)
panel1 = Label(root, image=new_pic)
panel1.place(x=255, y=50)



def signup_form():

    sec_questions = ["CHOOSE SECURITY QUESTIONS","What is Your Favorite Color?", "What is the Name of Your First School?","What is Your Favorite Dish?","What is Name of Your Pet?","Who's Your Close Friend?"]

    global signup
    try:

        if signup.state() == "normal":
            signup.focus()

    except:
        signup = Toplevel()
        signup.geometry("500x600")
        signup.title("CREATE ACCOUNT")

        signup_f1 = LabelFrame(signup, text="CREATE ACCOUNT", width=400, height=500)
        signup_f1.place(x=20, y=30)



        def connection_status():                #connection check and INSERT SIGNUP DATA

            con1 = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")
            cursor_check = con1.cursor()
            cursor_check.execute("SELECT email FROM signup_data WHERE email = '" + signup_e4.get() + "' ")
            myemails = cursor_check.fetchall()

            print(myemails)


            import urllib.request
            host = 'http://google.com'
            try:
                urllib.request.urlopen(host)
                print("Connected To INTERNET")
                #messagebox.showinfo("Message","Internet Connection is available!!!!")

                if(signup_e1.get()=="" or signup_e2.get()=="" or signup_e3.get()=="" or signup_e4.get()=="" or signup_e5.get()=="" or signup_e6.get()=="" or signup_c1.get()=="" or signup_e8.get() == ""):

                    messagebox.showerror("status","All Fields are Mandatory")
                else:

                    if(signup_e5.get() != signup_e6.get()):
                        messagebox.showerror("Status","CONFIRM PASSWORD entry donot matches with PASSWORD")

                    elif(myemails):

                        messagebox.showerror("Status","The User with this e-mail is already exist! Try another one.")

                    else:

                        query_insert = "INSERT INTO signup_data VALUES('" + signup_e1.get() + "', '" + signup_e2.get() + "', '" + signup_e3.get() + "', '" + signup_e4.get() + "', '" + signup_e5.get() + "', '" + signup_e6.get() + "', '" + signup_c1.get() + "', '" + signup_e8.get() + "'   )"
                        mycursor1 = con1.cursor()
                        mycursor1.execute(query_insert)
                        mycursor1.execute("commit")
                        messagebox.showinfo("Status", "CONGRATULATION!! YOUR ACCOUNT CREATED.", parent=signup)

                        signup.destroy()

            except:
                print("NOT CONNECTED TO INTERNET")
                messagebox.showerror("ERROR","INTERNET CONNECTION FAILED!!!!")


        signup_l1 = Label(signup_f1, text="Owner Name :").place(x=15,y=20)
        signup_l2 = Label(signup_f1, text="Business Name :").place(x=15, y=60)
        signup_l3 = Label(signup_f1, text="Contact No. :").place(x=15, y=100)
        signup_l4 = Label(signup_f1, text="Email :").place(x=15, y=140)
        signup_l5 = Label(signup_f1, text="Password :").place(x=15, y=180)
        signup_l6 = Label(signup_f1, text="Confirm Password :").place(x=15, y=220)
        signup_l7 = Label(signup_f1, text="Security Question :").place(x=15, y=260)
        signup_l8 = Label(signup_f1, text="Your Answer :").place(x=15, y=300)

        signup_e1 = Entry(signup_f1)
        signup_e1.place(x=170, y=20)
        signup_e2 = Entry(signup_f1)
        signup_e2.place(x=170, y=60)
        signup_e3 = Entry(signup_f1)
        signup_e3.place(x=170, y=100)
        signup_e4 = Entry(signup_f1)
        signup_e4.place(x=170, y=140)

        signup_e5 = Entry(signup_f1, show="*")
        signup_e5.place(x=170, y=180)
        signup_e6 = Entry(signup_f1, show="*")
        signup_e6.place(x=170, y=220)
        #signup_e7 = Entry(signup_f1)
        #signup_e7.place(x=170, y=260)

        signup_c1 = Combobox(signup_f1, width=30)
        signup_c1.place(x=170,y=260)
        signup_c1['values'] = sec_questions
        signup_c1.current(0)

        signup_e8 = Entry(signup_f1, width=33)
        signup_e8.place(x=170, y=300)


        signup_b1 = Button(signup_f1, text="CREATE", command=connection_status)
        signup_b1.place(x=190,y=380)

        tip1 = Hovertip(signup_e1, "Enter OWNER NAME")
        tip2 = Hovertip(signup_e2, "Enter BUSINESS NAME")
        tip3 = Hovertip(signup_e3, "Enter CONTACT NAME")
        tip4 = Hovertip(signup_e4, "Enter E-MAIL")
        tip5 = Hovertip(signup_e5, "Enter PASSWORD")
        tip6 = Hovertip(signup_e6, "Enter PASSWORD, AGAIN")
        tip7 = Hovertip(signup_c1, "Enter SECURITY QUESTION")
        tip8 = Hovertip(signup_e8, "Enter SECURITY ANSWER!")

        print("HGFGHFHG")
        signup.mainloop()



def signin_user():                                              #SIGNED IN WINDOW

    con2 = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")

    query_select = "SELECT email, password FROM signup_data WHERE email = '"+ root_e1.get() +"' and password = '"+ root_e2.get() +"' "
    mycursor2 = con2.cursor()
    mycursor2.execute(query_select)
    mydata2 = mycursor2.fetchone()



    if(root_e1.get()=="" or root_e2.get()==""):

        messagebox.showwarning("Warning","All Fields are Mandatory")

    else:
        print(mydata2)

        query_store = "SELECT business FROM signup_data WHERE email = '"+ root_e1.get() +"' "
        mycursor2.execute(query_store)
        mystore_name = mycursor2.fetchone()
        print(mystore_name)

        if(mydata2):
            messagebox.showinfo("Status","Login Successfully!!!")

            mainScreen = Toplevel()
            mainScreen.geometry("800x550")
            mainScreen.title("BUSINESS WINDOW")
            mainScreen.state("zoomed")
            #mainScreen.config(background="whitesmoke")

            mainScreen_l1 = Label(mainScreen, foreground="seagreen", text=mystore_name[0])
            mainScreen_l1.config(font=("League Spartan", 28,"bold"))
            mainScreen_l1.pack()

            mainScreen_l2 = Label(mainScreen, text="Cyberovate")
            mainScreen_l2.place(x=990, y=635)
            mainScreen_l2.config(font=("Arial", 32, "bold"), foreground="gainsboro")

            mainScreen_l2_2 = Label(mainScreen, text="the perfect solution...")
            mainScreen_l2_2.place(x=1100, y=680)
            #mainScreen_l2_2.config(background="white")


            mainScreen_f2 = LabelFrame(mainScreen, text="Info" ,width=440, height=260)
            mainScreen_f2.place(x=40,y=100)

            mainscreen_l1 = Label(mainScreen_f2, text="Customer Name :")
            mainscreen_l1.place(x=40, y=20)
            #mainscreen_l1.config(background="white")

            mainscreen_l2 = Label(mainScreen_f2, text="Mobile :")
            mainscreen_l2.place(x=40, y=60)
            #mainscreen_l2.config(background="white")

            #mainscreen_l3 = Label(mainScreen, text="Address :")
            #mainscreen_l3.place(x=40, y=210)
            #mainscreen_l3.config(background="white")

            #mainscreen_l4 = Label(mainScreen, text="City :")
            #mainscreen_l4.place(x=40, y=250)
            #mainscreen_l4.config(background="white")

            mainscreen_l5 = Label(mainScreen_f2, text="Product :")
            mainscreen_l5.place(x=40, y=100)
            #mainscreen_l5.config(background="white")

            mainscreen_l6 = Label(mainScreen_f2, text="Unit/Weight :")
            mainscreen_l6.place(x=40, y=140)
            #mainscreen_l6.config(background="white")

            mainscreen_l7 = Label(mainScreen_f2, text="Amount/Unit :")
            mainscreen_l7.place(x=40, y=180)
            #mainscreen_l7.config(background="white")

            #mainscreen_l8 = Label(mainScreen, text="Total Amount :")
            #mainscreen_l8.place(x=40, y=410)
            #mainscreen_l8.config(background="white")

            mainscreen_l9 = Label(mainScreen, text="GST % :")
            mainscreen_l9.place(x=910, y=350)
            #mainscreen_l9.config(background="white")

            mainscreen_l10 = Label(mainScreen, text="net Sum  :")
            mainscreen_l10.place(x=1100, y=345)
            #mainscreen_l10.config(background="white")

            mainscreen_l13 = Label(mainScreen, text="Amount Given By Customer : ")
            mainscreen_l13.place(x=960, y=520)
            mainscreen_l14 = Label(mainScreen, text="Amount Needs To Be Returned : ")
            mainscreen_l14.place(x=960, y=560)


            #Logo Display>>>>>>

            logo = Image.open("bill.png")
            img3 = ImageTk.PhotoImage(Image.open("bill.png"))
            resized3 = logo.resize((284, 273), Image.ANTIALIAS)
            new_logo = ImageTk.PhotoImage(resized3)
            panel2 = Label(mainScreen, image=new_logo)
            panel2.place(x=445, y=360)

            mainscreen_l11 = Label(mainScreen, text="gstamount :")
            mainscreen_l11.place(x=1100, y=370)

            mainscreen_l12 = Label(mainScreen, text="netAmountTo_Pay")
            mainscreen_l12.place(x=1100, y=410)

            def find_total():
                from win10toast import ToastNotifier
                toast = ToastNotifier()

                net_amount_list2 = []


                try:

                    mainscreen_l11.config(font=("Helvetica",13) ,text="GST : " + str(int(mainScreen_e9.get())/100 * sum(actual_amount_list)) )


                    mainscreen_l12.config(foreground="green" ,font=("Helvetica",13, "bold"), text="Net Amount to PAY : " +str(int(mainScreen_e9.get())/100 * sum(actual_amount_list) + sum(actual_amount_list)))



                    #toast.show_toast("INFO!", str(mainScreen_e1.get()) +" has to pay " + str(int(mainScreen_e9.get())/100 * sum(actual_amount_list) + sum(actual_amount_list)) )
                    messagebox.showinfo("NET AMOUNT : ", " Net Amount :  " + str(int(mainScreen_e9.get())/100 * sum(actual_amount_list) + sum(actual_amount_list)) , parent=mainScreen)

                    mainScreen.focus_force()

                except:
                    print("Enter Valid Character")
                    messagebox.showwarning("Warning","Enter Correct Value for GST", parent=mainScreen)



            mainScreen_e1 = Entry(mainScreen_f2, width=26)
            mainScreen_e1.place(x=170,y=20)
            mainScreen_e2 = Entry(mainScreen_f2)
            mainScreen_e2.place(x=170, y=60)

            #mainScreen_e3 = Entry(mainScreen, width=26)
            #mainScreen_e3.place(x=170, y=210)
            #mainScreen_e4 = Entry(mainScreen)
            #mainScreen_e4.place(x=170, y=250)



            mainScreen_c5 = Combobox(mainScreen_f2, width=23, state='readonly')
            mainScreen_c5.place(x=170, y=100)

            var_mainScreen_c6 = IntVar()

            mainScreen_c6 = Combobox(mainScreen_f2, width=23, state='readonly', textvariable=var_mainScreen_c6)
            mainScreen_c6.place(x=170, y=140)

            var_mainScreen_e7 = IntVar()

            mainScreen_e7 = Entry(mainScreen_f2, state = 'disabled', textvariable=var_mainScreen_e7)
            mainScreen_e7.place(x=170, y=180)

            mainScreen_c7 = Combobox(mainScreen, width=21, state="readonly")
            mainScreen_c7.place(x=1114,y=460)
            mainScreen_c7['values'] = ['Cash','Google Pay', 'Phone Pay', 'PayTM', 'BHIM UPI', 'Debit/Credit Card', 'Token/Voucher', 'Others']
            mainScreen_c7.current(0)

            mainscreen_l13 = Label(mainScreen, text="Payment Mode : ")
            mainscreen_l13.place(x=960, y=460)

            #<<<<<Populate Combobox>>>>>

            product_units_list = []

            for u in range(1, 101):
                product_units_list.append(u)
            mainScreen_c6['values'] = product_units_list
            mainScreen_c6.current(0)


            con_combo1 = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")
            mycursor_combo1 = con_combo1.cursor()
            query_combo1 = "SELECT pro_id, pro_name, pro_weight FROM product"
            mycursor_combo1.execute(query_combo1)
            myproduct = mycursor_combo1.fetchall()
            print(myproduct)

            combo_options_list = []

            for v in myproduct:
                combo_options_list.append(str(v[1]))

            print(combo_options_list)
            mainScreen_c5['values'] = combo_options_list
            mainScreen_c5.set("SELECT PRODUCTS")
            #mainScreen_c6.current(0)

            con_combo1.close()

            #<<<<<New product unit/amount update<<<<<<

            con_amount = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")


            def handler(event):

                mycursor_amount = con_amount.cursor()
                query_amount = "SELECT pro_unit_price FROM product WHERE pro_name = '" + mainScreen_c5.get() + "' "

                mycursor_amount.execute(query_amount)
                mydata_amount = mycursor_amount.fetchone()
                print(mydata_amount[0])

                var_mainScreen_e7.set(mydata_amount[0])


            mainScreen_c5.bind('<<ComboboxSelected>>', handler)



            #var_mainScreen_e8 = IntVar()
            #mainScreen_e8 = Entry(mainScreen, state='readonly', textvariable=var_mainScreen_e8)
            #mainScreen_e8.place(x=170, y=410)

            #var_mainScreen_e8.set()

            var_mainScreen_e9 = IntVar()
            mainScreen_e9 = Entry(mainScreen, textvariable=var_mainScreen_e9)
            mainScreen_e9.place(x=960, y=350)

            var_mainScreen_e11 = IntVar()
            #var_mainScreen_e10 = IntVar()

            mainScreen_e10 = Entry(mainScreen)
            mainScreen_e10.place(x=1137, y=520 )
            mainScreen_e11 = Entry(mainScreen, state = "readonly", textvariable=var_mainScreen_e11)
            mainScreen_e11.place(x=1137, y=560)

            var_mainScreen_e12 = StringVar()
            mainScreen_e12 = Entry(mainScreen, state="disabled", textvariable = var_mainScreen_e12)
            mainScreen_e12.place(x=780,y=520)

            invoice_list = []
            def invoice_gen():
                import random
                from datetime import datetime

                months = ['N/A', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                #days = []


                num_1 = random.randint(0, 1000)
                num_2 = random.randint(0, 100)

                obj_time = datetime.now()
                obj_h1 = obj_time.hour
                obj_m1 = obj_time.minute
                obj_s1 = obj_time.second

                obj_month = obj_time.month
                obj_week_day = obj_time.strftime("%a")

                final_invoice_text = str(num_1) + str(num_2) + str(months[obj_month].upper()) + str(obj_week_day.upper()) + str(obj_h1) + str(obj_m1) + str(obj_s1)

                invoice_list.append(final_invoice_text)

                print(invoice_list)
                print(invoice_list[0])



            def pdf_gen():
                import reportlab


            def amount_due():
                due_win = Toplevel()
                due_win.geometry("760x500")
                due_win.title("Due Amount Details ")

                pro_val = int(mainScreen_e9.get()) / 100 * sum(actual_amount_list) + sum(actual_amount_list)
                due_val = pro_val - float(mainScreen_e10.get())
                print(due_val)

                due_f1 = LabelFrame(due_win, text="Due Details" ,width=350, height=400)
                due_f1.place(x=20, y=40)
                due_f2 = LabelFrame(due_win, text="Instructions", width=300, height=400)
                due_f2.place(x=390, y=40)

                due_l1 = Label(due_f1, text="Due Amount : ")
                due_l1.place(x=20, y=30)
                due_l2 = Label(due_f1, text="Invoice : ")
                due_l2.place(x=20, y=70)
                due_l3 = Label(due_f1, text="Customer Mobile : ")
                due_l3.place(x=20, y=110)
                due_l4 = Label(due_f1, text="Customer Address : ")
                due_l4.place(x=20, y=150)

                due_tips = Label(due_f2, wraplength=200,text="Tips - It is advisable to never allow an unknown customer for due services, even his/her address is known to you. In that case, you might be indulged in some unusual conflicts.Product entity/organisation/company will not be responsible for any kind of losses you have related to this issue.")
                due_tips.place(x=10, y=20)

                var_due_e1 = IntVar()
                var_due_e2 = StringVar()

                due_e1 = Entry(due_f1, textvariable = var_due_e1, state="readonly")
                due_e1.place(x=170, y=30)
                var_due_e1.set(due_val)

                due_e2 = Entry(due_f1, state="disabled",  textvariable = var_due_e2)
                due_e2.place(x=170, y=70)

                var_due_e2.set(invoice_list[len(invoice_list)-1])

                due_e3 = Entry(due_f1)
                due_e3.place(x=170, y=110)
                due_e4 = Entry(due_f1)
                due_e4.place(x=170, y=150)

                # con_due.close()


                def insert_due_data_bill():

                    if(due_e3.get()=="" or due_e4.get()==""):
                        messagebox.showwarning("Warning","All fields are mandatory!", parent=due_win)
                    else:
                        con_due = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")
                        mycursor_due = con_due.cursor()
                        query_due = "INSERT INTO due_table VALUES('" + due_e1.get() + "',  '"+ due_e2.get() +"' , '" + due_e3.get() + "', '" + due_e4.get() + "'  ) "
                        mycursor_due.execute(query_due)
                        mycursor_due.execute("COMMIT")
                        messagebox.showinfo("Success", "Due Log entry done! Invoice Generated!", parent=due_win)

                        #con_sale2 = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")
                        #mycursor_sale2 = con_sale2.cursor()

                        #query_sale2 = "INSERT INTO sales VALUES( '" + mainScreen_e1.get() + "', '" + mainScreen_e2.get() + "', '" + str(pro_list3[0]) + "' , '" + str(sum(pro_amount_list3)) + "', '" + str(0) + "', '" + invoice_list[len(invoice_list) - 1] + "'  )  "

                        #sales_data_insertion()

                due_b1 = Button(due_f1, text="Set Reminder & Generate Bill", command=insert_due_data_bill)
                due_b1.place(x=170, y=200)

                due_win.mainloop()

            #AMOUNT TO BE RETURNED TO CUSTOMER



            def amount_return():
                p1 = mainScreen_e10.get()
                p2 = int(mainScreen_e9.get()) / 100 * sum(actual_amount_list) + sum(actual_amount_list)

                if mainScreen_e10.get() == "":

                    messagebox.showerror("Alert!", "Recieve amount from the Customer first!", parent=mainScreen)

                else:

                    if(int(p1) < p2):
                        messagebox.showerror("Error","RECIEVE PROPER AMOUNT FROM THE CUSTOMER!!! ", parent=mainScreen)
                        mainScreen_e11.config(foreground="crimson")

                        invoice_gen()
                        amount_due()

                        var_mainScreen_e12.set(invoice_list[len(invoice_list)-1])

                    else:

                        con_sale1 = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")

                        if(len(actual_amount_list)==0):
                            messagebox.showwarning("Warning", "ADD SOME ITEMS TO CART", parent=mainScreen)

                        else:

                            var_mainScreen_e11.set("{:.2f}".format(float(int(p1) - p2)))
                            mainScreen_e11.config(foreground="black")

                            actual_amount_list.clear()

                            invoice_gen()

                            #mainScreen_e1.delete(0, END)
                            #mainScreen_e2.delete(0, END)
                            mainScreen_e9.delete(0, END)
                            mainScreen_e10.delete(0, END)
                            mainScreen_e11.get()==""

                            mainscreen_l11.config(text="")
                            mainscreen_l12.config(text="")

                            #mainScreen_tree.delete(*mainScreen_tree.get_children())


                            var_mainScreen_e12.set(invoice_list[len(invoice_list)-1])

                            def sales_data_insertion():

                                pro_list3 = []
                                pro_amount_list3 =[]
                                for data_val in mainScreen_tree.get_children():
                                    pro_list2 = mainScreen_tree.item(data_val)['values'][0]

                                    pro_list3.append(pro_list2)

                                for data_val2 in mainScreen_tree.get_children():
                                    pro_amount3 = mainScreen_tree.item(data_val2)['values'][3]

                                    pro_amount_list3.append(pro_amount3)
                                print(pro_amount_list3)

                                mycursor_sale1 = con_sale1.cursor()
                                query_sale1 = "INSERT INTO sales VALUES( '"+ mainScreen_e1.get() +"', '"+ mainScreen_e2.get() +"', '"+ str(pro_list3[0]) + "' , '" + str(sum(pro_amount_list3) ) + "', '"+ str(0) +"', '"+ invoice_list[len(invoice_list)-1] +"'  )  "
                                mycursor_sale1.execute(query_sale1)
                                mycursor_sale1.execute("COMMIT")

                                print(pro_list2)
                                print(pro_list3)



                                messagebox.showinfo("Wow!", "Congratulation! ONE SALE DONE! Click 'OK' to add new Sale ", parent=mainScreen)

                            sales_data_insertion()



            mainScreen_tree = Treeview(mainScreen)
            mainScreen_tree.place(x=750, y=110)
            mainScreen_tree["column"] = ("one", "two", "three","four")
            mainScreen_tree.column("#0", width=10, minwidth=10)
            mainScreen_tree.column("one", width=200, minwidth=180)
            mainScreen_tree.column("two", width=100, minwidth=100)
            mainScreen_tree.column("three", width=100, minwidth=100)
            mainScreen_tree.column("four", width=100, minwidth=100)

            mainScreen_tree.heading("#0", text="")
            mainScreen_tree.heading("one", text="PRODUCT")
            mainScreen_tree.heading("two", text="UNITS")
            mainScreen_tree.heading("three", text="PRICE/UNIT")
            mainScreen_tree.heading("four", text="GROSS PRICE")
            mainScreen_tree.heading("#0", text="")

            #mainScreen_tree.tag_configure('oddrow', background="yellow")


            def add_product():
                pop_win = Toplevel()
                pop_win.geometry("450x350")
                pop_win.title("ADD YOUR PRODUCT")


                def load_product():
                    con_load = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")

                    if(pop_e1.get()=="" or pop_e2.get()=="" or pop_e3.get()=="" or pop_e4.get()==""):
                        messagebox.showwarning("Warning","All entries are mandatory", parent=pop_win)

                    else:

                        mycursor_load = con_load.cursor()
                        query_load = "INSERT INTO product VALUES('"+ pop_e1.get() +"', '"+ pop_e2.get() +"', '"+ pop_e3.get() +"', '"+ pop_e4.get() +"' )"
                        mycursor_load.execute(query_load)
                        mycursor_load.execute("COMMIT")
                        pop_win.grab_set()
                        messagebox.showinfo("Done!","YOUR PRODUCT GETS LOADED TO YOUR STORE", parent=pop_win)

                    #con_load.close()

                pop_l1 = Label(pop_win, text="Product ID : ").place(x=40, y=50)
                pop_l2 = Label(pop_win, text="Product Name : ").place(x=40, y=90)
                pop_l3 = Label(pop_win, text="Weight : ").place(x=40, y=130)
                pop_l4 = Label(pop_win, text="Price/Unit : ").place(x=40, y=170)
                pop_e1 = Entry(pop_win)
                pop_e1.place(x=150, y=50)
                pop_e2 = Entry(pop_win)
                pop_e2.place(x=150, y=90)
                pop_e3 = Entry(pop_win)
                pop_e3.place(x=150, y=130)
                pop_e4 = Entry(pop_win)
                pop_e4.place(x=150, y=170)
                pop_b1 = Button(pop_win, text="ADD", command=load_product)
                pop_b1.place(x=200, y=250)


                pop_win.mainloop()



            #ERASED FROM HERE


            #style = Style()

            mainScreen_f1 = LabelFrame(mainScreen,  width=390, height=90)
            mainScreen_f1.place(x=40, y=600)


            #style.configure("Treeview", background="whitesmoke")


            def filter_win():
                search_window = Toplevel()
                search_window.geometry("750x600")
                search_window.title("FILTER/SEARCH")

                search_f1 = LabelFrame(search_window, width=350, height=180, text="SEARCH SALE RECORDS")
                search_f1.place(x=20,y=30)

                search_l1 = Label(search_f1, text="Enter Invoice Number")
                search_l1.place(x=40, y=30)

                search_e1 = Entry(search_f1, width=26)
                search_e1.place(x=40, y=55)

                search_b1 = Button(search_f1, text="Search..")
                search_b1.place(x=210, y=53)


                search_window.mainloop()



            mainScreen_b2 = Button(mainScreen_f1, text="Filter", command=filter_win)
            mainScreen_b2.place(x=20, y=20)

            mainScreen_b1 = Button(mainScreen_f1, text=" Add Product ", command=add_product)
            mainScreen_b1.place(x=160, y=20)


            def move_cart():

                if(mainScreen_e1.get()=="" or mainScreen_e2.get()=="" or mainScreen_c5.get()=="" or mainScreen_c6.get()=="" or mainScreen_e7.get()==""):
                    messagebox.showwarning("Warning","All fields are mandatory", parent=mainScreen)

                else:
                    mainScreen_tree.insert('', index='end', text='parent',values=(mainScreen_c5.get(), mainScreen_c6.get(), mainScreen_e7.get(), int(mainScreen_c6.get()) * int(mainScreen_e7.get())) )


               #     for items_val in mainScreen_tree.get_children():

                #        amount = int(mainScreen_tree.item(items_val)['values'][2])

                #    amount_list.append(amount)
                #    total1 = mainScreen_tree.item(items_val)['values']

                #    print(amount_list)
                 #   print(sum(amount_list))
                #    print(total1)


                    for items_val2 in mainScreen_tree.get_children():

                        amount_2 = int(mainScreen_tree.item(items_val2)['values'][3])

                    actual_amount_list.append(amount_2)
                    total2 = mainScreen_tree.item(items_val2)['values']


                    print(actual_amount_list)
                    print(sum(actual_amount_list))
                    print(total2)

                    #messagebox.showinfo("ghjg", str(amount) + "total sum : "+str(sum(amount_list)) )
                    messagebox.showinfo("ACTUAL", str(amount_2) + "actual sum : " + str(sum(actual_amount_list)) , parent=mainScreen)

                    #mainscreen_l9 = Label(mainScreen)
                    #mainscreen_l9.place(x=750, y=380)
                    #mainscreen_l9.config(background="white", font=(("Helvetica", 13)), text="Total : " + str(sum(amount_list)) )

                    mainscreen_l10.config(font=(("Helvetica", 13)), text="Actual Total : " + str(sum(actual_amount_list)) )


            def del_cart():

                try:

            #        for nm in mainScreen_tree.selection():

            #            r1 = mainScreen_tree.item(nm, 'values')[2]
             #           print(r1)

             #       x1 = mainScreen_tree.selection()[0]
            #        mainScreen_tree.delete(x1)

             #       amount_list.pop(amount_list.index(int(r1)))
             #       print(sum(amount_list))
             #       mainscreen_l9.config(background="white", font=(("Helvetica", 13)),text="Total : " + str(sum(amount_list)))
            #        print(amount_list)
                    #total2 = mainScreen_tree.item(items_val2)['values']

                    for nm2 in mainScreen_tree.selection():
                        r2 = mainScreen_tree.item(nm2, 'values')[3]
                        print(r2)

                    x2 = mainScreen_tree.selection()[0]
                    mainScreen_tree.delete(x2)

                    actual_amount_list.pop(actual_amount_list.index(int(r2)))
                    print(sum(actual_amount_list))
                    mainscreen_l10.config(font=(("Helvetica", 13)), text="ActualTotal : " + str(sum(actual_amount_list)))
                    print(actual_amount_list)


                except:
                    messagebox.showwarning("Warning", "First, You must select a row to delete", parent=mainScreen)










            #mainscreen_l9 = Label(mainScreen)
            #mainscreen_l9.place(x=750, y=380)
            #mainscreen_l9.config(background="white", font=(("Helvetica", 13)), text="Total : " + str(sum(amount_list)))

            mainScreen_b3 = Button(mainScreen_f2, text="Move to Cart", command=move_cart)
            mainScreen_b3.place(x=342, y=120)

            mainScreen_b4 = Button(mainScreen, text=" Remove From Cart", command=del_cart)
            mainScreen_b4.place(x=750, y=350)

            mainScreen_b8 = Button(mainScreen, text="Generate Sale NOW!", command=amount_return)
            mainScreen_b8.place(x=963, y=597)


            mainScreen_sep1 = Separator(mainScreen, orient="horizontal")
            mainScreen_sep1.place(x=750, y=450, width=512)

            def enable_button(*args):
                t1 = mainScreen_e9.get()

                if(t1):
                    mainScreen_b6.config(state='normal')
                else:
                    mainScreen_b6.config(state='disabled')


            def open_cal():
                from subprocess import call
                call(["calc.exe"])

            mainScreen_b5 = Button(mainScreen_f1, text=" Calculator", command=open_cal)
            mainScreen_b5.place(x=300, y=20)

            mainScreen_b6 = Button(mainScreen, text="Find Total", command=find_total, state="disabled")
            mainScreen_b6.place(x=960, y=385)

            var_mainScreen_e9.trace("w", enable_button)  #enabling button to find total


            mainScreen.mainloop()

        else:
            messagebox.showerror("Status","Email and Password doesnot Matches!")



def forget_pass(e):
    sec_questions = ["CHOOSE SECURITY QUESTIONS","What is Your Favorite Color?", "What is the Name of Your First School?","What is Your Favorite Dish?","What is Name of Your Pet?","Who's Your Close Friend?"]

    forget_win = Toplevel()
    forget_win.geometry("600x320")
    forget_win.title("FORGET PASSWORD")
    #forget_win.config(background="white")


    forget_l1 = Label(forget_win, text="Enter Your Security Question :").place(x=20,y=20)
    forget_l2 = Label(forget_win, text="Enter Your Answer :").place(x=20, y=100)

    forget_c1 = Combobox(forget_win, width=30, state="readonly")
    forget_c1.place(x=20, y=45)
    forget_c1['values'] = sec_questions
    forget_c1.current(0)
    forget_e2 = Entry(forget_win, width=33)
    forget_e2.place(x=20, y=125)

    forget_f1 = LabelFrame(forget_win, text="OTP CODE", width=270, height=260)
    forget_f1.place(x=290, y=20)

    forget_l3 = Label(forget_f1, text="Enter One-Time-Password (OTP)")
    forget_l3.place(x=20, y=20)
    forget_l3 = Label(forget_f1, text="Enter New Password")
    forget_l3.place(x=20, y=100)
    forget_e3 = Entry(forget_f1, width=30, state="disabled")
    forget_e3.place(x=20, y=45)
    forget_e4 = Entry(forget_f1, width=30, state="disabled")
    forget_e4.place(x=20, y=125)



    #def gen_otp():



    forget_b1 = Button(forget_win, text="SEND")
    forget_b1.place(x=149, y=175)
    forget_b2 = Button(forget_f1, text="SUBMIT", state="disabled")
    forget_b2.place(x=120, y=175)


    forget_win.mainloop()



root_f1 = LabelFrame(root, text="LOGIN", width=235, height=400)
root_f1.place(x=20,y=50)

root_l1 = Label(root_f1, text="Username :")
root_l1.place(x=30,y=25)
#root_l1.config(font=("Helvetica", 11))
root_l2 = Label(root_f1, text="Password :")
root_l2.place(x=30,y=95)

root_e1 = Entry(root_f1, width=27)
root_e1.place(x=30,y=50)
root_e2 = Entry(root_f1, width=27, show="*")
root_e2.place(x=30,y=120)


root_b1 = Button(root_f1, text="LOGIN" ,width=27, command=signin_user)
root_b1.place(x=28, y=180)

root_b2 = Button(root_f1, text="SIGN UP", command=signup_form)
root_b2.place(x=30, y=310)

root_l3 = Label(root_f1, text="Forget Password", cursor = "hand2")
root_l3.config(foreground="blue")
root_l3.place(x=120, y=360)
root_l3.bind("<Button-1>", lambda e:forget_pass(e))




root.mainloop()







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
