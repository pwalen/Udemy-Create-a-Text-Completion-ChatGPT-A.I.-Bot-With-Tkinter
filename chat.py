from tkinter import *
import customtkinter
import openai
import os
import pickle


# Initiate App
root = customtkinter.CTk()
root.title("ChatGPT Bot")
root.geometry("600x600")
root.iconbitmap("ai_lt.ico") # https://tkinter.com/images/ai_lt.ico

# Set Color Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
