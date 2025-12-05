import tkinter as tk

# Global variable to store the current expression
expression = ""

def btn_click(item):
    """Updates the expression string and the display field when a button is clicked."""
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def btn_clear():
    """Clears the input field and resets the expression variable."""
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    """Evaluates the final expression and displays the result."""
    global expression
    try:
        # Using eval() to safely evaluate the mathematical expression
        result = str(eval(expression))
        input_text.set(result)
        expression = result # Keep the result in the expression for further calculations
    except Exception as e:
        input_text.set("Error")
        expression = ""

# 1. Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("310x350") # Set the initial size of the window

# StringVar() is used to get and set the text in the input field
input_text = tk.StringVar()

# 2. Create the display field (Entry widget)
input_field = tk.Entry(root, textvariable=input_text, font=('arial', 18, 'bold'), 
                       bd=5, insertwidth=4, bg="powder blue", justify='right')
input_field.grid(columnspan=4, ipadx=8, ipady=15) # Span across all 4 columns

# 3. Define the buttons layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# 4. Place buttons in the grid
row_val = 1
col_val = 0

for button in buttons:
    # Use a lambda function to pass the button value to the click handler
    if button == '=':
        btn = tk.Button(root, text=button, width=10, height=3, command=btn_equal)
    elif button == 'C':
        btn = tk.Button(root, text=button, width=10, height=3, command=btn_clear)
    else:
        btn = tk.Button(root, text=button, width=10, height=3, command=lambda item=button: btn_click(item))
        
    btn.grid(row=row_val, column=col_val, padx=1, pady=1)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# 5. Run the main application loop
root.mainloop()
