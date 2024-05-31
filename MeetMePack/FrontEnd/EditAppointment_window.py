from tkinter import*
from PIL import Image # ---> αν υπογραμμίζει την γραμμη αυτη, θελει επανεγκατασταση η Python, αλλά το πρόγραμμα τρέχει <-----------
import customtkinter
from MeetMePack.ConnectBackFrontEnd.EditAppointment_window_actions import *
from MeetMePack.BackEnd.supporting_functions import resource_path


def open_edit_appointment_local_appointment(conn, root, new_window2, appointment):
    new_window3 = tk.Toplevel(root)
    new_window3.title("Επεξεργασία Ραντεβού")
    new_window3.iconbitmap(resource_path("icons\\MeetMe_icon.ico"))
    new_window3.geometry("1200x700")  # Set width and height
    new_window3.minsize(width=1200, height=700) # Set MINIMUM width and height ALLOWED
    new_window3.configure(background='#282c34')

    label = customtkinter.CTkLabel(new_window3, text="Επεξεργασία Ραντεβού", text_color = "#f1fff2", font = ("Helvetica", 16))
    label.place(relx=0.5, rely=0.1, anchor="center")  

    client = search_client_by_id(conn, id=appointment[5])

    code_label = customtkinter.CTkLabel(new_window3, text="Κωδικός", text_color = "#f1fff2", font = ("Helvetica", 16))
    code_label.place(relx=0.3, rely=0.2, anchor="center")
    code_value = customtkinter.CTkEntry(new_window3, width = 150, corner_radius = 50, fg_color="#282c34", text_color = "#f1fff2")
    code_value.place(relx=0.4, rely=0.2, anchor="center")
    code_value.insert(0, f"{appointment[0]}")
    code_value.configure(state='readonly')

    date_label = customtkinter.CTkLabel(new_window3, text="Ημερομηνία", text_color = "#f1fff2", font = ("Helvetica", 16))
    date_label.place(relx=0.3, rely=0.3, anchor="center")
    date_value = customtkinter.CTkEntry(new_window3, width = 150, corner_radius = 50, fg_color="#343638", text_color = "#f1fff2")
    date_value.place(relx=0.4, rely=0.3, anchor="center")
    date_value.insert(0, f"{appointment[1]}")

    start_label = customtkinter.CTkLabel(new_window3, text="Απο", text_color = "#f1fff2", font = ("Helvetica", 16))
    start_label.place(relx=0.3, rely=0.4, anchor="center")
    start_value = customtkinter.CTkEntry(new_window3, width = 150, corner_radius = 50, fg_color="#343638", text_color = "#f1fff2")
    start_value.place(relx=0.4, rely=0.4, anchor="center")
    start_value.insert(0, f"{appointment[2]}")

    end_label = customtkinter.CTkLabel(new_window3, text="Εως", text_color = "#f1fff2", font = ("Helvetica", 16))
    end_label.place(relx=0.3, rely=0.5, anchor="center")
    end_value = customtkinter.CTkEntry(new_window3, width = 150, corner_radius = 50, fg_color="#282c34", text_color = "#f1fff2")
    end_value.place(relx=0.4, rely=0.5, anchor="center")
    end_value.insert(0, f"{appointment[3]}")
    end_value.configure(state='readonly')

    during_label = customtkinter.CTkLabel(new_window3, text="Διάρκεια", text_color = "#f1fff2", font = ("Helvetica", 16))
    during_label.place(relx=0.3, rely=0.6, anchor="center")
    during_value = customtkinter.CTkEntry(new_window3, width = 150, corner_radius = 50, fg_color="#343638", text_color = "#f1fff2")
    during_value.place(relx=0.4, rely=0.6, anchor="center")
    during_value.insert(0, f"{appointment[4]}")

    # -- Αυτά δεν υπάρχουν στο παράθυρο --

    id_client_label = customtkinter.CTkLabel(new_window3, text="ID Πελάτη", text_color = "#f1fff2", font = ("Helvetica", 16))
    id_client_label.place(relx=0.5, rely=0.2, anchor="center")
    id_client_value = customtkinter.CTkEntry(new_window3, width = 150, corner_radius = 50, fg_color="#282c34", text_color = "#f1fff2")
    id_client_value.place(relx=0.6, rely=0.2, anchor="center")
    id_client_value.insert(0, f"{appointment[5]}")
    id_client_value.configure(state='readonly')

    name_client_label = customtkinter.CTkLabel(new_window3, text="Όνομα", text_color = "#f1fff2", font = ("Helvetica", 16))
    name_client_label.place(relx=0.5, rely=0.3, anchor="center")
    name_client_value = customtkinter.CTkEntry(new_window3, width = 150, corner_radius = 50, fg_color="#282c34", text_color = "#f1fff2")
    name_client_value.place(relx=0.6, rely=0.3, anchor="center")
    name_client_value.insert(0, f"{client[1]}")
    name_client_value.configure(state='readonly')

    surname_client_label = customtkinter.CTkLabel(new_window3, text="Επώνυμο", text_color = "#f1fff2", font = ("Helvetica", 16))
    surname_client_label.place(relx=0.5, rely=0.4, anchor="center")
    surname_client_value = customtkinter.CTkEntry(new_window3, width = 150, corner_radius = 50, fg_color="#282c34", text_color = "#f1fff2")
    surname_client_value.place(relx=0.6, rely=0.4, anchor="center")
    surname_client_value.insert(0, f"{client[2]}")
    surname_client_value.configure(state='readonly')

    phone_client_label = customtkinter.CTkLabel(new_window3, text="Τηλέφωνο", text_color = "#f1fff2", font = ("Helvetica", 16))
    phone_client_label.place(relx=0.5, rely=0.5, anchor="center")
    phone_client_value = customtkinter.CTkEntry(new_window3, width = 150, corner_radius = 50, fg_color="#282c34", text_color = "#f1fff2")
    phone_client_value.place(relx=0.6, rely=0.5, anchor="center")
    phone_client_value.insert(0, f"{client[3]}")
    phone_client_value.configure(state='readonly')

    email_client_label = customtkinter.CTkLabel(new_window3, text="Email", text_color = "#f1fff2", font = ("Helvetica", 16))
    email_client_label.place(relx=0.5, rely=0.6, anchor="center")
    email_client_value = customtkinter.CTkEntry(new_window3, width = 150, corner_radius = 50, fg_color="#282c34", text_color = "#f1fff2")
    email_client_value.place(relx=0.6, rely=0.6, anchor="center")
    email_client_value.insert(0, f"{client[4]}")
    email_client_value.configure(state='readonly')

    # Load the image for the save button icon
    save_button_icon = customtkinter.CTkImage(dark_image=Image.open(resource_path("icons\\icons8-save-48.png")),
                                              light_image=Image.open(resource_path("icons\\icons8-save-48.png")),
                                              size = (30,30))
    save_button = customtkinter.CTkButton(new_window3, 
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
                                          command=lambda: save_edit_rantevou_local(conn, code_value, date_value, start_value, during_value, end_value, new_window2, new_window3))
    save_button.place(relx=0.5, rely=0.7, anchor="center")
    # fuction No 1

