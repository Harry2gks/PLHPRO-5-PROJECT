import tkinter as tk 
from tkinter import*
from PIL import ImageTk, Image # ---> αν υπογραμμίζει την γραμμη αυτη, θελει επανεγκατασταση η Python, αλλά το πρόγραμμα τρέχει <-----------
import customtkinter

from MeetMePack.database import *
from MeetMePack.client import *
from MeetMePack.appointment import *
from MeetMePack.display import *
from MeetMePack.Day_Appointments_window_actions import *
from MeetMePack.EditAppointment_window import *

def search_appointment_by_day_local(conn, root, search_entry):
    new_window2 = tk.Toplevel(root)
    new_window2.title("Ραντεβού Ημέρας")
    new_window2.iconbitmap("MeetMe_icon.ico")
    new_window2.geometry("1200x700")  # Set width and height
    new_window2.minsize(width=1200, height=700) # Set MINIMUM width and height ALLOWED
    new_window2.configure(background='#282c34')

    # -------------- Frame for a better items position --------------------
    headers_frame = customtkinter.CTkFrame(master=new_window2,                 
                                           fg_color="transparent")
    headers_frame.place(relwidth=1, relheight=0.2)
    # Configure columns to expand proportionally
    headers_frame.grid_columnconfigure(0, weight=1)
    headers_frame.grid_columnconfigure(1, weight=1)
    headers_frame.grid_columnconfigure(2, weight=1)
    headers_frame.grid_columnconfigure(3, weight=1)
    headers_frame.grid_columnconfigure(4, weight=1)
    headers_frame.grid_columnconfigure(5, weight=1)
    headers_frame.grid_columnconfigure(6, weight=1)
    headers_frame.grid_columnconfigure(7, weight=1)

    appointments_frame = customtkinter.CTkScrollableFrame(master=new_window2,
                                            fg_color="transparent")
    appointments_frame.place(rely=0.2, relwidth=1, relheight=0.7)
    # Configure columns to expand proportionally
    appointments_frame.grid_columnconfigure(0, weight=1)
    appointments_frame.grid_columnconfigure(1, weight=1)
    appointments_frame.grid_columnconfigure(2, weight=1)
    appointments_frame.grid_columnconfigure(3, weight=1)
    appointments_frame.grid_columnconfigure(4, weight=1)
    appointments_frame.grid_columnconfigure(4, weight=1)
    appointments_frame.grid_columnconfigure(5, weight=1)
    appointments_frame.grid_columnconfigure(6, weight=1)
    appointments_frame.grid_columnconfigure(7, weight=1)
     # -------------- Frame for a better items position --------------------
    
    # --------------------- Position the headers_frame top of the window ------------------------
    label = customtkinter.CTkLabel(headers_frame,
                                   text=f"Ραντεβού Ημέρας: {search_entry.get()}",
                                   text_color = "#f1fff2",
                                   font = ("Helvetica", 26))
    label.place(anchor="center", relx=0.5, rely=0.2) 
    # --------------------- Position the headers_frame top of the window ------------------------

    appointment = appointments_per_day(conn, date=search_entry.get())
    if appointment == 0:
        label = customtkinter.CTkLabel(new_window2,
                                       text="Δεν υπάρχουν Ραντεβού",
                                       text_color = "#f1fff2",
                                       font = ("Helvetica", 26))
        label.place(anchor="center", relx=0.5, rely=0.4)
    else:
        headers = ['Κωδικός Ραντεβού:', 'Ημερομηνία:', 'Ώρα Έναρξης:', 'Ώρα λήξης:', 'Διάρκεια:', 'ID Πελάτη:', 'Όνομα:',
           'Επώνυμο:', 'Τηλέφωνο:', 'Email:']

        for i, header in enumerate(headers[1:], start=1):
            if i != 5:
                label = customtkinter.CTkLabel(appointments_frame,
                                            text=header,
                                            text_color="#f1fff2",
                                            font=("Helvetica", 18))
                if i == 1:
                    label.grid(row=0, column=i-1, padx=0, pady=5, sticky="ew" )  
                elif i == 2:
                    label.grid(row=0, column=i-1, padx=0, pady=5, sticky="ew" )
                elif i == 3:
                    label.grid(row=0, column=i-1, padx=0, pady=5, sticky="ew" )
                elif i == 4:
                    label.grid(row=0, column=i-1, padx=0, pady=5, sticky="ew" )
                elif i == 6:
                    label.grid(row=0, column=i-2, padx=0, pady=5, sticky="ew" )
                elif i == 7:
                    label.grid(row=0, column=i-2, padx=0, pady=5, sticky="ew" ) 
                elif i == 8:
                    label.grid(row=0, column=i-2, padx=0, pady=5, sticky="ew" )
                elif i == 9:
                    label.grid(row=0, column=i-2, padx=0, pady=5, sticky="ew" )   


        # ------------------------------- Position the data ---------------------------------------------------
        for i, appointment in enumerate(appointment):
            for j in range(1, 5):
                label = customtkinter.CTkLabel(appointments_frame,
                                            text=appointment[j],
                                            text_color="#f1fff2",
                                            font=("Helvetica", 16))
                if j == 1:
                    label.grid(row=i+1, column=j-1, padx=0, pady=5, sticky="ew" )  
                elif j == 2:
                    label.grid(row=i+1, column=j-1, padx=0, pady=5, sticky="ew" ) 
                elif j == 3:
                    label.grid(row=i+1, column=j-1, padx=0, pady=5, sticky="ew" )
                elif j == 4:
                    label.grid(row=i+1, column=j-1, padx=0, pady=5, sticky="ew" )      
  
            client = search_client_by_id(conn, id=appointment[5])
            for k in range(0, 5):
                if k != 0:
                    label = customtkinter.CTkLabel(appointments_frame,
                                                text=client[k],
                                                text_color="#f1fff2",
                                                font=("Helvetica", 16))         
                if k == 1:
                    label.grid(row=i+1, column=k+3, padx=0, pady=5, sticky="ew" )
                elif k == 2:
                    label.grid(row=i+1, column=k+3, padx=0, pady=5, sticky="ew" )
                elif k == 3:
                    label.grid(row=i+1, column=k+3, padx=0, pady=5, sticky="ew" )
                elif k == 4:
                    label.grid(row=i+1, column=k+3, padx=0, pady=5, sticky="ew" )  

            # ------------------------------------- BUTTONS -------------------------------------------------------------
            edit_rantevou_icon =  customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-edit-48.png"),
                                            light_image=Image.open("MeetMe 2.0/icons/icons8-edit-48.png"),
                                            size = (30,30))                         
            edit_rantevou = customtkinter.CTkButton(appointments_frame, 
                                    #text="edit",
                                    image = edit_rantevou_icon,
                                    text="",
                                    fg_color = "#282c34",
                                    hover_color = "#c9c9c9", 
                                    corner_radius = 5,
                                    border_width = 2,
                                    border_color = "#282c34", 
                                    width = 30, 
                                    height = 30,
                                    command=lambda appointment=appointment: open_edit_appointment_local_appointment(conn, root, new_window2, appointment))
            edit_rantevou.grid(row=i+1, column=10, padx=10, pady=5, sticky="e")
            # New window "EditAppointment"

            del_rantevou_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-trash-48.png"),
                                        light_image=Image.open("MeetMe 2.0/icons/icons8-trash-48.png"),
                                        size = (30,30))                         
            del_rantevou = customtkinter.CTkButton(appointments_frame, 
                                    #text="delete",
                                    image = del_rantevou_icon,
                                    text="",
                                    fg_color = "#282c34",
                                    hover_color = "#c9c9c9", 
                                    corner_radius = 5,
                                    border_width = 2,
                                    border_color = "#282c34", 
                                    width = 30, 
                                    height = 30,
                                    command=lambda appointment=appointment: del_appointment_local_appointment(conn, new_window2, appointment))
            del_rantevou.grid(row=i+1, column=11, padx=10, pady=5, sticky="e")
            # function No 1

        export_button_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-export-excel-48.png"),
                                            light_image=Image.open("MeetMe 2.0/icons/icons8-export-excel-48.png"),
                                            size = (30,30))                         
        export_button = customtkinter.CTkButton(headers_frame, 
                                #text="xls",
                                image=export_button_icon,
                                text="",
                                fg_color = "#282c34",
                                hover_color = "#c9c9c9", 
                                corner_radius = 5,
                                border_width = 2,
                                border_color = "#282c34", 
                                width = 30, 
                                height = 30,
                                command=lambda: export_xls_local(conn, search_entry))
        export_button.place(anchor="center", relx=0.45, rely=0.5)
        # function No 2

        email_button_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-send-email-48.png"),
                                            light_image=Image.open("MeetMe 2.0/icons/icons8-send-email-48.png"),
                                            size = (30,30))                         
        email_button = customtkinter.CTkButton(headers_frame, 
                                #text="e-mail",
                                image=email_button_icon,
                                text="",
                                fg_color = "#282c34",
                                hover_color = "#c9c9c9", 
                                corner_radius = 5,
                                border_width = 2,
                                border_color = "#282c34", 
                                width = 30, 
                                height = 30,
                                command=lambda: email_local(conn, search_entry))
        email_button.place(anchor="center", relx=0.55, rely=0.5)
            # function No 3
        # ---------------------------------- BUTTONS ------------------------------------------------------

       
