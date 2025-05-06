import tkinter as tk
from tkinter import messagebox
import json
import os

# File untuk menyimpan user
USER_FILE = "users.json"

# Membaca data user
def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        return json.load(f)

# Menyimpan data user
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

# Halaman utama setelah login
def main_app():
    app = tk.Tk()
    app.title("Main App - GUI Menarik")
    app.geometry("400x300")
    app.configure(bg="#e0f7fa")

    # Label warna biru
    label = tk.Label(app, text="Selamat Datang di Aplikasi!", bg="#2196f3", fg="white", font=("Arial", 14), pady=10)
    label.pack(pady=10)

    # Frame oranye
    frame = tk.Frame(app, bg="#ff9800", width=300, height=100)
    frame.pack(pady=20)
    tk.Label(frame, text="Ini adalah Frame berwarna", bg="#ff9800", fg="white", font=("Arial", 12)).pack(pady=10)

    # Button hijau
    def on_hover(e): button.config(bg="#43a047")
    def off_hover(e): button.config(bg="#4caf50")

    button = tk.Button(app, text="Keluar", bg="#4caf50", fg="white", font=("Arial", 12), command=app.destroy)
    button.pack(pady=10)
    button.bind("<Enter>", on_hover)
    button.bind("<Leave>", off_hover)

    app.mainloop()

# Halaman Login/Register
class AuthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login & Register")
        self.root.geometry("400x300")
        self.root.configure(bg="#f1f8e9")

        self.users = load_users()

        self.is_registering = False
        self.setup_widgets()

    def setup_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        title = "Register" if self.is_registering else "Login"
        tk.Label(self.root, text=title, font=("Arial", 16), bg="#f1f8e9").pack(pady=10)

        self.username_entry = self.create_entry("Username")
        self.password_entry = self.create_entry("Password", show="*")

        if self.is_registering:
            self.confirm_entry = self.create_entry("Confirm Password", show="*")

        action_btn = tk.Button(self.root, text=title, command=self.register if self.is_registering else self.login, bg="#8bc34a", fg="white", width=15)
        action_btn.pack(pady=10)

        switch_text = "Sudah punya akun? Login" if self.is_registering else "Belum punya akun? Register"
        switch_btn = tk.Button(self.root, text=switch_text, command=self.toggle_mode, bg="#cfd8dc")
        switch_btn.pack(pady=5)

    def create_entry(self, label_text, show=None):
        tk.Label(self.root, text=label_text, bg="#f1f8e9").pack()
        entry = tk.Entry(self.root, show=show)
        entry.pack(pady=2)
        return entry

    def toggle_mode(self):
        self.is_registering = not self.is_registering
        self.setup_widgets()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "Semua field harus diisi!")
            return
        if password != confirm:
            messagebox.showerror("Password Error", "Password tidak cocok!")
            return
        if username in self.users:
            messagebox.showerror("Register Error", "Username sudah ada!")
            return

        self.users[username] = password
        save_users(self.users)
        messagebox.showinfo("Sukses", "Registrasi berhasil!")
        self.toggle_mode()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.users.get(username) == password:
            messagebox.showinfo("Login Berhasil", f"Selamat datang, {username}!")
            self.root.destroy()
            main_app()
        else:
            messagebox.showerror("Login Gagal", "Username atau password salah.")

# Menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = AuthApp(root)
    root.mainloop()
