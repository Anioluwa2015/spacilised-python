import tkinter as tk
from tkinter import messagebox
import re

def check_password_strength():
    """Evaluates the password and displays the strength."""
    password = password_entry.get()
    score = 0
    feedback = []

    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    if re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("Password must contain at least one lowercase letter.")
        
    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("Password must contain at least one uppercase letter.")

    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("Password must contain at least one digit.")

    if re.search("[!@#$%^&*()_+={}\[\]:;\"'|<,>.?/]", password):
        score += 1
    else:
        feedback.append("Password must contain at least one special character.")

    # Display result
    if score == 5:
        messagebox.showinfo("Password Strength", "Very Strong Password!")
    elif score >= 3:
        messagebox.showinfo("Password Strength", f"Medium Strength. Tips: {' '.join(feedback)}")
    else:
        messagebox.showwarning("Password Strength", f"Weak Password. Tips: {' '.join(feedback)}")

# --- Tkinter GUI Setup ---

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x150")

# Label
password_label = tk.Label(root, text="Enter Password:")
password_label.pack(pady=10)

# Entry widget for password input (hides characters with '*')
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

# Button to trigger the check
check_button = tk.Button(root, text="Check Strength", command=check_password_strength)
check_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
