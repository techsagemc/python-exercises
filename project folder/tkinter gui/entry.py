from tkinter import *
#create screen widget step1
window = Tk()
#Create title 
window.title("Simple Calculator")
#This is how you enter an input box
e =Entry(window, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#This will put default text inside your input box
#e.insert(0,"Enter Your Name:  ")
#e.get retrieves info from input click
def button_click(number):
    # e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def button_clear():
    e.delete(0, END)
    
def button_add():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    # e.delete(0, END)
    
    
def button_equal():
    next_number = e.get()
    global n_num
    n_num = int(next_number)
    e.delete(0, END)
    
    e.insert(0, f_num + n_num)
    
#define buttons
button1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
add_button = Button(window, text="+", padx=39, pady=20, command=button_add)
equal_button = Button(window, text="=", padx=87, pady=20, command=button_equal)
clear_button = Button(window, text="C", padx=87, pady=20, command=button_clear)
 
#put buttons on the screen
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

add_button.grid(row=5, column=0)
equal_button.grid(row=5, column=1, columnspan=2)
clear_button.grid(row=4, column=1, columnspan=2)


# def myclick():
    # hello = "Hello " + e.get() + "!!"
    # windowlabel1 = Label(window, text=hello)#.grid(row=0, column=0)
    # windowlabel1.pack()
    
#you can make buttons work by creating a function that does something, then using (command="whatever the function name is without the parentheses") within the button
# mybutton = Button(window, text="Enter your name", command=button_add)#can use status=""
#creating a label widget
# windowlabel2 = Label(window, text="My name is Michael Cook")#.grid(row=0, column=0)

#push it to the screen. (we can do it in 1 step if needed)(see note on line 5 and 6)
# windowlabel1.grid(row=0, column=0)
# windowlabel2.grid(row=1, column=5)


window.mainloop()