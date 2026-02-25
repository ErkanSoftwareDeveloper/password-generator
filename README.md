#  Password Generator & Manager

A simple and secure **password generator and manager desktop application** built with **Python** and **Tkinter**.
This project focuses on generating strong passwords, storing them securely with encryption, and managing them easily.

---

##  Features

* Generate strong passwords with:

  * Uppercase letters
  * Digits
  * Symbols
* Customizable password length
* Save passwords with site name and username
* Delete saved passwords
* Encrypted storage for security
* Simple and clean UI

---

##  Technologies Used

* **Python 3**
* **Tkinter** – standard Python GUI library
* **cryptography** – for encrypting stored passwords
* **JSON** – for structured data storage

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/ErkanSoftwareDeveloper/password-generator.git
cd password-generator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the application:

```bash
python password.py
```

1. Set password length and options (uppercase, digits, symbols)
2. Click **Generate Password** to create a password
3. Enter site and username, then click **Save Password**
4. Select a saved password to **delete** it if needed

---

##  Project Structure

```text
password-manager/
├─ password.py   # Main application file
├─ .gitignore            # Git ignored files
├─ README.md             # Project documentation
├─ requirements.txt      # Project dependencies
├─ key.key               # Encryption key file (auto-generated)
└─ passwords.json        # Encrypted saved passwords
```

---

##  Video

![2026-01-1111-12-01-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/6e849fce-d321-4548-8e50-47dba7e7b3a2)


---

##  Possible Improvements

* Master password protection
* Search/filter saved passwords
* Export/import encrypted password backup
* Password strength meter
* Dark / light theme options
* Packaging as executable (.exe)

---

##  License

This project is intended for **educational and personal use**.
