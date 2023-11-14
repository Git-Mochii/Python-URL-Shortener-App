
# URL Shortener Application #

import tkinter as tk 
from tkinter import messagebox
from urllib.parse import urlparse # Key module
import pyshorteners # Key module

# Window Settings #

window = tk.Tk()
window.title("Link Shortener Application")
window.geometry("500x500")
window.resizable(False, False)

# Shorten Link Function

def shorten():
    url = alpha_url.get() # Get the URL from the alpha_url entry (Non-Shortened Link Entry)
    if not url:
        messagebox.showerror("Error", "Please enter a URL") # If the URL is empty, show an error message
        return

    parsed_url = urlparse(url)
    if not all([parsed_url.scheme, parsed_url.netloc]): # Check if the URL is valid by ensuring it has both a scheme and a netloc (domain)
        messagebox.showerror("Error", "Please enter a valid URL") # If the URL is invalid, show an error message
        return

    short_url = pyshorteners.Shortener().tinyurl.short(url) # Get the shortened URL from the tinyurl module
    beta_url.delete(0, tk.END)  # Clear the beta_url entry before inserting the new URL
    beta_url.insert(0, short_url)  # Insert the shortened URL into beta_url (Shortened Link Entry)
    messagebox.showinfo("Success", "URL Shortened")

# Label Text (Tell users what to do)

label = tk.Label(window, text="Enter the URL below to shorten:", font=("Arial", 20))
label.pack(padx=20, pady=20)

# Alpha URL Entry (Non-Shortened Link Entry)

alpha_url = tk.Entry(window, font=("Arial", 20), width= 40)
alpha_url.pack(padx=20, pady=20)

# Beta URL Entry (Shortened Link Entry)

beta_url = tk.Entry(window, font=("Arial", 15), justify=tk.CENTER, width= 30)
beta_url.pack(padx=20, pady=20)

# Button to Shorten URL

shortener_button = tk.Button(window, text="Shorten URL", command=shorten, font=("Arial", 15))
shortener_button.pack(padx=20, pady=20)

# Main Application Loop

window.mainloop()

