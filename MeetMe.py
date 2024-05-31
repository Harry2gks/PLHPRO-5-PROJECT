from MeetMePack.FrontEnd.intro import intro
from MeetMePack.FrontEnd.main_window import root

root.after(10, intro)  # Open fist the main window and after the intro
root.mainloop()

