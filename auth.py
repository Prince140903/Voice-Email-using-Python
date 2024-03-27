from main import main
import sqlite3
from flask import render_template



# conn = sqlite3.connect('login_credentials.db')
# cursor = conn.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY,
#                     email TEXT UNIQUE NOT NULL,
#                     password TEXT NOT NULL
#                 )''')

# def save_login_credentials(sender_email, sender_password):
#     try:
#         cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (sender_email, sender_password))
#         conn.commit()
#         print("Login credentials saved successfully.")
#     except sqlite3.IntegrityError:
#         print("Email address already exists.")
#     except Exception as e:
#         print("Error:", e)


# def login(sender_email, sender_password):
#     try:
#         # cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (sender_email, sender_password))
#         # user = cursor.fetchone()
#         if user:
#             print("Login successful!")
#             return render_template("index.html")
#         else:
#             print("Invalid email or password.")
#             return False
#     except Exception as e:
#         print("Error:", e)
#         return False

# conn.close()
