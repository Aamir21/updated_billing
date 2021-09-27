from tkinter import *
from tkinter.ttk import *
import mysql.connector as mysql
from tkinter import messagebox
from idlelib.tooltip import Hovertip
import os

#from PIL import ImageTk, Image




con = mysql.connect(host="localhost", user="root", passwd="Aamir@21i")


amount_list = []

def db_creation():
    con_table = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")
    con_table2 = mysql.connect(host="localhost", user="root", passwd="Aamir@21i", database="Maindb1")

    try:
        query_db = "CREATE DATABASE Maindb1"
        #db_create = con.execute(query_db)
        mycursor = con.cursor()
        mycursor.execute(query_db)
        print("DATABASE CREATED!!!")

        query_table = "CREATE TABLE signup_data (owner VARCHAR(255), business VARCHAR(255), contact VARCHAR(255), email VARCHAR(255), password VARCHAR(255), cpassword VARCHAR(255), question VARCHAR(255), answer VARCHAR(255)  )"
        cursor_table = con_table.cursor()
        cursor_table.execute(query_table)
        cursor_table.execute("COMMIT")
        print("TABLE CREATED")

        splash.destroy()

    except:

        print("Database with this name already exist")
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
root.title("PRODUCT NAME")
root.config(background="white")
#canvas = Canvas(root, width=250, height=250)
#canvas.pack()

photo = PhotoImage(file="vector1.png")
lp = Label(root, image=photo)
lp.pack()






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
                        messagebox.showinfo("Status", "CONGRATULATION!! YOUR ACCOUNT CREATED.")


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
            mainScreen.config(background="white")

            mainScreen_l1 = Label(mainScreen, foreground="seagreen" ,text=mystore_name[0])
            mainScreen_l1.config(font=("League Spartan", 28,"bold"), background="white")

            mainScreen_l1.pack()
            mainScreen_l2 = Label(mainScreen, text="PRODUCT LoGo")
            mainScreen_l2.place(x=990, y=635)
            mainScreen_l2.config(font=("Arial", 32, "bold"), foreground="gainsboro", background="white")


            #mainScreen_f1 = LabelFrame(mainScreen, text="GO AHEAD", width=180, height=300)
            #mainScreen_f1.config(background="white")
            #mainScreen_f1.place(x=20, y=80)



            mainscreen_l1 = Label(mainScreen, text="Customer Name :")
            mainscreen_l1.place(x=40, y=130)
            mainscreen_l1.config(background="white")

            mainscreen_l2 = Label(mainScreen, text="Mobile :")
            mainscreen_l2.place(x=40, y=170)
            mainscreen_l2.config(background="white")

            #mainscreen_l3 = Label(mainScreen, text="Address :")
            #mainscreen_l3.place(x=40, y=210)
            #mainscreen_l3.config(background="white")

            #mainscreen_l4 = Label(mainScreen, text="City :")
            #mainscreen_l4.place(x=40, y=250)
            #mainscreen_l4.config(background="white")

            mainscreen_l5 = Label(mainScreen, text="Product :")
            mainscreen_l5.place(x=40, y=290)
            mainscreen_l5.config(background="white")

            mainscreen_l6 = Label(mainScreen, text="Unit/Weight :")
            mainscreen_l6.place(x=40, y=330)
            mainscreen_l6.config(background="white")

            mainscreen_l7 = Label(mainScreen, text="Amount :")
            mainscreen_l7.place(x=40, y=370)
            mainscreen_l7.config(background="white")

            mainscreen_l8 = Label(mainScreen, text="GST % :")
            mainscreen_l8.place(x=450, y=370)
            mainscreen_l8.config(background="white")



            mainScreen_e1 = Entry(mainScreen, width=26)
            mainScreen_e1.place(x=170,y=130)
            mainScreen_e2 = Entry(mainScreen)
            mainScreen_e2.place(x=170, y=170)
            #mainScreen_e3 = Entry(mainScreen, width=26)
            #mainScreen_e3.place(x=170, y=210)
            #mainScreen_e4 = Entry(mainScreen)
            #mainScreen_e4.place(x=170, y=250)
            mainScreen_c5 = Combobox(mainScreen, width=23)
            mainScreen_c5.place(x=170, y=290)
            mainScreen_c6 = Combobox(mainScreen, width=23)
            mainScreen_c6.place(x=170, y=330)
            mainScreen_e7 = Entry(mainScreen)
            mainScreen_e7.place(x=170, y=370)

            mainScreen_e8 = Entry(mainScreen)
            mainScreen_e8.place(x=500, y=370)

            mainScreen_tree = Treeview(mainScreen)
            mainScreen_tree.place(x=750, y=150)
            mainScreen_tree["column"] = ("one", "two", "three")
            mainScreen_tree.column("#0", width=10, minwidth=10)
            mainScreen_tree.column("one", width=200, minwidth=180)
            mainScreen_tree.column("two", width=100, minwidth=100)
            mainScreen_tree.column("three", width=100, minwidth=100)

            mainScreen_tree.heading("#0", text="")
            mainScreen_tree.heading("one", text="PRODUCT")
            mainScreen_tree.heading("two", text="UNITS")
            mainScreen_tree.heading("three", text="PRICE")

            #mainScreen_tree.tag_configure('oddrow', background="yellow")



            def add_product():
                pop_win = Toplevel()
                pop_win.geometry("450x350")
                pop_win.title("ADD YOUR PRODUCT")

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
                pop_b1 = Button(pop_win, text="ADD")
                pop_b1.place(x=200, y=250)



                pop_win.mainloop()



            #ERASED FROM HERE




            mainScreen_f1 = LabelFrame(mainScreen, text="MENU", width=280, height=100)
            mainScreen_f1.place(x=40, y=500)
            #mainScreen_f1.config(background="white")
            mainScreen_b2 = Button(mainScreen_f1, text="Add Products List")
            mainScreen_b2.place(x=20, y=20)
            mainScreen_b1 = Button(mainScreen_f1, text=" ADD PRODUCT ", command=add_product)
            mainScreen_b1.place(x=160, y=20)


            def move_cart():

                if(mainScreen_e1.get()=="" or mainScreen_e2.get()=="" or mainScreen_c5.get()=="" or mainScreen_c6.get()=="" or mainScreen_e7.get()==""):
                    messagebox.showwarning("Warning","All fields are mandatory")

                else:
                    mainScreen_tree.insert('', index='end', text='parent',values=(mainScreen_c5.get(), mainScreen_c6.get(), mainScreen_e7.get()))

                    #p=0
                    for items_val in mainScreen_tree.get_children():

                        amount = int(mainScreen_tree.item(items_val)['values'][2])

                    amount_list.append(amount)

                    total1 = mainScreen_tree.item(items_val)['values']

                    print(amount_list)
                    print(sum(amount_list))

                    print(total1)
                    messagebox.showinfo("ghjg", str(amount) + "total sum : "+str(sum(amount_list)) )

                    #mainscreen_l9 = Label(mainScreen)
                    #mainscreen_l9.place(x=750, y=380)
                    mainscreen_l9.config(background="white", font=(("Helvetica", 13)), text="Total : " + str(sum(amount_list)))

                    #def net_total():

                    #pass



            def del_cart():

                #try:

                    for nm in mainScreen_tree.selection():

                        r1 = mainScreen_tree.item(nm, 'values')[2]
                        print(r1)

                    x1 = mainScreen_tree.selection()[0]
                    mainScreen_tree.delete(x1)



                    amount_list.pop(amount_list.index(int(r1)))
                    print(sum(amount_list))
                    mainscreen_l9.config(background="white", font=(("Helvetica", 13)),text="Total : " + str(sum(amount_list)))
                    print(amount_list)
                    #total2 = mainScreen_tree.item(items_val2)['values']





                #except:
                    #messagebox.showwarning("Warning", "Firstly, You must select a row to delete")


            mainscreen_l9 = Label(mainScreen)
            mainscreen_l9.place(x=750, y=380)
            mainscreen_l9.config(background="white", font=(("Helvetica", 13)), text="Total : " + str(sum(amount_list)))

            mainScreen_b3 = Button(mainScreen, text=" ADD TO CART", command=move_cart)
            mainScreen_b3.place(x=342, y=310)

            mainScreen_b4 = Button(mainScreen, text=" REMOVE FROM CART", command=del_cart)
            mainScreen_b4.place(x=742, y=420)

            def open_cal():
                from subprocess import call
                call(["calc.exe"])

            mainScreen_b5 = Button(mainScreen, text=" Calculator", command=open_cal)
            mainScreen_b5.place(x=1100, y=20)

            mainScreen_b6 = Button(mainScreen, text="Find Total")
            mainScreen_b6.place(x=900, y=580)




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

    forget_c1 = Combobox(forget_win, width=30)
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
