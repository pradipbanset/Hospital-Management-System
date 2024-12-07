from tkinter import *
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == 'admin' and password == '123':
        login_window.destroy()
        main_window()
    else:
        messagebox.showerror('Error', 'Incorrect username or password.')

def main_window():
    # Create the main window
    window = Tk()
    window.title('Hospital Management System')

    # Add your GUI elements and functionality here

    window.mainloop()

# Create the login window
login_window = Tk()
login_window.title('Login')

# Configure the login window
login_window.configure(bg='#F2F2F2')

# Create username label and entry
username_label = Label(login_window, text='Username:', font=('Arial', 16), bg='#F2F2F2')
username_label.pack()
username_entry = Entry(login_window, font=('Arial', 14))
username_entry.pack()

# Create password label and entry
password_label = Label(login_window, text='Password:', font=('Arial', 16), bg='#F2F2F2')
password_label.pack()
password_entry = Entry(login_window, show='*', font=('Arial', 14))
password_entry.pack()

# Create login button
login_button = Button(login_window, text='Login', command=login, bg='#4CAF50', fg='white', font=('Arial', 16, 'bold'))
login_button.pack()

# Run the login window
login_window.mainloop()