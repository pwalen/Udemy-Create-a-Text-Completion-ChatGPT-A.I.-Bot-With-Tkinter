from tkinter import *
import customtkinter
import openai
import os
import pickle


# Initiate App
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry("600x600")
root.iconbitmap("ai_lt.ico")  # https://tkinter.com/images/ai_lt.ico

# Set Color Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Create Text Frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)

# Add Text Wiget To Get ChatGPT Responses
my_text = Text(
    text_frame,
    bg="#343638",
    width=65,
    bd=1,
    fg="#d6d6d6",
    relief=FLAT,
    wrap=WORD,
    selectbackground="#1f538d",
)
my_text.grid(row=0, column=0)

# Create Scrollbar for text widget
text_scroll = customtkinter.CTkScrollbar(text_frame, command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")

# Add the scrollbar to the textbox
my_text.configure(yscrollcommand=text_scroll.set)

# Entry widget to type stuff to ChatGPT
chat_entry = customtkinter.CTkEntry(
    root,
    placeholder_text="Type Something to ChatGPT ...",
    width=535,
    height=50,
    border_width=2,
)
chat_entry.pack(pady=10)


root.mainloop()
