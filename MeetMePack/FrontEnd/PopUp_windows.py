import tkinter as tk
import customtkinter
from MeetMePack.BackEnd.supporting_functions import resource_path

def pop_up(root, notification):
    pop_up = tk.Toplevel(root)
    pop_up.title("Ειδοποίηση")
    pop_up.iconbitmap(resource_path("icons\\MeetMe_icon.ico"))
    pop_up.geometry("600x200")  # Set width and height
    pop_up.configure(background='#282c34')
    pop_up.resizable(False, False)

    text = customtkinter.CTkLabel(pop_up,
                                     text= notification,
                                     text_color="#f1fff2",
                                     font=("Helvetica", 16))
    text.place(relx=0.5, rely=0.35, anchor="center")

    close_button = customtkinter.CTkButton(pop_up,
                                      text="OK",
                                      text_color="#f1fff2",
                                      font=("Helvetica", 16),
                                      width=60,
                                      height=30,
                                      corner_radius=20,
                                      fg_color="#2fa572",
                                      command=lambda: pop_up.destroy())
    close_button.place(relx=0.5, rely=0.65, anchor="center")
