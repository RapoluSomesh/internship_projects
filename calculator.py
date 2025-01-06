import tkinter as tk
from math import sqrt, factorial


def button_click(event):
    button = event.widget
    text = button['text']

    if text == '=':
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == 'C':
        entry.delete(0, tk.END)
    elif text == '√':
        try:
            result = sqrt(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == '<-':
        entry.delete(len(entry.get()) - 1)
    elif text == '!':
        try:
            result = factorial(int(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)


# Create main window
window = tk.Tk()
window.title("Calculator")
window.resizable(0, 0)

# Create entry widget
entry = tk.Entry(window, width=30, font=('Arial', 14), bd=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('C', 1, 0), ('√', 1, 1), ('/', 1, 2), ('<-', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('!', 5, 0), ('0', 5, 1), ('.', 5, 2), ('=', 5, 3)
]

# Create and place buttons
for (text, row, column) in buttons:
    button = tk.Button(window, text=text, width=3, height=2, font=('Arial', 14))
    button.grid(row=row, column=column, padx=5, pady=5)
    button.bind('<Button-1>', button_click)

# Run the application
window.mainloop()
