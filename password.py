import tkinter as tk  # GUI library
from tkinter import messagebox  # For dialog boxes
import random  # For password generation
import string  # For character sets
from cryptography.fernet import Fernet  # For encryption
import json  # For data storage
import os  # For file operations

DATA_FILE = "passwords.json"  # Encrypted data file
KEY_FILE = "key.key"  # Encryption key file

# --- JSON functions ---
if not os.path.exists(KEY_FILE):  # Generate key if it doesn't exist
    key = Fernet.generate_key()  # Create a new key
    with open(KEY_FILE, "wb") as f:  # Save the key to a file
        f.write(key)  # Write key to file
else:  # Load existing key
    with open(KEY_FILE, "rb") as f:  # Read the key from file
        key = f.read()  # Load key

fernet = Fernet(key)  # Create Fernet object for encryption/decryption


def save_data(data):  # Save data to encrypted JSON file
    # Convert data to JSON and encode to bytes
    json_data = json.dumps(data).encode()
    encrypted = fernet.encrypt(json_data)  # Encrypt the JSON data
    with open(DATA_FILE, "wb") as f:  # Write encrypted data to file
        f.write(encrypted)  # Save encrypted data


def load_data():  # Load data from encrypted JSON file
    if not os.path.exists(DATA_FILE):  # If file doesn't exist, return empty list
        return []  # No data yet
    with open(DATA_FILE, "rb") as f:  # Read encrypted data from file
        encrypted = f.read()  # Load encrypted data
    decrypted = fernet.decrypt(encrypted)  # Decrypt the data
    return json.loads(decrypted.decode())  # Convert JSON back to Python object

# --- Password generation ---


# Generate a random password
def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase  # Start with lowercase letters
    if use_upper:  # Include uppercase letters
        chars += string.ascii_uppercase  # Add uppercase letters
    if use_digits:  # Include digits
        chars += string.digits  # Add digits
    if use_symbols:  # Include symbols
        chars += string.punctuation  # Add symbols
    # Generate password
    return ''.join(random.choice(chars) for _ in range(length))

# --- GUI Functions ---


def create_password():  # Create password and display it
    try:  # Get length from entry
        length = int(entry_length.get())  # Convert to integer
    except ValueError:  # Handle invalid input
        messagebox.showerror(  # Show error message
            "Error", "Password length must be a valid number!")
        return  # Exit function

    password = generate_password(  # Generate password
        # Get options from checkboxes
        length, var_upper.get(), var_digits.get(), var_symbols.get())
    entry_password.delete(0, tk.END)  # Clear previous password
    entry_password.insert(0, password)  # Display new password


def save_password():  # Save password to encrypted JSON file
    site = entry_site.get()  # Get site name
    username = entry_username.get()  # Get username
    password = entry_password.get()  # Get password

    if not site or not username or not password:  # Check for empty fields
        # Show error message
        messagebox.showerror("Error", "Please fill in all fields!")
        return  # Exit function

    data = load_data()  # Load existing data
    data.append({"site": site, "username": username,
                "password": password})  # Add new entry
    save_data(data)  # Save updated data
    # Show success message
    messagebox.showinfo("Success", "Password saved successfully!")
    update_password_list()  # Update listbox


def delete_password():  # Delete selected password from encrypted JSON file
    selected = listbox_passwords.curselection()  # Get selected item
    if not selected:  # Check if nothing is selected
        # Show error message
        messagebox.showerror("Error", "No password selected!")
        return  # Exit function

    index = selected[0]  # Get index of selected item
    data = load_data()  # Load existing data
    deleted_entry = data.pop(index)  # Remove selected entry
    save_data(data)  # Save updated data
    messagebox.showinfo(  # Show success message
        # Message
        "Success", f"Password for {deleted_entry['site']} deleted successfully!")
    update_password_list()  # Update listbox


def update_password_list():  # Update the listbox with saved passwords
    listbox_passwords.delete(0, tk.END)  # Clear existing entries
    for entry in load_data():  # Load data and iterate
        listbox_passwords.insert(  # Insert each entry into listbox
            # Format entry
            tk.END, f"{entry['site']} | {entry['username']} | {entry['password']}")


# --- GUI Design ---
root = tk.Tk()  # Create main window
root.title("Password Generator & Manager")  # Set window title
root.geometry("500x500")  # Set window size

# Password Generation Section
tk.Label(root, text="Password Length:").pack()  # Label for length
entry_length = tk.Entry(root)  # Entry for length
entry_length.pack()  # Pack entry
entry_length.insert(0, "12")  # Default length

var_upper = tk.BooleanVar(value=True)  # Variable for uppercase option
tk.Checkbutton(root, text="Include Uppercase Letters",  # Checkbox for uppercase
               variable=var_upper).pack()  # Pack checkbox

var_digits = tk.BooleanVar(value=True)  # Variable for digits option
tk.Checkbutton(root, text="Include Digits",
               variable=var_digits).pack()  # Pack checkbox

var_symbols = tk.BooleanVar(value=True)  # Variable for symbols option
tk.Checkbutton(root, text="Include Symbols",
               variable=var_symbols).pack()  # Pack checkbox

tk.Button(root, text="Generate Password",
          command=create_password).pack()  # Generate button

entry_password = tk.Entry(root, width=40)  # Entry for displaying password
entry_password.pack(pady=5)  # Pack entry

# Save Password Section
tk.Label(root, text="Site Name:").pack()  # Label for site name
entry_site = tk.Entry(root)  # Entry for site name
entry_site.pack()  # Pack entry

tk.Label(root, text="Username:").pack()  # Label for username
entry_username = tk.Entry(root)  # Entry for username
entry_username.pack()  # Pack entry

tk.Button(root, text="Save Password", command=save_password).pack(
    pady=5)  # Save button
tk.Button(root, text="Delete Selected Password",  # Delete button
          command=delete_password).pack(pady=5)  # Pack button

# Saved Passwords Section
tk.Label(root, text="Saved Passwords:").pack()  # Label for saved passwords
# Listbox for displaying passwords
listbox_passwords = tk.Listbox(root, width=60)
listbox_passwords.pack(pady=5)  # Pack listbox
update_password_list()  # Initial population of listbox

root.mainloop()  # Start the GUI event loop
