import xlsxwriter
import smtplib
from pathlib import Path
from MeetMePack.BackEnd.client import *
from MeetMePack.BackEnd.appointment import *
from MeetMePack.BackEnd.email_settings import *


def print_client(client):
    try:
        if client == 0:
            print("No entry")
        else:
            print("Client ID:", client[0])
            print("Name:", client[1])
            print("Surname:", client[2])
            print("Phone:", client[3])
            print("Email:", client[4])
            print()
    except Exception as e:
        print(f"Failed to print client: {e}")
        return None


def print_appointment(conn, appointment):
    try:
        if appointment == 0:
            print("No entry")
        else:
            print("Appointment ID:", appointment[0])
            print("Date:", appointment[1])
            print("Start Time:", appointment[2])
            print("End Time:", appointment[3])
            print("Duration:", appointment[4])
            # Using the client id, we print the clients' details together with each appointment
            print_client(search_client_by_id(conn, appointment[5]))
            print()
    except Exception as e:
        print(f"Failed to print client: {e}")
        return None

def print_appointments(conn, appointments):
    try:
        if appointments == 0:
            print("No entry")
        else:
            for appointment in appointments:
                print_appointment(conn, appointment)
                print()
    except Exception as e:
        print(f"Failed to print appointments: {e}")
        return None


def extract_xls(conn, date):
    try:
        # Find the appointment of the date
        appointments = appointments_per_day(conn, date)

        # Use pathlib to get the path to the Downloads folder
        downloads_path = Path.home() / "Downloads"

        # Create the Excel file name with the date
        file_name = f"Appointments_{date.replace('/', '-')}.xlsx"
        full_path = downloads_path / file_name

        # Begin writing the Excel file
        workbook = xlsxwriter.Workbook(str(full_path))

        # Create format to align text in the center of the cell
        format_center = workbook.add_format({'align': 'center'})

        # Create format for Header
        header_format = workbook.add_format({
            'bold': True,
            'bg_color': '#D3D3D3',
            'align': 'center'
        })

        # Create format for the title of table
        title_format = workbook.add_format({
            'align': 'center',
            'bold': True,
            'font_size': 14
        })

        # Text of title
        title = f"Appointments {date}"

        # Headers of the table
        headers = ['APPOINTMENT ID', 'DATE', 'START TIME', 'END TIME', 'DURATION (min)', 'CLIENT ID', 'NAME', 'SURNAME', 'PHONE', 'EMAIL']

        # Create worksheet
        worksheet = workbook.add_worksheet()

        # Merge cells, write title with its format
        worksheet.merge_range(f'A1:J1', title, title_format)

        # Write the headers with their format
        for i, header in enumerate(headers):
            worksheet.write(2, i, header, header_format)
            worksheet.set_column(i, i, 20)

        # Write the table entries
        for row_num, appointment in enumerate(appointments, 1):
            # Write appointment's details
            for col_num, column in enumerate(appointment):
                worksheet.write(row_num+2, col_num, column, format_center)
            # Write client's details
            for col_num, column in enumerate(search_client_by_id(conn, appointment[5])):
                worksheet.write(row_num+2, col_num+5, column, format_center)

        # Close workbook
        workbook.close()

        print("File was saved!")

    except Exception as e:
        print(f"Failed to extract Excel file: {e}")
        return 0


def remind_email(conn, date):
    appointments = appointments_per_day(conn, date)

    try:
        # Connect server
        smtp = smtplib.SMTP(smtp_server, port)
        smtp_response = smtp.ehlo()
        print(f"EHLO response: {smtp_response}")
        smtp.starttls()
        smtp_response = smtp.ehlo()  # Re-send EHLO after starttls
        print(f"EHLO after STARTTLS response: {smtp_response}")
        smtp.login(sender_email, password)

        # Loop for each appointment
        for appointment in appointments:
            # Find the client's email
            receiver_email = search_client_by_id(conn, appointment[5])[4]

            # Create the message using date and the name of client
            message = """Subject: MeetMe: Remind your Appointment on %s\n\n     
            Dear %s,
    
            We would like to remind you your appointment on %s at %s.
    
            See you soon!
    
            Best regards,
            MeetMe Team""" % (date, search_client_by_id(conn, appointment[5])[1], date, appointment[2])

            message = message.encode('utf-8')

            # Send email
            smtp.sendmail(sender_email, receiver_email, message)

            print(f"Email sent successfully! (appointment id: {appointment[0]})")

        return 1
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        # Disconnect server
        smtp.quit()
