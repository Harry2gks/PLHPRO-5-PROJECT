from MeetMePack.display import *


# function No 1
def edit_client_rantevou(conn, new_window4, code_value, date_value, start_value, during_value):
    change_appointment_details(conn, appointment_id=code_value.get(), new_date=date_value.get(), new_start_time=start_value.get(), new_duration=during_value.get())
    new_window4.destroy()
