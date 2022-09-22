from tkinter import *

window = Tk()

def myclick():
    windowlabel1 = Label(window, text="Look! I clicked a Button!")#.grid(row=0, column=0)
    windowlabel1.pack()
    
#you can make buttons work by creating a function that does something, then using (command="whatever the function name is without the parentheses") within the button
mybutton = Button(window, text="Click Me!", padx=50, pady=50, command=myclick)#can use status=
mybutton.pack()
#creating a label widget
# windowlabel2 = Label(window, text="My name is Michael Cook")#.grid(row=0, column=0)

#push it to the screen. (we can do it in 1 step if needed)(see note on line 5 and 6)
# windowlabel1.grid(row=0, column=0)
# windowlabel2.grid(row=1, column=5)


window.mainloop()