import tkinter as tk

root = tk.Tk()
root.title("Advanced Calculator")

# Display
entry = tk.Entry(root, width=25, font=("Arial", 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# History
history = []

# Click function
def click(value):
    entry.insert(tk.END, value)

# Clear screen
def clear():
    entry.delete(0, tk.END)

# Calculate without eval
def calculate():
    try:
        expression = entry.get()

        if '+' in expression:
            a, b = expression.split('+')
            result = float(a) + float(b)

        elif '-' in expression:
            a, b = expression.split('-')
            result = float(a) - float(b)

        elif '*' in expression:
            a, b = expression.split('*')
            result = float(a) * float(b)

        elif '/' in expression:
            a, b = expression.split('/')
            if float(b) != 0:
                result = float(a) / float(b)
            else:
                result = "Error"

        else:
            result = "Invalid"

        history.append(f"{expression} = {result}")

        entry.delete(0, tk.END)
        entry.insert(0, result)

    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Show history
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("History")

    for i, item in enumerate(history):
        tk.Label(history_window, text=item).pack()

# Buttons
buttons = [
    ('1',1,0), ('2',1,1), ('3',1,2), ('+',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
    ('7',3,0), ('8',3,1), ('9',3,2), ('*',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('/',4,3),
    ('H',5,0)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "C":
        action = clear
    elif text == "=":
        action = calculate
    elif text == "H":
        action = show_history
    else:
        action = lambda x=text: click(x)

    tk.Button(root, text=text, width=5, height=2, command=action)\
        .grid(row=row, column=col)

root.mainloop()