from tkinter import *

win = Tk() 
win.geometry("312x330")  
win.resizable(0, 0)  
win.title("Calculator")

# function for input button
def btn_click(item,text=None):
    global expression
    expression = expression + str(item)
    it.set(expression)

# function for clear the input field
def bt_clear(): 
    global expression
    expression = "" 
    it.set("")

# to calculate the expression 
def bt_equal():
    global expression
    result = str(eval(expression))
    it.set(result)
    expression = result

class button:
    
    def __init__(self, text, row, column):
        self.text = text
        self.row = row
        self.column = column
        self.button = Button(btns_frame, text = self.text, fg = "black", width = 10, height = 3, bd = 0, bg = "white", cursor = "hand2", command = lambda: btn_click(self.text))
        self.button.grid(row = self.row, column = self.column, padx = 1, pady = 1)

expression = ""
 
it = StringVar()
 
# frame for the input field
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(fill="both",padx=10,pady=10)
 
#input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=it, width=20, bg="#eee", bd=0, justify=RIGHT, fg="#000",state='readonly').grid(row=0, column=0)

#'Frame' for the button 
btns_frame = Frame(win, bg="red")
btns_frame.pack()

one=button(1,0,0)
two=button(2,0,1)
three=button(3,0,2)
four=button(4,1,0)
five=button(5,1,1)
six=button(6,1,2)
seven=button(7,2,0)
eight=button(8,2,1)
nine=button(9,2,2)
zero=button(0,3,0)
point=button(".",3,1)
clear=button("C",3,2)
clear.button.configure(command=bt_clear)
plus=button("+",0,3)
minus=button("-",1,3)
multiply=button("*",2,3)
divide=button("/",3,3)
equal=button("=",4,0)
equal.button.configure(command=bt_equal,width=44)
equal.button.grid(row=4,column=0,columnspan=4)

win.mainloop()