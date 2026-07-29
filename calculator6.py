import tkinter as tk

# Create window
root = tk.Tk()
root.title("Calculator")

# Entry box (display)
entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Function to click buttons
def click(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

# Clear function
def clear():
    entry.delete(0, tk.END)

# Calculate result
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons
buttons = [
    ('1',1,0), ('2',1,1), ('3',1,2), ('+',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
    ('7',3,0), ('8',3,1), ('9',3,2), ('*',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('/',4,3)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "C":
        action = clear
    elif text == "=":
        action = equal
    else:
        action = lambda x=text: click(x)

    tk.Button(root, text=text, width=5, height=2, command=action)\
        .grid(row=row, column=col)

# Run app
root.mainloop()