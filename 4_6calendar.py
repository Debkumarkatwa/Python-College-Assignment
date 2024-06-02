from calendar import *
from tkinter import *

win = Tk()
win.title("Calendar")
win.geometry("200x300")
win.resizable(0, 0)

def show():
    m = int(month_n.get())
    y = int(year.get())
    output.delete(0.0, END)
    output.insert(INSERT,month(y, m))

Label(win, text="Month:").pack()
month_n = Spinbox(win, from_=1, to=12)
month_n.pack()

Label(win, text="Year:").pack()
year = Spinbox(win, from_=1900, to=2100)
year.pack()

Button(win, text="Show", command=show).pack()

output = Text(win, width=20, height=10, wrap=WORD)
output.pack()

win.mainloop()
