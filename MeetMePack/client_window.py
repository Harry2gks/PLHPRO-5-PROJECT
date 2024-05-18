import tkinter as tk 
from tkinter import*
from PIL import ImageTk, Image # ---> αν υπογραμμίζει την γραμμη αυτη, θελει επανεγκατασταση η Python, αλλά το πρόγραμμα τρέχει <-----------
import customtkinter

from MeetMePack.database import *
from MeetMePack.client import *
from MeetMePack.appointment import *
from MeetMePack.display import *
from MeetMePack.client_window_actions import *
from MeetMePack.clientAppointments_window import *
from MeetMePack.New_Appointment_window import *


def client_list(conn, root):
    new_window = tk.Toplevel(root)
    new_window.title("καρτέλα Πελάτη")
    new_window.iconbitmap("MeetMe_icon.ico")
    new_window.geometry("1200x700")  # Set width and height
    new_window.configure(background='#282c34')
    new_window.minsize(width=1200, height=700)

    # labels for search fields
    label = customtkinter.CTkLabel(new_window, 
                     text="καρτέλα Πελάτη",
                     text_color = "#f1fff2",
                     font = ("Helvetica", 26))
    
    # Search Fields / default phone
    search_label = customtkinter.CTkLabel(new_window, 
                                          text="Τηλέφωνο",
                                          text_color = "#f1fff2",
                                          font = ("Helvetica", 16))
    search_value = customtkinter.CTkEntry(new_window, 
                                          width = 150,
                                          corner_radius = 50)

    id_label = customtkinter.CTkLabel(new_window, 
                                          text="id",
                                          text_color = "#f1fff2",
                                          font = ("Helvetica", 16))
    id_value = customtkinter.CTkEntry(new_window, 
                                      state='readonly',
                                      width = 150,
                                      corner_radius = 50) 

    name_label = customtkinter.CTkLabel(new_window, 
                                          text="Όνομα",
                                          text_color = "#f1fff2",
                                          font = ("Helvetica", 16))
    name_value = customtkinter.CTkEntry(new_window,
                                         state='readonly',
                                         width = 150,
                                         corner_radius = 50)
    
    surname_label = customtkinter.CTkLabel(new_window, 
                                          text="Επώνυμο",
                                          text_color = "#f1fff2",
                                          font = ("Helvetica", 16))
    surname_value = customtkinter.CTkEntry(new_window,
                                           state='readonly',
                                           width = 150,
                                           corner_radius = 50)
    
    # Anti-search Fields / default email
    anti_search_label = customtkinter.CTkLabel(new_window, 
                                          text="Email",
                                          text_color = "#f1fff2",
                                          font = ("Helvetica", 16))
    anti_search_value = customtkinter.CTkEntry(new_window, 
                                               state='readonly',
                                               width = 150,
                                               corner_radius = 50)
    
    # -------------------------- Buttons -----------------------------------
    # Load the image for the phone search button icon
    phone_search_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/mobile-search.png"),
                                               light_image=Image.open("MeetMe 2.0/icons/mobile-search.png"),
                                               size = (30,30))
                            
    phone_search = customtkinter.CTkButton(new_window,      
                                          #text="Αναζήτηση με τηλέφωνο", 
                                          image=phone_search_icon,
                                          text="",
                                          fg_color = "#282c34",
                                          hover_color = "#c9c9c9", 
                                          corner_radius = 5,
                                          border_width = 2,
                                          border_color = "#282c34", 
                                          width = 30, 
                                          height = 30,
                                          command=lambda: phone_search_action(search_value, search_label, anti_search_label, id_value, name_value, surname_value, anti_search_value))  
    # Function No 2

    # Load the image for the email search button icon
    email_search_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-search-in-mail-48.png"),
                                               light_image=Image.open("MeetMe 2.0/icons/icons8-search-in-mail-48.png"),
                                               size = (30,30))
    email_search = customtkinter.CTkButton(new_window, 
                                            #text="Αναζήτηση με email", 
                                            text="",
                                            image=email_search_icon,
                                            fg_color = "#282c34",
                                            hover_color = "#c9c9c9", 
                                            corner_radius = 5,
                                            border_width = 2,
                                            border_color = "#282c34", 
                                            width = 30, 
                                            height = 30,
                                            command=lambda: email_search_action(search_value, search_label, anti_search_label, id_value, name_value, surname_value, anti_search_value)) 
    # Function No 3

    # Load the image for the new client button icon
    new_client_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-new-contact-48.png"),
                                               light_image=Image.open("MeetMe 2.0/icons/icons8-new-contact-48.png"),
                                               size = (30,30))
    new_client = customtkinter.CTkButton(new_window, 
                                         #text="Νέος Πελάτης", 
                                         image=new_client_icon,
                                         text="",
                                         fg_color = "#282c34",
                                         hover_color = "#c9c9c9", 
                                         corner_radius = 5,
                                         border_width = 2,
                                         border_color = "#282c34", 
                                         width = 30, 
                                         height = 30,
                           command=lambda: add_client_local(id_value, search_value, name_value, surname_value, anti_search_value))
    # Function No 4

    # Load the image for the search button icon
    search_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-search-48.png"),
                                               light_image=Image.open("MeetMe 2.0/icons/icons8-search-48.png"),
                                               size = (30,30))                             
    search_button = customtkinter.CTkButton(new_window, 
                                          #text="search",
                                          image=search_icon,
                                          text="",
                                          fg_color = "#282c34",
                                          hover_color = "#c9c9c9", 
                                          corner_radius = 5,
                                          border_width = 2,
                                          border_color = "#282c34", 
                                          width = 30, 
                                          height = 30,
                                          command=lambda: search_client_local(conn, search_value, id_value, name_value, surname_value, anti_search_value))  
    # Function No 5

    # Load the image for the edit button icon
    edit_button_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-edit-48.png"),
                                               light_image=Image.open("MeetMe 2.0/icons/icons8-edit-48.png"),
                                               size = (30,30))                         
    edit_button = customtkinter.CTkButton(new_window, 
                                          #text="edit",
                                          image=edit_button_icon,
                                          text="",
                                          fg_color = "#282c34",
                                          hover_color = "#c9c9c9", 
                                          corner_radius = 5,
                                          border_width = 2,
                                          border_color = "#282c34", 
                                          width = 30, 
                                          height = 30,
                                          command=lambda: edit_client(id_value, search_value, name_value, surname_value, anti_search_value))
    # Function No 6

    # Load the image for the delete button icon
    delete_button_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-trash-48.png"),
                                               light_image=Image.open("MeetMe 2.0/icons/icons8-trash-48.png"),
                                               size = (30,30))
    delete_button = customtkinter.CTkButton(new_window, 
                                          #text="delete",
                                          image=delete_button_icon,
                                          text="",
                                          fg_color = "#282c34",
                                          hover_color = "#c9c9c9", 
                                          corner_radius = 5,
                                          border_width = 2,
                                          border_color = "#282c34", 
                                          width = 30, 
                                          height = 30,
                                          command=lambda: delete_client_local(conn, id_value, search_value, name_value, surname_value, anti_search_value))  
    # Function No 7

    # Load the image for the save button icon
    save_button_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-save-48.png"),
                                               light_image=Image.open("MeetMe 2.0/icons/icons8-save-48.png"),
                                               size = (30,30))              
    save_button = customtkinter.CTkButton(new_window, 
                                          #text="save",
                                          image=save_button_icon,
                                          text="",
                                          fg_color = "#282c34",
                                          hover_color = "#c9c9c9", 
                                          corner_radius = 5,
                                          border_width = 2,
                                          border_color = "#282c34", 
                                          width = 30, 
                                          height = 30,
                                          command=lambda: save_changes(conn, id_value, name_value, surname_value, search_value, anti_search_value))   
    # Function No 8

    # Load the image for the appointments button icon
    appointments_button_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-calendar-48.png"),
                                               light_image=Image.open("MeetMe 2.0/icons/icons8-calendar-48.png"),
                                               size = (30,30))                   
    rantevou_button = customtkinter.CTkButton(new_window, 
                                              #text="Ραντεβού Πελάτη",
                                              image=appointments_button_icon,
                                              text="",
                                              fg_color = "#282c34",
                                              hover_color = "#c9c9c9", 
                                              corner_radius = 5,
                                              border_width = 2,
                                              border_color = "#282c34", 
                                              width = 30, 
                                              height = 30,
                                              command=lambda: client_appointments(conn, root, id_value, name_value, surname_value))
    # New window "clientAppointments"

    # Load the image for the appointments button icon
    new_appointment_button_icon = customtkinter.CTkImage(dark_image=Image.open("MeetMe 2.0/icons/icons8-calendar-plus-48.png"),
                                               light_image=Image.open("MeetMe 2.0/icons/icons8-calendar-plus-48.png"),
                                               size = (30,30))           
    neo_rantevou_button = customtkinter.CTkButton(new_window, 
                                                  #text="Νεο ραντεβού",
                                                  image=new_appointment_button_icon,
                                                  text="",
                                                  fg_color = "#282c34",
                                                  hover_color = "#c9c9c9", 
                                                  corner_radius = 5,
                                                  border_width = 2,
                                                  border_color = "#282c34", 
                                                  width = 30, 
                                                  height = 30,
                                                  command=lambda: open_appointment(conn, root, id_value, name_value, surname_value, search_value, anti_search_value)) 
    # New window "New_Appointment_window"

    # ---------------- center content ----------------------------
    search_label.place(anchor="center",relx=0.4, rely=0.2)
    search_value.place(anchor="center",relx=0.5, rely=0.2)
    id_label.place(anchor="center",relx=0.4, rely=0.3)
    id_value.place(anchor="center",relx=0.5, rely=0.3)
    name_label.place(anchor="center",relx=0.4, rely=0.4)
    name_value.place(anchor="center",relx=0.5, rely=0.4)
    surname_label.place(anchor="center",relx=0.4, rely=0.5)
    surname_value.place(anchor="center",relx=0.5, rely=0.5)
    anti_search_label.place(anchor="center",relx=0.4, rely=0.6)
    anti_search_value.place(anchor="center",relx=0.5, rely=0.6)
    # ----------- buttons -------------------
    phone_search.place(relx=0.3, rely=0.7)
    email_search.place(relx=0.35, rely=0.7)
    new_client.place(relx=0.4, rely=0.7)
    search_button.place(relx=0.45, rely=0.7)
    edit_button.place(relx=0.5, rely=0.7)
    delete_button.place(relx=0.55, rely=0.7)
    save_button.place(relx=0.60, rely=0.7)
    rantevou_button.place(relx=0.65, rely=0.7)
    neo_rantevou_button.place(relx=0.7, rely=0.7)
    # ---------------- center content ----------------------------