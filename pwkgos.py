import tkinter as tk
import random
import string
import pyperclip

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create a function to generate the password
def generate_password():
  # Set the length of the password
  password_length = int(password_entry.get())

  # Create an empty list to store the characters of the password
  password_chars = []

  # Generate the password by adding random characters to the list
  for i in range(password_length):
    # Choose a random character type (lowercase, uppercase, or digits)
    char_type = random.choice(['lower', 'upper', 'digits'])

    # Add a random character of the chosen type to the list
    if char_type == 'lower':
      password_chars.append(random.choice(string.ascii_lowercase))
    elif char_type == 'upper':
      password_chars.append(random.choice(string.ascii_uppercase))
    elif char_type == 'digits':
      password_chars.append(random.choice(string.digits))

  # Convert the list of characters to a string and return it
  return ''.join(password_chars)

# Create a function to copy the password to the clipboard
def copy_password():
  # Copy the password to the clipboard
  pyperclip.copy(password_label['text'])

# Create a label to display the password
password_label = tk.Label(window, text="")
password_label.pack()

# Create a entry for password length
password_entry = tk.Entry(window)
password_entry.insert([0],'8')
password_entry.pack()

# Create a button to generate a new password
generate_button = tk.Button(window, text="Generate Password", command=lambda: password_label.config(text=generate_password()))
generate_button.pack()

# Create a button to copy the password to the clipboard
copy_button = tk.Button(window, text="Copy Password", command=copy_password)
copy_button.pack()

# Run the Tkinter event loop
window.mainloop()
