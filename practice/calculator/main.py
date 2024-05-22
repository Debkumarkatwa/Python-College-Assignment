import tkinter as tk

window=tk.Tk()
window.title("Simple Calculator")
window.iconbitmap('cal logo.ico')
window.minsize(300, 400)

class buttons:
    
    def __init__(self, text, row, column):
        self.text = text
        self.row = row
        self.column = column
        self.button = tk.Button(window, text=self.text, font=("Arial", 20), fg="white", bg="black",width=2, height=1)
        self.button.grid(row=self.row, column=self.column)
        #self.button.bind("<Button-1>", self.click)

    def color(self,color):
        self.button.config(bg=color)

    # def click(self, event):
    #     if self.text=="C":
    #         screen.delete(0, tk.END)
    #     elif self.text=="<--":
    #         screen.delete(len(screen.get())-1, tk.END)
    #     elif self.text=="=":
    #         try:
    #             screen.delete(0, tk.END)
    #             screen.insert(tk.END, str(eval(screen.get())))
    #         except:
    #             screen.delete(0, tk.END)
    #             screen.insert(tk.END, "Error")
    #     elif self.text=="x^2":
    #         screen.insert(tk.END, "**2")
    #     elif self.text=="1/x":
    #         screen.insert(tk.END, "**-1")
    #     elif self.text=="√":
    #         screen.insert(tk.END, "**0.5")
    #     else:
    #         screen.insert(tk.END, self.text)


screen=tk.Entry(window, font=("Arial", 20), fg="black", bg="light gray", width=10, borderwidth=5, justify="right")
screen.grid(row=0, column=0, columnspan=4)

point=buttons(".", 8, 0)

num0=buttons("0", 8, 1)

percent=buttons("%", 8, 2)

equal=buttons("=", 8, 3)
equal.color("blue")

num1=buttons("1", 7, 0)

num2=buttons("2", 7, 1)

num3=buttons("3", 7, 2)

plus=buttons("+", 7, 3)

num4=buttons("4", 6, 0)

num5=buttons("5", 6, 1)

num6=buttons("6", 6, 2)

minus=buttons("-", 6, 3)

num7=buttons("7", 5, 0)

num8=buttons("8", 5, 1)

num9=buttons("9", 5, 2)

multiply=buttons("*", 5, 3)

zz=buttons("1/x", 4, 0)

square=buttons("x^2", 4, 1)

root=buttons("√", 4, 2)

divide=buttons("/", 4, 3)

bra=buttons("(", 3, 0)

ket=buttons(")", 3, 1)

clear=buttons("C", 3, 2)

delete=buttons("<--", 3, 3)

window.mainloop()

