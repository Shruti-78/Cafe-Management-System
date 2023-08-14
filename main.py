from tkinter import *
import time

# def of sys
root_resto = Tk()
root_resto.geometry("1000x600")
root_resto.title("My App")

# time
localtime = time.asctime(time.localtime(time.time()))

# framing
name_frame = Frame(root_resto, bg="black", width=1600, height=10)
name_frame.pack(side=TOP, fill=X)

bottom = Frame(root_resto, bg="misty rose", width=2000, height=300)
bottom.pack(fill=X, anchor=S)
main_lbl = Label(name_frame, font=('Segoe Print', 10,), text=localtime, bg="black", fg="white", anchor=W)
main_lbl.pack(anchor=W)
main_lbl = Label(name_frame, font=('Segoe Print', 25, 'bold'), text="Cafe Management System",  bg="black", fg="white",
                 justify=CENTER)
main_lbl.pack(anchor=N)

# variable datatype assignment
Order_no = StringVar()
Name = StringVar()
Mobile = StringVar()
Tea = StringVar()
Pattice = StringVar()
Bread_roll = StringVar()
Sandwich = StringVar()
Toast_sandwich = StringVar()
Idli = StringVar()
Poha = StringVar()
Lemonade = StringVar()
Watermelon_juice = StringVar()
Total = StringVar()
Paid = StringVar()
Change = StringVar()

Order_no.set("")
Name.set("")
Mobile.set("")
Tea.set(0)
Pattice.set(0)
Bread_roll.set(0)
Sandwich.set(0)
Toast_sandwich.set(0)
Idli.set(0)
Poha.set(0)
Lemonade.set(0)
Watermelon_juice.set(0)
Total.set(0)
Paid.set(0)
Change.set(0)


# labels and entries
# order
#order = Label(bottom, font=('Calibri', 15, 'bold'), text="MENU", bg="salmon", fg="black", bd=5, anchor=W).grid(row=2, column=6, padx=50, pady=5)
l_orderno = Label(bottom, font=('Calibri', 15, 'bold'), text="Order No.", bg="salmon", fg="black", bd=5, anchor=W).grid( row=7, column=2, padx=50, pady=5)
e_orderno = Entry(bottom, font=('Calibri', 15, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=Order_no).grid(row=7, column=3, padx=50, pady=5)

# name
l_name = Label(bottom, font=('Calibri', 15, 'bold'), text="Name", bg="salmon", fg="black", bd=5, anchor=W).grid(row=5, column=2, padx=50, pady=5)
e_name = Entry(bottom, font=('Calibri', 15, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=Name).grid(row=5, column=3, padx=50, pady=5)

# mobile no
l_mobile = Label(bottom, font=('Calibri', 15, 'bold'), text="Mobile No.", bg="salmon", fg="black", bd=5, anchor=W).grid(row=9, column=2, padx=50, pady=5)
e_mobile = Entry(bottom, font=('Calibri', 15, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=Mobile).grid( row=9, column=3, padx=50, pady=5)

# items
l_tea = Label(bottom, font=('Calibri', 15, 'bold'), text="Tea", fg="black",bg="salmon", bd=5, anchor=W).grid(row=3, column=5, padx=50, pady=10)
e_tea = Entry(bottom, font=('Calibri', 15, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=Tea).grid(row=3, column=6, padx=50, pady=10)

l_pattice = Label(bottom, font=('Calibri', 15, 'bold'), text="Pattice", fg="black",bg="salmon", bd=5, anchor=W).grid(row=4, column=5, padx=50, pady=10)
e_pattice = Entry(bottom, font=('Calibri', 15, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=Pattice).grid(row=4, column=6, padx=50, pady=10)

l_bread_roll = Label(bottom, font=('Calibri', 15, 'bold'), text="Bread roll", fg="black",bg="salmon", bd=5, anchor=W).grid(row=5, column=5, padx=50, pady=10)
e_bread_roll = Entry(bottom, font=('Calibri', 15, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=Bread_roll).grid(row=5, column=6, padx=50, pady=10)

l_sandwich = Label(bottom, font=('Calibri', 15, 'bold'), text="Sandwich",bg="salmon", bd=5, anchor=W).grid(row=6, column=5, padx=50, pady=10)
e_sandwich = Entry(bottom, font=('Calibri', 15, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=Sandwich).grid(row=6, column=6, padx=50, pady=10)

l_toast_sandwich = Label(bottom, font=('Calibri', 15, 'bold'), text="Toast sandwich",bg="salmon", bd=5, anchor=W).grid(row=7, column=5, padx=50, pady=10)
e_toast_sandwich = Entry(bottom, font=('Calibri', 15, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=Toast_sandwich).grid(row=7, column=6, padx=50, pady=10)

l_idli = Label(bottom, font=('Calibri', 15, 'bold'), text="Idli", bd=5,bg="salmon", anchor=W).grid(row=8, column=5, padx=50, pady=10)
e_idli = Entry(bottom, font=('Calibri', 15, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=Idli).grid( row=8, column=6, padx=50, pady=10)

l_poha = Label(bottom, font=('Calibri', 15, 'bold'), text="Poha", bd=5, bg="salmon",anchor=W).grid(row=9, column=5, padx=50, pady=10)
e_poha = Entry(bottom, font=('Calibri', 15, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=Poha).grid(row=9, column=6, padx=50, pady=10)

l_lemonade = Label(bottom, font=('Calibri', 15, 'bold'), text="Lemonade", bd=5,bg="salmon", anchor=W).grid(row=10, column=5, padx=50, pady=10)
e_lemonade = Entry(bottom, font=('Calibri', 15, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=Lemonade).grid(row=10, column=6, padx=50, pady=10)

l_watermelon_juice = Label(bottom, font=('Calibri', 15, 'bold'), text="Watermelon juice", bg="salmon",fg="black", bd=5, anchor=W).grid(row=11, column=5, padx=50, pady=9)
e_watermelon_juice = Entry(bottom, font=('Calibri', 15, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=Watermelon_juice).grid(row=11, column=6, padx=50, pady=9)

# paid
l_paid = Label(bottom, font=('Calibri', 15, 'bold'), text="Paid", fg="black",bg="salmon", bd=5, anchor=W).grid(row=12, column=5, padx=50, pady=8)#(row=13, column=5, padx=50, pady=5)
e_paid = Entry(bottom, font=('Calibri', 15, 'bold'), bd=6, insertwidth=4, justify='right', textvariable=Paid).grid(row=12, column=6, padx=50, pady=8)#(row=13, column=6, padx=50, pady=5)

# total
#l_total = Label(bottom, font=('Calibri', 12, 'bold'), text="Total", fg="black", bd=5, anchor=W).grid(row=13, column=5, padx=50, pady=5)
e_total = Label(bottom, font=('Calibri', 15, 'bold'), bd=6,width=20, bg="white", justify='right', textvariable=Total).grid(row=13, column=6, padx=50, pady=8)

# change
#l_change = Label(bottom, font=('Calibri', 10, 'bold'), text="Change", fg="black", bd=5, anchor=W).grid(row=14, column=5, padx=50, pady=5)
e_change = Label(bottom, font=('Calibri', 15, 'bold'), bd=6,width=20, bg="white", justify='right', textvariable=Change).grid(row=14, column=6, padx=50, pady=10)


def total_cost():
    # charges
    overall_cost = (int(Tea.get()) * 12) + (int(Pattice.get()) * 15) + (int(Bread_roll.get()) * 15) + (
                int(Sandwich.get()) * 30) + (int(Toast_sandwich.get()) * 40) + (int(Idli.get()) * 30) + (
                               int(Poha.get()) * 18) + (int(Lemonade.get()) * 15) + (int(Watermelon_juice.get()) * 30)
    Total.set(overall_cost)


def remainder():
    remainder_money = (int(Paid.get()) - int(Total.get()))
    Change.set(remainder_money)


def reset():
    Order_no.set("")
    Name.set("")
    Mobile.set("")
    Tea.set(0)
    Pattice.set(0)
    Bread_roll.set(0)
    Sandwich.set(0)
    Toast_sandwich.set(0)
    Idli.set(0)
    Poha.set(0)
    Lemonade.set(0)
    Watermelon_juice.set(0)
    Total.set(0)
    Paid.set(0)
    Change.set(0)


def menu():
    root_menu = Tk()
    root_menu.geometry("500x600")
    root_menu.title("Menu Card")



    item = Label(root_menu, font=("Calibri", 18, "bold"), text="Item", fg="salmon", bd=10)
    item.grid(row=0, column=0)
    label_price = Label(root_menu, font=("Calibri", 18, "bold"), text="Price", fg="salmon", bd=10)
    label_price.grid(row=0, column=3)

    label_tea = Label(root_menu, font=("Calibri", 18, "bold"), text="Tea", fg="black", bd=10)
    label_tea.grid(row=1, column=0)
    label_price_tea = Label(root_menu, font=("Calibri", 18, "bold"), text="12/-", fg="black", bd=10)
    label_price_tea.grid(row=1, column=3)

    label_pattice = Label(root_menu, font=("Calibri", 18, "bold"), text="Pattice",fg="black", bd=10)
    label_pattice.grid(row=3, column=0)
    label_price_pattice = Label(root_menu, font=("Calibri", 18, "bold"), text="15/-", fg="black", bd=10)
    label_price_pattice.grid(row=3, column=3)

    label_bread_roll = Label(root_menu, font=("Calibri", 18, "bold"), text="Bread Roll", fg="black", bd=10)
    label_bread_roll.grid(row=4, column=0)
    label_price_bread_roll = Label(root_menu, font=("Calibri", 18, "bold"), text="15/-", fg="black", bd=10)
    label_price_bread_roll.grid(row=4, column=3)

    label_sandwich = Label(root_menu, font=("Calibri", 18, "bold"), text="Sandwich", fg="black", bd=10)
    label_sandwich.grid(row=5, column=0)
    label_price_sandwich = Label(root_menu, font=("Calibri", 18, "bold"), text="30/-",fg="black", bd=10)
    label_price_sandwich.grid(row=5, column=3)

    label_toast_sandwich = Label(root_menu, font=("Calibri", 18, "bold"), text="Toast Sandwich", fg="black", bd=10)
    label_toast_sandwich.grid(row=6, column=0)
    label_price_toast_sandwich = Label(root_menu, font=("Calibri", 18, "bold"), text="40/-", fg="black", bd=10)
    label_price_toast_sandwich.grid(row=6, column=3)

    label_idli = Label(root_menu, font=("CalibriT", 18, "bold"), text="Idli",fg="black", bd=10)
    label_idli.grid(row=7, column=0)
    label_price_idli = Label(root_menu, font=("Calibri", 18, "bold"), text="30/-",fg="black", bd=10)
    label_price_idli.grid(row=7, column=3)

    label_poha = Label(root_menu, font=("Calibri", 18, "bold"), text="Poha",fg="black", bd=10)
    label_poha.grid(row=8, column=0)
    label_price_poha = Label(root_menu, font=("Calibri", 18, "bold"), text="18/-",fg="black", bd=10)
    label_price_poha.grid(row=8, column=3)

    label_lemonade = Label(root_menu, font=("Calibri", 18, "bold"), text="Lemonade", fg="black", bd=10)
    label_lemonade.grid(row=9, column=0)
    label_price_lemonade = Label(root_menu, font=("Calibri", 18, "bold"), text="15/-", fg="black", bd=10)
    label_price_lemonade.grid(row=9, column=3)

    label_watermelon_juice = Label(root_menu, font=("Calibri", 18, "bold"), text="Watermelon juice",fg="black", bd=10)
    label_watermelon_juice.grid(row=10, column=0)
    label_price_watermelon_juice = Label(root_menu, font=("Calibri", 18, "bold"), text="30/-",fg="black", bd=10)
    label_price_watermelon_juice.grid(row=10, column=3)

    button_close = Button(root_menu,font=("Calibri", 18, "bold"), text="Close menu", bg="black", fg="salmon", command=root_menu.destroy).grid(row=11,
                                                                                                               column=2,pady = 10)
    root_menu.mainloop()


def rating():
    root_rating = Tk()
    root_rating.geometry("600x500")

    fill = Frame(root_rating, bg="black", width=2000, height=100)
    fill.pack(side=TOP, fill=X)
    name1 = StringVar()

    top = Frame(root_rating, bg="misty rose", width=2000, height=800)
    top.pack()

    label_thank = Label(root_rating, font=("Calisto MT", 15, "bold"), text="Thanks for Visiting!", bg="black",fg="white", padx=180).place(x=10, y=5)
    label_feed = Label(root_rating, font=("calisto MT", 15),text="We're glad you chose us ! Please tell us how it was!",   bg="black",fg="white", padx=30).place(x = 20, y =40)

    # name
    label_name = Label(root_rating, font=('vardana', 15), text="Name:-", bg="salmon", fg="black", bd=10, anchor=W).place(
        x=10, y=100)
    entry_name = Entry(root_rating, font=('vardana', 15), bd=6, insertwidth=2,bg="white", fg="black", justify='right',
                       textvariable=name1).place(x=15, y=150)

    # radiobutton
    label_rate = Label(root_rating, font=('vardana', 15), text="How would you rate us?", bg="salmon", fg="black", bd=10,
                       anchor=W).place(x=10, y=215)
    cb1 = IntVar()

    c1 = Radiobutton(root_rating, font=('Calibri', 10, "bold"), bg="white", text="Excellent", variable=cb1,value=1)
    c1.place(x=15, y=265)
    c2 = Radiobutton(root_rating, font=('Calibri', 10, "bold"), text="Good", bg="white", variable=cb1, value=2)
    c2.place(x=120, y=265)
    c3 = Radiobutton(root_rating, font=('Calibri', 10, "bold"), text="Average", bg="white", variable=cb1, value=3)
    c3.place(x=220, y=265)
    c4 = Radiobutton(root_rating, font=('Calibri', 10, "bold"), text="Needs improvement", bg="white", variable=cb1,value=4)
    c4.place(x=320, y=265)

    submit = Button(root_rating, font=("Calibri", 15), text="Submit", fg="salmon", bg="black", bd=2,
                    command=root_rating.destroy).place(x=145, y=430)
    submit.place(x=200, y=275)

    root_rating.mainloop()


# butons
button_menu = Button(bottom, font=('Calibri', 16, 'bold'), text="Menu Card", bg="black", fg="white", bd=3, padx=5, pady=5, width=8, command=menu).grid(row=11, column=3)

button_total = Button(bottom, font=('Calibri', 12, 'bold'), text="Total(in Rs.)", fg="maroon", bd=3, padx=5, pady=5, width=10, command=total_cost).grid(row=13, column=5, padx=50, pady=5)

button_change = Button(bottom, font=('Calibri', 12, 'bold'), text="Change(in Rs.)", fg="maroon", bd=3, padx=5, pady=5, width=12, command=remainder).grid(row=14, column=5, padx=50, pady=5)

button_reset = Button(bottom, font=('Calibri', 16, 'bold'), text="Reset",bg="black", fg="white", bd=3, padx=5, pady=5, width=6, command=reset).grid(row=9, column=10, padx=50, pady=5)

button_rating = Button(bottom, font=('Calibri', 16, 'bold'), text="Rating", bg="black",fg="white", bd=3, padx=5, pady=5, width=8, command=rating).grid(row=7, column=10)

button_close = Button(bottom, font=('Calibri', 16, 'bold'), text="Close",bg="black", fg="salmon", bd=3, padx=5,pady=5, width=12, command=root_resto.destroy).grid(row=11, column=10, padx=50, pady=5)


root_resto.mainloop()
