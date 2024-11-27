import tkinter as tk
from tkinter import messagebox

# Dracula theme colors
BG_COLOR = "#282a36"
FG_COLOR = "#f8f8f2"
BUTTON_COLOR = "#44475a"
BORDER_COLOR = "#50fa7b"  # Softer neon green
OPERATOR_COLOR = "#bd93f9"
EQUALS_COLOR = "#6272a4"
CLEAR_COLOR = "#ff5555"

# Fighting popup colors (neutral style)
FIGHTING_BG_COLOR = "#f0f0f0"  # Light grey background
FIGHTING_TEXT_COLOR = "#333333"  # Darker text color

def click_button(value):
    """Update entry field with button press."""
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(value))

def clear_entry():
    """Clear the entry field."""
    entry.delete(0, tk.END)

def delete_last():
    """Delete last character in the entry field."""
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text[:-1])

def calculate_result():
    """Evaluate the expression in the entry field."""
    try:
        # Special case for 9 + 10 = 21
        if entry.get() == "9+10":
            entry.delete(0, tk.END)
            entry.insert(0, "21")
        else:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed.")
    except Exception:
        messagebox.showerror("Error", "Invalid input.")

def challenge():
    """Handle challenge popup."""
    response = messagebox.askquestion("Challenge", "Oh, so you're up for a challenge? Are you sure?")
    if response == 'yes':
        show_fighting_popup()

def show_fighting_popup():
    """Show 'Fighting...' popup for 3 seconds."""
    fighting_popup = tk.Toplevel(root)
    fighting_popup.title("Fighting...")
    fighting_popup.configure(bg=FIGHTING_BG_COLOR)
    fighting_popup.geometry("200x100")
    
    fighting_label = tk.Label(fighting_popup, text="Fighting...", font=("Arial", 20), bg=FIGHTING_BG_COLOR, fg=FIGHTING_TEXT_COLOR)
    fighting_label.pack(expand=True)

    fighting_popup.grab_set()
    root.after(3000, lambda: close_fighting_popup(fighting_popup))

def close_fighting_popup(popup):
    """Close the fighting popup and show the lost popup."""
    popup.destroy()
    lost_popup()

def lost_popup():
    """Show 'You lost' popup and handle user response."""
    response = messagebox.askquestion("You lost", "You lost. Return to calculator?")
    if response == 'yes':
        clear_entry()
    else:
        root.quit()

# Main window setup
root = tk.Tk()
root.title("Dracula calculator")
root.configure(bg=BG_COLOR)

# Entry field setup
entry = tk.Entry(root, width=25, font=("Arial", 20), borderwidth=2, justify="right", bg=BUTTON_COLOR, fg=FG_COLOR)
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipady=10)

# Button definitions
buttons = [
    ("AC", 1, 0, CLEAR_COLOR, clear_entry), ("DE", 1, 1, CLEAR_COLOR, delete_last),
    (".", 1, 2, BUTTON_COLOR, lambda: click_button(".")), ("/", 1, 3, OPERATOR_COLOR, lambda: click_button("/")),

    ("7", 2, 0, BUTTON_COLOR, lambda: click_button("7")), ("8", 2, 1, BUTTON_COLOR, lambda: click_button("8")),
    ("9", 2, 2, BUTTON_COLOR, lambda: click_button("9")), ("*", 2, 3, OPERATOR_COLOR, lambda: click_button("*")),

    ("4", 3, 0, BUTTON_COLOR, lambda: click_button("4")), ("5", 3, 1, BUTTON_COLOR, lambda: click_button("5")),
    ("6", 3, 2, BUTTON_COLOR, lambda: click_button("6")), ("-", 3, 3, OPERATOR_COLOR, lambda: click_button("-")),

    ("1", 4, 0, BUTTON_COLOR, lambda: click_button("1")), ("2", 4, 1, BUTTON_COLOR, lambda: click_button("2")),
    ("3", 4, 2, BUTTON_COLOR, lambda: click_button("3")), ("+", 4, 3, OPERATOR_COLOR, lambda: click_button("+")),

    ("Hmm?", 5, 0, BUTTON_COLOR, challenge), ("0", 5, 1, BUTTON_COLOR, lambda: click_button("0")), 
    ("=", 5, 2, EQUALS_COLOR, calculate_result)  # "=" spans across 2 tiles
]

# Add buttons with layout
for (text, row, col, color, command) in buttons:
    button = tk.Button(
        root, text=text, width=5, height=2, font=("Arial", 18), command=command,
        bg=color, fg=FG_COLOR, activebackground=color, activeforeground=BG_COLOR,
        relief="solid", bd=2, highlightbackground=BORDER_COLOR
    )
    if text == "=":
        button.grid(row=row, column=col, columnspan=2, padx=5, pady=5, sticky="nsew")
    else:
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Make the grid resize responsively
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the application
root.mainloop()
