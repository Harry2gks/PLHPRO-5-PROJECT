import tkinter as tk 
from tkinter import*
from PIL import ImageTk, Image # type: ignore # ---> αν υπογραμμίζει την γραμμη αυτη, θελει επανεγκατασταση η Python, αλλά το πρόγραμμα τρέχει <-----------
import customtkinter

from MeetMePack.client_window import *
from MeetMePack.appoinment_window import *

import webbrowser

root = tk.Tk()
root.title("Meet Me")
root.iconbitmap("MeetMe_icon.ico")
root.geometry("1200x700")  # Set width and height
#root.configure(background='#212029') 
root.configure(background='#282c34')
root.minsize(width=1200, height=700)


# Connect with database
conn = run()

# Buttons
button1 = customtkinter.CTkButton(root, 
                                  text="Πελατολόγιο",
                                  text_color = "#f1fff2",
                                  font = ("Helvetica", 24),  
                                  width = 300, 
                                  height = 60, 
                                  corner_radius = 20,
                                  #fg_color="#327fe3",
                                  fg_color="#2fa572",
                                  command=lambda: client_list(conn, root))
button1.place(relx=0.5, rely=0.25, anchor="center")
# New window #client_window

button2 = customtkinter.CTkButton(root, 
                                  text="Ραντεβού",
                                  text_color = "#f1fff2",
                                  font = ("Helvetica", 24),
                                  width = 300, height = 60,
                                  corner_radius = 20,
                                  #fg_color="#327fe3",
                                  fg_color="#2fa572", 
                                  command=lambda: appointments(conn, root))
button2.place(relx=0.5, rely=0.45, anchor="center")
# New window #appointment_window

# Version
version = customtkinter.CTkLabel(root, 
                                text="MeetMe v2.5",
                                text_color = "#2fa572",
                                font = ("Helvetica", 16))
version.place(relx=0.8, rely=0.9, anchor="center")

# GitHub link

#Define a callback function
def callback(url):
   webbrowser.open_new_tab(url)

link = customtkinter.CTkLabel(root, 
                                text="view GitHub repository",
                                text_color = "#2fa572",
                                font = ("Helvetica", 16),
                                cursor ="hand2")
link.bind("<Button-1>", lambda e:
callback("https://github.com/Harry2gks/PLHPRO-5-PROJECT"))
link.place(relx=0.2, rely=0.9, anchor="center")