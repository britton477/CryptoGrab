from tkinter import *

# Must happen first
root = Tk()

# Name of the program
root.title("Simple Calculator")

# Entry point for numbers
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Function to add the numbers
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    return


# Function to clear the entry(e)
def button_clear():
    e.delete(0, END)
    return


# Function for the addition
def button_add():
    first_num = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_num)
    e.delete(0, END)


# Function for subtraction
def button_subtract():
    first_num = e.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_num)
    e.delete(0, END)


# Function for multiply
def button_multiply():
    first_num = e.get()
    global f_num
    global math
    math = 'multiply'
    f_num = int(first_num)
    e.delete(0, END)


# Function for divide
def button_divide():
    first_num = e.get()
    global f_num
    global math
    math = 'divide'
    f_num = int(first_num)
    e.delete(0, END)


# Function to equal
def button_equal():
    sec_num = e.get()
    e.delete(0, END)

    if math == 'addition':
        e.insert(0, f_num + int(sec_num))

    if math == 'subtraction':
        e.insert(0, f_num - int(sec_num))

    if math == 'multiply':
        e.insert(0, f_num * int(sec_num))

    if math == 'divide':
        e.insert(0, f_num / int(sec_num))


# Define buttons
button1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_pl = Button(root, text='+', padx=39, pady=20, command=button_add)
button_eq = Button(root, text='=', padx=89, pady=20, command=button_equal)
button_cl = Button(root, text='Clear', padx=79, pady=20, command=button_clear)
button_sub = Button(root, text='-', padx=40, pady=20, command=button_subtract)
button_mul = Button(root, text='x', padx=40, pady=20, command=button_multiply)
button_div = Button(root, text='÷', padx=40, pady=20, command=button_divide)


# Put the buttons on the screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)
button_cl.grid(row=4, column=1, columnspan=2)
button_eq.grid(row=5, column=1, columnspan=2)
button_pl.grid(row=5, column=0)
button_sub.grid(row=6, column=0)
button_mul.grid(row=6, column=1)
button_div.grid(row=6, column=2)


root.mainloop()
