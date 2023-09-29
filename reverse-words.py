import tkinter as tk
from tkinter import Entry, Label, Button


"""Given a string s containing words separated by spaces, return a new string with each word reversed but the order of the words should remain the same."""

def reverse_words(s:str) -> str:
  words = s.split()
  reverse_words = [word[::-1] for word in words]
  return ' '.join(reverse_words)

def on_reverse_click():
  input_text = input_entry.get()
  reversed_text = reverse_words(input_text)
  output_label.config(text=reversed_text)

# Create the main window
root = tk.Tk()
root.title("Reverse Words")

# Create and place the widgets
input_label = Label(root, text="Enter text:")
input_label.pack(pady=10)

input_entry = Entry(root, width=50)
input_entry.pack(pady=10)

reverse_button = Button(root, text="Reverse Words", command=on_reverse_click)
reverse_button.pack(pady=10)

output_label = Label(root, text="")
output_label.pack(pady=10)

# Start the application
root.mainloop()
