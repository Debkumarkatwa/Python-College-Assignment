import tkinter as tk
# Function to evaluate the expression
def evaluate_expression():
 try:
 result.set(eval(expression.get()))
 except:
 result.set("Error")
# Function to append clicked buttons to the expression
def append_to_expression(value):
 expression.set(expression.get() + value)
# Function to clear the expression
def clear_expression():
 expression.set("")
 result.set("")
# Create the main window
root = tk.Tk()
root.title("Calculator")
# StringVar to store the expression and result
expression = tk.StringVar()
result = tk.StringVar()
# Entry widget to display the expression
entry = tk.Entry(root, textvariable=expression, bd=5, font=('Arial', 14), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
# Entry widget to display the result
result_label = tk.Label(root, textvariable=result, bd=5, font=('Arial', 14), justify="right")
result_label.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="ew")
# Buttons for numbers and operators
buttons = [
 ('7', '8', '9', '/'),
 ('4', '5', '6', '*'),
 ('1', '2', '3', '-'),
 ('0', '.', '=', '+')
]
# Create and place buttons in the grid
for i in range(len(buttons)):
 for j in range(len(buttons[i])):
 if buttons[i][j] == '=':
 btn = tk.Button(root, text=buttons[i][j], bd=5, font=('Arial', 14), 
command=evaluate_expression)
 elif buttons[i][j] == '0':
 btn = tk.Button(root, text=buttons[i][j], bd=5, font=('Arial', 14), command=lambda x='0': 
append_to_expression(x))
 else:
 btn = tk.Button(root, text=buttons[i][j], bd=5, font=('Arial', 14), command=lambda 
x=buttons[i][j]: append_to_expression(x))
 btn.grid(row=i+2, column=j, padx=5, pady=5, sticky="ew")
# Clear button
clear_btn = tk.Button(root, text="Clear", bd=5, font=('Arial', 14), command=clear_expression)
clear_btn.grid(row=len(buttons)+2, column=0, columnspan=4, padx=5, pady=5, sticky="ew")
# Run the main loop
root.mainloop()