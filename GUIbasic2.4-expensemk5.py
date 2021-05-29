from tkinter import *
from tkinter import ttk, messagebox
import csv
from PIL import Image, ImageTk
from datetime import datetime
import csv
#if tkinter is HTML then tkk is CSS
GUI = Tk ()
GUI.resizable(width=False, height=False)
GUI.title("saving all your expenses by g00gle@yandex.ru")
GUI.geometry("700x700+500+125")
###################MENU!######################
menubar = Menu(GUI)
GUI.config(menu=menubar)
#file menu
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Import CSV")
filemenu.add_command(label="Export to Google Sheets")
#help menu
def About():
    messagebox.showinfo("about","hello, this program is for keeping track of your balance. \n Commands:\n Tab to move to next box \n Enter to save.")
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About",command=About)
helpmenu.add_command(label="Donate")
#donate menu
def Donate():
    messagebox.showinfo("Donate","Bank Acc:5555555555555555555")
donatemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Donate", menu=donatemenu)
##############################################
notebook = ttk.Notebook()
notebook.pack(fill=BOTH, expand=1)
#B1 = Button(GUI,text="Hello")
#B1.pack(ipadx=50,ipady=20) #pack() enter button into main GUI
F1 = Frame(notebook, height=500, width=500, cursor="crosshair")
F1.place(x=100,y=50)
F2 = Frame(notebook, height=500, width=500, cursor="wait")
F2.place(x=100,y=50)
image1 = ImageTk.PhotoImage(Image.open("wallet.png"))
image2 = ImageTk.PhotoImage(Image.open("plus.png"))
image3 = ImageTk.PhotoImage(Image.open("list.png"))
image4 = ImageTk.PhotoImage(Image.open("writeDown.png"))
Picture = ttk.Label(F1, image=image1)
Picture.pack()
notebook.add(F1, text=f'{"Add Expense":^{30}}', image=image2, compound=TOP)
notebook.add(F2, text=f'{"Expense List":^{30}}', image=image3, compound=TOP)
days = {"Mon":"จันทร์",
        "Tue":"อังคาร",
        "Wed":"พุธ",
        "Thu":"พฤหัสบดี",
        "Fri":"ศุกร์",
        "Sat":"เสาร์",
        "Sun":"อาทิตย์ "}
def Save(event=None):
    expense = v_expense.get()
    price = v_price.get()
    amount = v_amount.get()
    if expense == "":
        print("no data")
        messagebox.showwarning("ERROR!","No data")
        return
    elif price == "":
        print("no data")
        messagebox.showwarning("ERROR!","No data")
        return
    elif amount == "":
        print("no data")
        messagebox.showwarning("ERROR!","No data")
        return
    try:
        totalPrice = float(price) * float(amount)
        today = datetime.now().strftime("%a")
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dt = days[today] + "-" + dt
        print(f"bought: {expense} | price(each): {price} | amount: {amount} | total price: {totalPrice}")
        #clear old data
        v_expense.set('')
        v_price.set('')
        v_amount.set('')
        text = (f"bought: {expense} | price(each): {price} \n ")
        text = text + (f"amount: {amount} | total price: {totalPrice}")
        v_result.set(text)
        #add data to csv
        with open("savedataMK2.csv","a",encoding="utf-8",newline="") as f:
                #with is open file and close it after
                #a = store to add data, w is 1 record
                fw = csv.writer(f) #add function to write data
                data = [dt,expense,price,amount,totalPrice]
                fw.writerow(data)
        E1.focus()
        expensesTable.delete(*expensesTable.get_children())
        updateTable()
        #updateRecord()
    except Exception as e:
        print("error",e)
        messagebox.showwarning("ERROR!","the information provided is incorrect")
        expense = v_expense.get()
        price = v_price.get()
        amount = v_amount.get() 
#make it ok to click enter
GUI.bind("<Return>",Save)
FONT1 = ("Comic Sans MS",20)
#--------text1---------
L = ttk.Label(F1,text="expenses data",font=FONT1).pack()
v_expense = StringVar() #StringVar = special Var to store data in GUI
E1 = ttk.Entry(F1,textvariable=v_expense,font=FONT1)
E1.pack()
#--------endoftext1--------
#--------text2---------
L = ttk.Label(F1,text="price (USD)",font=FONT1).pack()
v_price = StringVar() #StringVar = special Var to store data in GUI
E2 = ttk.Entry(F1,textvariable=v_price,font=FONT1)
E2.pack()
#--------endoftext2--------
#--------text3---------
L = ttk.Label(F1,text="amount",font=FONT1).pack()
v_amount = StringVar() #StringVar = special Var to store data in GUI
E3 = ttk.Entry(F1,textvariable=v_amount,font=FONT1)
E3.pack()
#--------endoftext3--------
B2 = ttk.Button(F1,text=f'{"Save": >{15}}', image=image4, compound=LEFT, command=Save)
B2.pack(ipadx=50,ipady=20,pady=20)
v_result = StringVar() 
v_result.set("-----------total------------")
result = ttk.Label(F1, textvariable=v_result,font=FONT1,foreground="green")
result.pack(pady=10)
#---------F2time------------
#---------------------------
def reader():
    with open("savedataMK2.csv",newline="",encoding="utf-8") as f:
        fr = csv.reader(f)
        data = list(fr)
        rs = data
    return data
header = ["Date","Expense","Price","Amount","Total Price" ]
expensesTable = ttk.Treeview(F2, columns=header,show="headings",height=10)
expensesTable.pack()
for h in header:
    expensesTable.heading(h,text=h)
headerwidth = [170,200,110,110,110]
for h,w in zip(header,headerwidth):
    expensesTable.column(h,width=w)
def updateTable():
    expensesTable.delete(*expensesTable.get_children())
    data = reader()
    for d in data:
        expensesTable.insert("",0,value=d)
updateTable()
print("GET CHILD:",expensesTable.get_children())
GUI.bind("<Tab>",lambda x: E2.focus())
GUI.mainloop()