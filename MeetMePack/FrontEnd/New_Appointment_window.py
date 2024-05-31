from MeetMePack.ConnectBackFrontEnd.New_Appointment_window_actions import *
from MeetMePack.BackEnd.supporting_functions import resource_path


search_by = "phone"     #global default search field
editable_fields = False  #global if fields are in editable mode or not
new_client_process = False #global if we create a new client

def open_appointment(conn, root, id_value, name_value, surname_value, search_value, anti_search_value):
    global search_by
    if id_value.get() != "":
        new_window3 = tk.Toplevel(root)
        new_window3.title("Νεο Ραντεβού")
        new_window3.iconbitmap(resource_path("icons\\MeetMe_icon.ico"))
        new_window3.geometry("1200x700")  # Set width and height
        new_window3.minsize(width=1200, height=700) # Set MINIMUM width and height ALLOWED
        new_window3.configure(background='#282c34')
        label = customtkinter.CTkLabel(new_window3,
                                       text="Προσθήκη Νέου Ραντεβού",
                                       text_color = "#f1fff2",
                                       font = ("Helvetica", 26))
        label.place(anchor="center",relx=0.5, rely=0.05)

        code_label = customtkinter.CTkLabel(new_window3,
                                            text="Κωδικός",
                                            text_color = "#f1fff2",
                                            font = ("Helvetica", 16))
        code_value = customtkinter.CTkEntry(new_window3,
                                            width = 150,
                                            corner_radius = 150,
                                            fg_color="#282c34",
                                            text_color = "#f1fff2")
        code_value.configure(state='readonly')

        date_label = customtkinter.CTkLabel(new_window3,
                                            text="Ημερομηνία",
                                            text_color = "#f1fff2",
                                            font = ("Helvetica", 16))
        date_value = customtkinter.CTkEntry(new_window3,
                                            width = 150,
                                            corner_radius = 150,
                                            fg_color="#343638",
                                            text_color = "#f1fff2")
        start_label = customtkinter.CTkLabel(new_window3,
                                            text="Απο",
                                            text_color = "#f1fff2",
                                            font = ("Helvetica", 16))
        start_value = customtkinter.CTkEntry(new_window3,
                                            width = 150,
                                            corner_radius = 150,
                                            fg_color="#343638",
                                            text_color = "#f1fff2")
        end_label = customtkinter.CTkLabel(new_window3,
                                            text="Εως",
                                            text_color = "#f1fff2",
                                            font = ("Helvetica", 16))
        end_value = customtkinter.CTkEntry(new_window3,
                                            width = 150,
                                            corner_radius = 150,
                                            fg_color="#282c34",
                                            text_color = "#f1fff2")
        end_value.configure(state='readonly')

        during_label = customtkinter.CTkLabel(new_window3,
                                            text="Διάρκεια",
                                            text_color = "#f1fff2",
                                            font = ("Helvetica", 16))
        during_value = customtkinter.CTkEntry(new_window3,
                                            width = 150,
                                            corner_radius = 150,
                                            fg_color="#343638",
                                            text_color = "#f1fff2")
        during_value.insert(0, string="30")

        id_client_label = customtkinter.CTkLabel(new_window3,
                                            text="ID Πελάτη",
                                            text_color = "#f1fff2",
                                            font = ("Helvetica", 16))
        id_client_value = customtkinter.CTkEntry(new_window3,
                                                width = 150,
                                                corner_radius = 150,
                                                fg_color="#282c34",
                                                text_color = "#f1fff2")
        id_client_value.insert(0, f"{id_value.get()}")
        id_client_value.configure(state='readonly')

        name_client_label = customtkinter.CTkLabel(new_window3,
                                                    text="Όνομα",
                                                    text_color = "#f1fff2",
                                                    font = ("Helvetica", 16))
        name_client_value = customtkinter.CTkEntry(new_window3,
                                                    width = 150,
                                                    corner_radius = 150,
                                                    fg_color="#282c34",
                                                    text_color = "#f1fff2")
        name_client_value.insert(0, f"{name_value.get()}")
        name_client_value.configure(state='readonly')

        surname_client_label = customtkinter.CTkLabel(new_window3,
                                                    text="Επώνυμο",
                                                    text_color = "#f1fff2",
                                                    font = ("Helvetica", 16))
        surname_client_value = customtkinter.CTkEntry(new_window3,
                                                    width = 150,
                                                    corner_radius = 150,
                                                    fg_color="#282c34",
                                                    text_color = "#f1fff2")
        surname_client_value.insert(0, f"{surname_value.get()}")
        surname_client_value.configure(state='readonly')

        phone_client_label = customtkinter.CTkLabel(new_window3,
                                                    text="Τηλέφωνο",
                                                    text_color = "#f1fff2",
                                                    font = ("Helvetica", 16))
        phone_client_value = customtkinter.CTkEntry(new_window3,
                                                    width = 150,
                                                    corner_radius = 150,
                                                    fg_color="#282c34",
                                                    text_color = "#f1fff2")
        if search_by == "phone":
            phone_client_value.insert(0, f"{search_value.get()}")
        elif search_by == "email":
            phone_client_value.insert(0, f"{anti_search_value.get()}")
        phone_client_value.configure(state='readonly')

        email_client_label = customtkinter.CTkLabel(new_window3,
                                                    text="Email",
                                                    text_color = "#f1fff2",
                                                    font = ("Helvetica", 16))
        email_client_value = customtkinter.CTkEntry(new_window3,
                                                    width = 150,
                                                    corner_radius = 150,
                                                    fg_color="#282c34",
                                                    text_color = "#f1fff2")
        if search_by == "phone":
            email_client_value.insert(0, f"{anti_search_value.get()}")
        elif search_by == "email":
            email_client_value.insert(0, f"{search_value.get()}")
        email_client_value.configure(state='readonly')

     # --------------------------- BUTTONS --------------------------------------------
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
                                                command=lambda: save_rantevou(conn, new_window3, code_value, id_client_value, date_value, start_value, during_value, end_value))
        save_button.place(anchor="center", relx=0.4, rely=0.7)
        # function No 1

        #discard_rantevou_button_icon = customtkinter.CTkImage(dark_image=Image.open("C:\\Users\\nikos\\OneDrive\\Υπολογιστής\\MeetMe 3.0\\icons\\icons8-trash-48.png"),
                                               #light_image=Image.open("C:\\Users\\nikos\\OneDrive\\Υπολογιστής\\MeetMe 3.0\\icons\\icons8-trash-48.png"),
                                               #size = (30,30))
        #discard_rantevou_button = customtkinter.CTkButton(new_window3,
                                          #text="delete",
                                          #image=discard_rantevou_button_icon,
                                          #text="",
                                          #fg_color = "#282c34",
                                          #hover_color = "#c9c9c9",
                                          #corner_radius = 5,
                                          #border_width = 2,
                                          #border_color = "#282c34",
                                          #width = 30,
                                          #height = 30,
                                          #command=lambda: delete_appointment_local(conn, code_value, date_value, start_value, end_value, during_value))
        #discard_rantevou_button.place(anchor="center", relx=0.6, rely=0.7)
        # function No 2

        # ------------------ Center Content ---------------------
        code_label.place(anchor="center",relx=0.3, rely=0.2)
        code_value.place(anchor="center",relx=0.4, rely=0.2)
        date_label.place(anchor="center",relx=0.3, rely=0.3)
        date_value.place(anchor="center",relx=0.4, rely=0.3)
        start_label.place(anchor="center",relx=0.3, rely=0.4)
        start_value.place(anchor="center",relx=0.4, rely=0.4)
        end_label.place(anchor="center",relx=0.3, rely=0.5)
        end_value.place(anchor="center",relx=0.4, rely=0.5)
        during_label.place(anchor="center",relx=0.3, rely=0.6)
        during_value.place(anchor="center",relx=0.4, rely=0.6)
        id_client_label.place(anchor="center",relx=0.6, rely=0.2)
        id_client_value.place(anchor="center",relx=0.7, rely=0.2)
        name_client_label.place(anchor="center",relx=0.6, rely=0.3)
        name_client_value.place(anchor="center",relx=0.7, rely=0.3)
        surname_client_label.place(anchor="center",relx=0.6, rely=0.4)
        surname_client_value.place(anchor="center",relx=0.7, rely=0.4)
        phone_client_label.place(anchor="center",relx=0.6, rely=0.5)
        phone_client_value.place(anchor="center",relx=0.7, rely=0.5)
        email_client_label.place(anchor="center", relx=0.6, rely=0.6)
        email_client_value.place(anchor="center", relx=0.7, rely=0.6)