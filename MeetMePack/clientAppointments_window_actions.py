from MeetMePack.display import *


# function No 1
def del_appointment(conn, root, new_window2, id_value, name_value, surname_value, appointment):
    delete_appointment(conn, appointment_id=appointment[0])
    new_window2.destroy()


