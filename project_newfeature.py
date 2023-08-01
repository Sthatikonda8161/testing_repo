# login_page.py
import tkinter as tk
from tkinter import messagebox

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry("300x150")

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Replace with your actual authentication logic here
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, {}!".format(username))
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
    

if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
