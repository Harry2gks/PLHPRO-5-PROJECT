import tkinter as tk
from tkinter import ttk
from MeetMePack.database import *
from MeetMePack.client import *
from MeetMePack.appointment import *
from MeetMePack.display import *


# function No 1
def del_appointment_local_appointment(conn, new_window2, appointment):
    delete_appointment(conn, appointment_id=appointment[0])
    new_window2.destroy()


# function No 2
def export_xls_local(conn, search_entry):
    extract_xls(conn, date=search_entry.get())


# function No 3
def email_local(conn, search_entry):
    remind_email(conn, date=search_entry.get())