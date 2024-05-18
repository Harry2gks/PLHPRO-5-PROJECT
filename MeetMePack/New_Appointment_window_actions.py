import tkinter as tk
from tkinter import ttk
from MeetMePack.database import *
from MeetMePack.client import *
from MeetMePack.appointment import *
from MeetMePack.display import *
from MeetMePack.client_window_actions import *
from MeetMePack.clientAppointments_window import *


# function No1
def save_rantevou(conn, new_window3, code_value, id_client_value, date_value, start_value, during_value, end_value):
    if code_value.get() == "":
        id = add_appointment(conn, client_id=id_client_value.get(), date=date_value.get(),
                             start_time=start_value.get(), duration=during_value.get())
        rantevou = search_appointment_by_id(conn, appointment_id=id)
        code_value.configure(state='normal')
        code_value.insert(0, f"{rantevou[0]}")
        code_value.configure(state='readonly')
        end_value.configure(state='normal')
        end_value.insert(0, f"{rantevou[3]}")
        end_value.configure(state='readonly')
        date_value.configure(state='readonly')
        start_value.configure(state='readonly')
        during_value.configure(state='readonly')
        new_window3.destroy()


# function No2
def delete_appointment_local(conn, code_value, date_value, start_value, end_value, during_value):
    if code_value.get() != "":
        rantevou = search_appointment_by_id(conn, appointment_id=code_value.get())
        delete_appointment(conn, appointment_id=rantevou[0])
        code_value.configure(state='normal')
        code_value.delete(0, tk.END)
        code_value.configure(state='readonly')
        date_value.configure(state='normal')
        date_value.delete(0, tk.END)
        start_value.configure(state='normal')
        start_value.delete(0, tk.END)
        end_value.configure(state='normal')
        end_value.delete(0, tk.END)
        end_value.configure(state='readonly')
        during_value.configure(state='normal')
        during_value.delete(0, tk.END)
        during_value.insert(0, string="30")


