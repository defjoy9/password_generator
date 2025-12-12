# Password Generator (PyQt5)

A small GUI tool I built with **Python** and **PyQt5** to explore desktop interface design and event-driven programming.
It generates secure passwords based on selected character sets and gives immediate feedback if no options are chosen.

This was a practical way for me to get comfortable with PyQt5 widgets, layouts, signals, and input validation.

---

# 1. What the App Does

The generator creates a **16-character password** using any combination of:

* Uppercase letters
* Lowercase letters
* Numbers
* Symbols

If the user tries to generate a password without choosing any character sets, the app displays a clear warning.

This is a simple project, but it helped me understand how to structure a GUI application and manage real-time user interactions.

---

# 2. Screenshots

<img width="506" height="534" alt="sample_password" src="https://github.com/user-attachments/assets/77ef464c-7ad7-421e-be4c-f5bc6b02c94f" />

<img width="506" height="533" alt="no_action" src="https://github.com/user-attachments/assets/34f1cdc9-2a0f-46f9-9483-b8e58776fef7" />

---

# 3. Requirements

You’ll need:

* Python **3.6+**
* PyQt5

Install dependencies:

```bash
pip install PyQt5
```

---

# 4. Running the App

```
python password_generator.py
```

A window will appear where you can:

1. Select the character sets you want
2. Click **Generate Password**
3. Copy the generated password or try again

---

# 5. How It Works (Short Explanation)

The script uses:

* PyQt5 widgets (`QCheckBox`, `QPushButton`, `QLineEdit`, `QMessageBox`)
* A signal/slot connection for handling button clicks
* Python’s `random` and `string` modules to build a character pool
* Simple validation to ensure at least one option is selected
* A clean layout structure (vertical + horizontal layout combo)

It’s intentionally minimal — I wanted to focus on UX flow and PyQt5 fundamentals without adding unnecessary complexity.

---

# 6. Possible Improvements

I may add some of the following in the future:

* Configurable password length
* Password entropy / strength meter
* “Copy to clipboard” button
* Keyboard shortcuts
* Save generated passwords to a file
* Unit tests for the generator logic
* Packaging with PyInstaller for a standalone `.exe`

---

# 7. Why I Built This

I wanted practice with:

* GUI development in Python
* Organizing event-driven code
* Designing a simple but responsive user interface
* Input handling and validation
* Releasing small tools that solve real everyday problems

It’s not a big or complex project, but it’s clean, functional, and was useful as a stepping stone toward bigger desktop and backend applications.

---

# 8. License

MIT License.
