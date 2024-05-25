from tkinter import *

win = Tk() 
win.geometry("312x348")  
win.resizable(0, 0)  
win.title("Calculator")
win.iconbitmap('cal logo.ico')
win.configure(background="white")

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# function for clear the input field
def bt_clear(): 
    global expression 
    expression = "" 
    input_text.set("")

def bt_back():
    global expression
    expression = expression[:-1]
    input_text.set(expression)

 # to calculate the expression 
def bt_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""

# making a class for the buttons
class button:
    def color(self, fg=None, bg=None):
        self.button.config(fg=fg, bg=bg)

    def __init__(self, text, row, column,frame=None,command=None):
        self.text = text
        self.row = row
        self.column = column
        self.command = command
        self.frame = btns_frame if frame is None else frame
        self.button = Button(self.frame, text = self.text, fg = "white", width = 10, height = 3, bd = 0, bg = "black", cursor = "hand2", command = self.command if command is not None else lambda: btn_click(self.text))
        self.button.grid(row = self.row, column = self.column, padx = 1, pady = 1)
        if self.frame != btns_frame:
            self.color("black","white")

 


expression = ""
 
input_text = StringVar()
 
# frame for the input field
input_frame = Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
input_frame.pack(side=TOP)
 
#input field inside the 'Frame'
input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=20, bg="#eee", bd=0, justify=RIGHT, fg="#000",state='readonly')
input_field.grid(row=0, column=0)

# 'Frame' for the Scientific calculator
sci_frame = Frame(win, width=312, height=1, bg="dark gray")
sci_frame.pack(anchor="se")

#'Frame' for the button 
btns_frame = Frame(win, width=312, height=272.5, bg="dark gray")
btns_frame.pack(side=RIGHT)

# making a button for backspace
back= button("⌫\t", 0, 1,input_frame,bt_back)
back.color(fg="white",bg="black")

# first row
clear = button("C", 0, 0,command= bt_clear)
clear.color(bg="green")

brac = button("(", 0, 1)
brac.color(fg="light green")
ket = button(")", 0, 2) 
ket.color(fg="light green")
divide = button("/", 0, 3,)
divide.color(fg="light green")
 
# second row
seven = button("7", 1, 0,)
eight = button("8", 1, 1)
nine = button("9", 1, 2) 
multiply = button("*", 1, 3)
multiply.color(fg="light green")

# third row
four = button("4", 2, 0)
five = button("5", 2, 1)
six = button("6", 2, 2) 
minus = button("-", 2, 3)
minus.color(fg="light green")

# fourth row
one = button("1", 3, 0)
two = button("2", 3, 1)
three = button("3", 3, 2) 
plus = button("+", 3, 3)
plus.color(fg="light green")

# fifth row
zero = button("0", 4, 0)
point = button(".", 4, 1)
equals = Button(btns_frame, text = "=", fg = "white", width = 21, height = 3, bd = 0, bg = "green", cursor = "hand2", command = lambda: bt_equal()).grid(row = 4, column = 2, padx = 1, pady = 1,columnspan=2)


#making a function to change surface to simple calculator
def simcal():
    win.geometry("312x328")
    input_frame.pack(fill=X)
    input_field.config(width=20)
    sci_frame.config(height=1,width=312)
    switch.button.destroy(),kuadrat.button.destroy(),akar.button.destroy(),pangkat.button.destroy(),one_by_x.button.destroy(),faktorial.button.destroy(),quebe.button.destroy(),sin.button.destroy(),cos.button.destroy(),tan.button.destroy()
    sci_frame2.destroy()


#making a function to change surface to Scientific calculator 
a=0
def scical(): 
    def change(): 
        return   
        global a
        if a==0:
            sin_inv = button("sin⁻¹", 1, 2,sci_frame)
            cos_inv = button("cos⁻¹", 1, 3,sci_frame)
            tan_inv = button("tan⁻¹", 1, 4,sci_frame)
            a=1
            return
        if a==1:
            sin_inv.button.destroy()
            cos_inv.button.destroy()
            tan_inv.button.destroy()
            a=0
            return
        
    win.geometry("391x437")
    input_frame.pack(fill=X)
    input_field.config(width=26)
    btns_frame.pack(anchor="sw")
    sci_frame.config(height=102,width=400)
    global sci_frame2
    sci_frame2 = Frame(win,width=100,height=272.5, bg="dark gray")
    sci_frame2.pack(anchor="nw")

    # making a button for the scientific calculator
    global switch,kuadrat,akar,pangkat,one_by_x,faktorial,quebe,sin,cos,tan
    switch = button("<=>", 0, 0,sci_frame,change)
    kuadrat = button("x²", 0, 1,sci_frame)
    akar = button("√", 0, 2,sci_frame)
    pangkat = button("^", 0, 3,sci_frame)
    one_by_x = button("1/x", 0, 4,sci_frame)

    faktorial = button("n!", 1, 0,sci_frame)
    quebe = button("x³", 1, 1,sci_frame)
    sin = button("sin", 1, 2,sci_frame)
    cos = button("cos", 1, 3,sci_frame)
    tan = button("tan", 1, 4,sci_frame)


    pi = button("π", 0, 0,sci_frame2)
    e = button("e", 1, 0,sci_frame2)
    log = button("log", 2, 0,sci_frame2)
    ln = button("ln", 3, 0,sci_frame2)
    mod = button("|x|", 4, 0,sci_frame2)
    
# creating a menu bar for further options
menu=Menu(win)
win.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="Option", menu=filemenu)
filemenu.add_command(label="Simple",command=simcal)
filemenu.add_command(label="Scientific",command=scical)

win.mainloop()
