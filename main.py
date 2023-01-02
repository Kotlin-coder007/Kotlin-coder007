#class10_ai_project
#Innovated by:Selvakrishna(34),Saai Subrahmanian(30),Shriharan(35),Aswath Arumugam(xx),Hritick Raj(xx)


#project_starts...

#importing_required_packages
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import numpy
import pandas as pd
import matplotlib.pyplot as plt


#declaring_functions

def cred_login():
    #login_functions
    db=open('database.txt',"r")
    username=e1.get()
    password=e2.get()
    if not len(username or password)<1:
        d=[]
        f=[]
        for i in db:
            a,b=i.split(",")
            b=b.strip()
            d.append(a)
            f.append(b)
        data=dict(zip(d,f))
        try:
            if data[username]:
                try:
                    if password==data[username]:
                        messagebox.showinfo('success','Logined successfully!')
                        user_page()
                except:
                    messagebox.showinfo('Status','Success')
            else:
                messagebox.showinfo('Error','Username doesnt exist!')
        except:
            messagebox.showinfo('Error','Login error')

def main_page():
    #login_page_setup
    splash.destroy()
    main=Tk()
    main.title('xConstellation')
    main.geometry('300x200')
    Label(main,text='Username').place(x=20,y=20)
    Label(main,text='Password').place(x=20,y=70)
    global e1,e2
    e1=Entry(main,bd=1)
    e1.place(x=140,y=20)
    e2=Entry(main,bd=1)
    e2.place(x=140,y=70)
    Button(main,text='Login',command=cred_login).place(x=100,y=120)
    Button(main,text='Signup',command=signup).place(x=160,y=120)


def redirect():
    #redirection_main_page
    main_page()

def cred_signup():
    #signup_functions
    global c,d
    user_page()
    fell=open('database.txt','r')
    c=e3.get()
    d=e7.get()
    y=[]
    z=[]
    for i in fell:
        a,b=i.split(",")
        b=b.strip()
        y.append(a)
        z.append(b)
    credential=dict(zip(y,z))
    print(credential)
    if c != '' :
       db=open('database.txt',"a")
       db.write(c+','+d+'\n')
       messagebox.showinfo('Status','Successfully Joined !')
    else:
        messagebox.showinfo('Error','Username or Password is Blank !')

    
def signup():
    #signup_page_setup
    initial=Tk()
    initial.title('sign up')
    initial.geometry('500x500')
    Label(initial,text='Username').place(x=20,y=20)
    Label(initial,text='Class').place(x=20,y=60)
    Label(initial,text='Section').place(x=20,y=100)
    Label(initial,text='School').place(x=20,y=140)
    Label(initial,text='Password').place(x=20,y=180)
    global e3,e4,e5,e6,e7
    e3=Entry(initial,bd=1)
    e3.place(x=140,y=20)
    e4=Entry(initial,bd=1)
    e4.place(x=140,y=60)
    e5=Entry(initial,bd=1)
    e5.place(x=140,y=100)
    e6=Entry(initial,bd=1)
    e6.place(x=140,y=140)
    e7=Entry(initial,bd=1)
    e7.place(x=140,y=180)
    Button(initial,text='Signup',command=cred_signup).place(x=140,y=220)


def add():
    #add_button_function_in_usrpage
    global count
    name=txtName.get()
    age=txtAge.get()
    dob=txtDob.get()
    gender=comboGender.get()
    email=txtEmail.get()
    cont=txtContact.get()
    mark=txtMark.get()
    x=open("DATASET.csv","a")
    x.write(name+',')
    x.write(age+',')
    x.write(dob+',')
    x.write(gender+',')
    x.write(email+',')
    x.write(cont+',')
    x.write(mark+'\n')
    x.close() 
    table.insert(parent='',index='end',iid=count,text="",values=(txtName.get(),txtAge.get(),txtDob.get(),comboGender.get(),txtEmail.get(),txtContact.get()))
    count+=1

    
def clear():
    #clear_button_function_in_usrpage
    txtName.delete(0,END)
    txtAge.delete(0,END)
    txtDob.delete(0,END)
    txtEmail.delete(0,END)
    txtContact.delete(0,END)
    txtMark.delete(0,END)

    
def remove():
    #remove_button_function_in_usrpage
    global z
    x=table.selection()[0]
    table.delete(x)
    z.drop(int(x),axis=0,inplace=True)
    
def plot():
    #visualize_button_function_in_usrpage
    x_data=z['Name']
    y_data=z['C.G.P.A']
    plt.bar(x_data,y_data,width=0.1,align='center')
    plt.xlabel('Students')
    plt.ylabel('Percentile')
    plt.title('Overall C.G.P.A Perfomance')
    plt.show()

def user_page():
    #user_page_setup
    root = Tk()
    root.title("Student Management System ----XconsTellation")
    root.geometry("1920x1080+0+0")
    root.config(bg="#2c3e50")
    root.state("zoomed")
    name = str()
    age = str()
    dob = str()
    gender = str()
    email = str()
    cont = str()
    address=str()
    global txtName,txtAge,txtDob,txtEmail,txtContact,txtMark,comboGender,z_rows,z,table
    entries_frame = Frame(root, bg="#535c68")
    entries_frame.pack(side=TOP, fill=X)
    title = Label(entries_frame, text="Student Management System", font=("Helvetica", 18, "bold"), bg="#535c68", fg="white")
    title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
    lblName = Label(entries_frame, text="Name", font=("Calibri", 16), bg="#535c68", fg="white")
    lblName.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    txtName = Entry(entries_frame, font=("Calibri", 16), width=30)
    txtName.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    lblAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="#535c68", fg="white")
    lblAge.grid(row=1, column=2, padx=10, pady=10, sticky="w")
    txtAge = Entry(entries_frame, font=("Calibri", 16), width=30)
    txtAge.grid(row=1, column=3, padx=10, pady=10, sticky="w")
    lbldob = Label(entries_frame, text="D.O.B", font=("Calibri", 16), bg="#535c68", fg="white")
    lbldob.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    txtDob = Entry(entries_frame, font=("Calibri", 16), width=30)
    txtDob.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#535c68", fg="white")
    lblEmail.grid(row=2, column=2, padx=10, pady=10, sticky="w")
    txtEmail = Entry(entries_frame, font=("Calibri", 16), width=30)
    txtEmail.grid(row=2, column=3, padx=10, pady=10, sticky="w")
    lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#535c68", fg="white")
    lblGender.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28,  state="readonly")
    comboGender['values'] = ("Male", "Female")
    comboGender.grid(row=3, column=1, padx=10, sticky="w")
    lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#535c68", fg="white")
    lblContact.grid(row=3, column=2, padx=10, pady=10, sticky="w")
    txtContact = Entry(entries_frame, font=("Calibri", 16), width=30)
    txtContact.grid(row=3, column=3, padx=10, sticky="w")
    lblMark = Label(entries_frame, text="C.G.P.A", font=("Calibri", 16), bg="#535c68", fg="white")
    lblMark.grid(row=1, column=4, padx=10, pady=10, sticky="w")
    txtMark = Entry(entries_frame, font=("Calibri", 16), width=30)
    txtMark.grid(row=1, column=5, padx=10, pady=10, sticky="w")

    btn_frame = Frame(entries_frame, bg="#535c68")
    btn_frame.grid(row=6,column=0, columnspan=4, padx=10, pady=10, sticky="w")
    btnAdd =Button(btn_frame, command=add, text="Add Details", width=15,font=("Calibri", 16, "bold"), fg="white",bg="#16a085", bd=0).grid(row=0,column=0)
    btnDelete = Button(btn_frame,command=remove, text="Delete Details", width=15, font=("Calibri", 16,"bold"), fg="white", bg="#c0392b", bd=0).grid(row=0, column=1, padx=10)
    btnClear = Button(btn_frame, command=clear, text="Clear Details", width=15,font=("Calibri", 16, "bold"), fg="white", bg="#f39c12",bd=0).grid(row=0, column=2, padx=10)
    btnPlot = Button(btn_frame, command=plot, text="Visualize", width=15,font=("Calibri", 16, "bold"), fg="white", bg="#2980b9",bd=0).grid(row=0, column=3, padx=10)
    z=pd.read_csv('DATASET.csv')
    tree_frame = Frame(root, bg="#ecf0f1")
    tree_frame.place(x=0, y=290, width=1980, height=900)
    table = ttk.Treeview(tree_frame)
    table['columns']=(tuple(z.loc[:]))
    table.column('#0',width=0)
    table.heading("#0",text='ID')
    table.heading("Name",text="Name",anchor=W)
    table.heading("Age",text='Age')
    table.heading("D.O.B",text="DOB")
    table.heading("Gender",text="Gender")
    table.heading("Email",text="Email")
    table.heading("Contact",text="Contact")
    table.heading("C.G.P.A",text="C.G.P.A")
    table.pack(fill=X)
    z_rows=z.to_numpy().tolist()
    global count
    count=0
    for data in z_rows:
        table.insert('','end',iid=count,text="",values=(data))
        count+=1
    print(z)

#opening_splash_screen
splash=Tk()
splash.title('Loading')
splash.geometry('511x337')
bg=PhotoImage(file="background.png")
bglabel=Label(splash,image=bg)
bglabel.place(x=0,y=0)
cop_label=Label(text='© xConstellation and its Affiliates')
cop_label.place(x=150,y=300)
Label(splash,text='xConstellation').pack()
Label(splash,text='Student Database Management System').pack()
splash_progress=ttk.Progressbar(splash,orient=HORIZONTAL,length=300,mode='determinate')
splash_progress.start(20)
splash_progress.place(x=80,y=160)
splash.after(10000,main_page)


#End.... :)


