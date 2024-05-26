from tkinter import *
import math as m

win = Tk() 
win.geometry("312x348")  
win.resizable(0, 0)  
win.title("Calculator")
win.iconbitmap('cal logo.ico')
win.configure(background="white")

def btn_click(item,text=None):
    global expression , out_expression
    if text is not None:
        out_expression = out_expression + str(text)
    else:
        out_expression = out_expression + str(item)
    expression = expression + str(item)
    print(expression)
    input_text.set(out_expression)

# function for clear the input field
def bt_clear(): 
    global expression , out_expression
    expression = "" 
    out_expression = ""
    input_text.set("")

def bt_back():
    global expression,out_expression
    if expression.endswith("**0.5"):
        expression = expression[:-5]
        out_expression = out_expression[:-1]
    if expression.endswith("**2") or expression.endswith("**3"):
        expression = expression[:-2]
        out_expression = out_expression[:-3]
    if expression.endswith("**"):
        expression = expression[:-1]
    expression = expression[:-1]
    out_expression = out_expression[:-1]
    print(expression)
    input_text.set(out_expression)

 # to calculate the expression 
def bt_equal():
    global expression,out_expression
    result = str(eval(expression))
    input_text.set(result)
    expression = result
    out_expression = result


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
out_expression = ""
 
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
    kuadrat.button.destroy(),pangkat.button.destroy(),one_by_x.button.destroy(),quebe.button.destroy(),sin.button.destroy(),cos.button.destroy(),tan.button.destroy()#,akar.button.destroy(),switch.button.destroy(),faktorial.button.destroy()
    sci_frame2.destroy()


#making a function to change surface to Scientific calculator 
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
    # switch = button("<=>", 0, 0,sci_frame,change)
    kuadrat = button("x²", 0, 1,sci_frame,command=lambda: btn_click("**2","^(2)"))
    # akar = button("√", 0, 2,sci_frame,command=lambda: btn_click("**0.5","√")) # problem when i give value > 9
    pangkat = button("^", 0, 3,sci_frame,command=lambda: btn_click("**(","^("))
    one_by_x = button("1/x", 0, 4,sci_frame,command=lambda: btn_click("1/","1/"))

    #faktorial = button("n!", 1, 0,sci_frame,command=lambda: btn_click("m.factorial(","!"))
    quebe = button("x³", 1, 1,sci_frame,command=lambda: btn_click("**3","^(3)"))
    sin = button("sin", 1, 2,sci_frame,command=lambda: btn_click("m.sin((m.pi / 180)*","sin("))
    cos = button("cos", 1, 3,sci_frame,command=lambda: btn_click("m.cos((m.pi / 180)*","cos("))
    tan = button("tan", 1, 4,sci_frame,command=lambda: btn_click("m.tan((m.pi / 180)*","tan("))


    pi = button("π", 0, 0,sci_frame2,command=lambda: btn_click("m.pi","π"))
    e = button("e", 1, 0,sci_frame2,command=lambda: btn_click("m.e","e"))
    log = button("log", 2, 0,sci_frame2,command=lambda: btn_click("m.log10(","log("))
    ln = button("ln", 3, 0,sci_frame2,command=lambda: btn_click("m.log(","ln("))
    mod = button("|x|", 4, 0,sci_frame2,command=lambda: btn_click("m.fabs(","("))
    
# creating a menu bar for further options
def c():
    global option
    if option=="Scientific":
        option="Simple"
        filemenu.entryconfig(1,label="Simple")
        scical()
    elif option=="Simple":
        option="Scientific"
        filemenu.entryconfig(1,label="Scientific")
        simcal()
menu=Menu(win)
win.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label="Switch Mode", menu=filemenu)
option="Scientific"
filemenu.add_command(label=option,command=c)

win.mainloop()
