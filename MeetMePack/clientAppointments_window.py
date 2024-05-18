import tkinter as tk 
from tkinter import*
from PIL import ImageTk, Image # ---> αν υπογραμμίζει την γραμμη αυτη, θελει επανεγκατασταση η Python, αλλά το πρόγραμμα τρέχει <-----------
import customtkinter

from MeetMePack.database import *
from MeetMePack.client import *
from MeetMePack.appointment import *
from MeetMePack.display import *
from MeetMePack.clientAppointments_window_actions import *
from MeetMePack.EditClientAppointment_window import *

def client_appointments(conn, root, id_value, name_value, surname_value):
    if id_value.get() != "":
        new_window2 = tk.Toplevel(root)
        new_window2.title("Ραντεβού Πελάτη")
        new_window2.iconbitmap("MeetMe_icon.ico")
        new_window2.geometry("1200x700")  # Set width and height
        new_window2.configure(background='#282c34')
        new_window2.minsize(width=1200, height=700)

        # -------------- Creating a Frame that holds the widgets inside --------------------
        headers_frame = customtkinter.CTkFrame(master=new_window2,                 
                                               fg_color="transparent")
        headers_frame.place(relwidth=1, relheight=0.2)
        # Configure columns to expand proportionally
        headers_frame.grid_columnconfigure(0, weight=1)
        headers_frame.grid_columnconfigure(1, weight=1)
        headers_frame.grid_columnconfigure(2, weight=1)
        headers_frame.grid_columnconfigure(3, weight=1)

        appointments_frame = customtkinter.CTkScrollableFrame(master=new_window2,
                                                    fg_color="transparent")
        appointments_frame.place(rely=0.2, relwidth=1, relheight=0.7)
        # Configure columns to expand proportionally
        appointments_frame.grid_columnconfigure(0, weight=1)
        appointments_frame.grid_columnconfigure(1, weight=1)
        appointments_frame.grid_columnconfigure(2, weight=1)
        appointments_frame.grid_columnconfigure(3, weight=1)
        appointments_frame.grid_columnconfigure(4, weight=1)
        # -------------- Creating a Frame that holds the widgets inside --------------------

        # ------------------------------- Position the headers_frame top of the window ---------------------------------------------------
        label = customtkinter.CTkLabel(headers_frame, 
                                       text=f"Ραντεβού Πελάτη: {name_value.get()} {surname_value.get()}",
                                       text_color = "#f1fff2",
                                       font = ("Helvetica", 26))
        label.place(anchor="center", relx=0.5, rely=0.2)  
        rantevou = appointments_per_client(conn, client_id=id_value.get())
        # ------------------------------- Position the headers_frame top of the window ---------------------------------------------------
        

        # --------- Η ΤΕΛΕΥΤΑΙΑ ΚΕΝΗ ΕΙΣΟΔΟΣ ΣΤΗΝ ΛΙΣΤΑ ΕΙΝΑΙ ΑΝΑΓΚΑΙΑ ΓΙΑ ΤΗΝ ΣΩΣΤΗ ΕΜΦΑΝΙΣΗ ΤΩΝ ΤΙΜΩΝ --------------------------
        headers = ['Κωδικός Ραντεβού', 'Ημερομηνία', 'Ώρα Έναρξης', 'Ώρα λήξης', 'Διάρκεια', ''] 
        if rantevou == 0:
            label = customtkinter.CTkLabel(new_window2,
                                           text="Δεν υπάρχουν Ραντεβού",
                                           text_color = "#f1fff2",
                                           font = ("Helvetica", 26))
            label.place(anchor="center", relx=0.5, rely=0.4)
        else:
            for i, header in enumerate(headers):
                if i != 0:
                    label = customtkinter.CTkLabel(appointments_frame, 
                                            text=header, 
                                            text_color = "#f1fff2",
                                            font = ("Helvetica", 18))
                    if i == 1:
                        label.grid(row=0, column=i-1, padx=0, pady=5, sticky="e" )  
                    elif i == 2:
                        label.grid(row=0, column=i-1, padx=0, pady=5, sticky="e" )
                    elif i == 3:
                        label.grid(row=0, column=i-1, padx=0, pady=5, sticky="e" )
                    elif i == 4:
                        label.grid(row=0, column=i-1, padx=0, pady=5, sticky="e" )  

            # ------------------------------- Position the data ---------------------------------------------------
            for i, appointment in enumerate(rantevou):
                for j in range(0, 5):
                    if j != 0:
                        label = customtkinter.CTkLabel(appointments_frame,
                                                        text=appointment[j],
                                                        text_color = "#f1fff2",
                                                        font = ("Helvetica", 16))
                    if j == 1:
                        label.grid(row=i+1, column=j-1, padx=0, pady=5, sticky="e" )
                    elif j == 2:
                        label.grid(row=i+1, column=j-1, padx=0, pady=5, sticky="e" )
                    elif j == 3:
                        label.grid(row=i+1, column=j-1, padx=0, pady=5, sticky="e" )
                    elif j == 4:
                        label.grid(row=i+1, column=j-1, padx=0, pady=5, sticky="e" )
                # ------------------------------- Position the data ---------------------------------------------------         

                # ------------------------------------- BUTTONS -------------------------------------------------------------
                edit_rantevou_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-edit-48.png"),
                                            light_image=Image.open("MeetMe 2.0/icons/icons8-edit-48.png"),
                                            size = (30,30))                         
                edit_rantevou = customtkinter.CTkButton(appointments_frame, 
                                        #text="edit",
                                        image=edit_rantevou_icon,
                                        text="",
                                        fg_color = "#282c34",
                                        hover_color = "#c9c9c9", 
                                        corner_radius = 5,
                                        border_width = 2,
                                        border_color = "#282c34", 
                                        width = 30, 
                                        height = 30,
                                        command=lambda appointment=appointment: open_edit_appointment(conn, root, new_window2, appointment, id_value, name_value, surname_value))
                edit_rantevou.grid(row=i+1, column=4, padx=10, pady=5, sticky="e")
                # New window "EditClientAppointment"

                    # Load the image for the delete button icon
                delete_rantevou_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-trash-48.png"),
                                            light_image=Image.open("MeetMe 2.0/icons/icons8-trash-48.png"),
                                            size = (30,30))
                del_rantevou = customtkinter.CTkButton(appointments_frame, 
                                        #text="delete",
                                        image=delete_rantevou_icon,
                                        text="",
                                        fg_color = "#282c34",
                                        hover_color = "#c9c9c9", 
                                        corner_radius = 5,
                                        border_width = 2,
                                        border_color = "#282c34", 
                                        width = 30, 
                                        height = 30,
                                        command=lambda appointment=appointment: del_appointment(conn, root, new_window2, id_value, name_value, surname_value, appointment))
                del_rantevou.grid(row=i+1, column=5, padx=10, pady=5, sticky="w")
                # ------------------------------------- BUTTONS -------------------------------------------------------------
                # function No 1