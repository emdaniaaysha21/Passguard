# 🔐 PassGuard

A command-line Password Strength Analyzer and Generator built using Python.

PassGuard helps users understand password strength, identify weaknesses and generate strong passwords.

## 🚀 Features

- Analyzes password length.
- Counts uppercase, lowercase, digits and special characters.
- Checks passwords against a list of common passwords.
- Calculates password strength score out of 100.
- Classifies passwords as Weak, Medium, Strong or Very Strong.
- Calculates password entropy in bits.
- Estimates password cracking time.
- Provides suggestions to improve password strength.
- Generates strong random passwords.

## 📌 Version 5 – Entropy and Suggestions

- Calculates password entropy using the `math` module.
- Estimates password cracking time.
- Provides suggestions such as adding uppercase letters, digits and special characters.

## 📌 Version 6 – Menu and Password Generator

- Added a menu using a `while` loop.
- Option 1: Analyze a password.
- Option 2: Generate a strong password.
- Option 3: Exit the program.
- Uses Python's `secrets` module for secure password generation.

**Why secrets instead of random?**

The `secrets` module is designed for generating passwords and other security-sensitive values. The `random` module is not suitable for security purposes.

## 🛠️ How to Run

1. Install Python 3.
2. Download `passguard.py`.
3. Open the terminal in the project folder.
4. Run:

```bash
python passguard.py
```

## 📸 Screenshots

### Main Menu
![PassGuard Menu](Passguard%20Menu.png)

### Weak Password Analysis
![Weak Password](Passguard%20Weak%20Password.png)

### Strong Password Analysis
![Strong Password](Passguard%20Strong%20Password.png)

### Very Strong Password Analysis
![Very Strong Password](Passguard%20Very%20Strong%20Password.png)

## 📚 Concepts Used

- Variables and data types
- Strings and string methods
- If, elif and else conditions
- For and while loops
- Lists and sets
- Importing Python modules
- Mathematical calculations
- Password generation

## ⚠️ Limitations

- Crack time is an approximate estimate based on an assumed speed of 10 billion guesses per second.
- The common-password list contains a limited number of passwords.
- Entropy and crack-time estimates do not guarantee actual password security.

## 🔮 Future Improvements

- Check passwords against a larger breached-password database.
- Save password analysis reports to a file.
- Build a simple web interface.

## 👩‍💻 Author

Aaysha Emdani 

Information communication Technology  
GEC Bhavnagar
