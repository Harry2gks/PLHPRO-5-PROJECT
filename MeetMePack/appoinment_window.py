import tkinter as tk 
from tkinter import*
from PIL import ImageTk, Image # ---> αν υπογραμμίζει την γραμμη αυτη, θελει επανεγκατασταση η Python, αλλά το πρόγραμμα τρέχει <-----------
import customtkinter 

from MeetMePack.database import *
from MeetMePack.client import *
from MeetMePack.appointment import *
from MeetMePack.display import *
from MeetMePack.appointment_window_action import *
from MeetMePack.Day_Appointments_window import *


def appointments(conn, root):
    new_window = tk.Toplevel(root)
    new_window.title("Προβολή Ραντεβού ανά ημέρα")
    new_window.iconbitmap("MeetMe_icon.ico")
    new_window.geometry("1200x700")  # Set width and height
    #new_window.configure(background='#212029')
    new_window.configure(background='#282c34') 
    new_window.minsize(width=1200, height=700)

    # searchfield
    search_var = tk.StringVar()
    search_entry = customtkinter.CTkEntry(new_window, 
                                          textvariable=search_var,
                                          width=400,
                                          corner_radius = 50,
                                          fg_color="#282c34",
                                          text_color = "#f1fff2")
    search_entry.place(relx=0.5, rely=0.5, anchor="center")
    
    # Οδηγιες εισαγωγής ημερομηνίας
    search_label = customtkinter.CTkLabel(new_window, 
                                         text="Εισάγεται ημερομηνία μορφής DD/MM/YYYY",
                                         text_color = "#8d918d",
                                         font = ("Helvetica", 16))
    search_label.place(relx=0.5, rely=0.45, anchor="center")

    # Load the image for the search button icon
    search_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-search-48.png"),
                                         light_image=Image.open("MeetMe 2.0/icons/icons8-search-48.png"),
                                         size=(30,30))
    # button
    search_button = customtkinter.CTkButton(new_window, 
                                            text="",
                                            image=search_icon, 
                                            fg_color = "#f3f3f3",
                                            hover_color = "#c9c9c9",  
                                            width = 30, 
                                            height = 30,                                      
                                            command=lambda: search_appointment_by_day_local(conn, root, search_entry))
    # Place the button on the Grid
    search_button.place(relx=0.5, rely=0.5, anchor="center", x=search_entry.winfo_reqwidth()/2 + 30)
    # New window "Day_Appointments"
