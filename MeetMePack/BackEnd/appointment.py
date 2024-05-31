import sqlite3
from datetime import datetime, timedelta

def appointment_end_time_calculate(start_time, duration):
    """Calculate the end time of the appointment"""
    try:
        # Turn str to time
        appointment_start_time = datetime.strptime(start_time, "%H:%M")
        # Turn duration to minutes and add them to time
        appointment_end_time = appointment_start_time + timedelta(minutes=int(duration))
        # Turn date to str
        end_time = appointment_end_time.strftime("%H:%M")
        return end_time
    except ValueError as e:
        print(f"Failed to calculate appointment end time: {e}")
        return None


def check_availability(conn, date, start_time, end_time):
    """Check if a specific day & time is available
        we check two cases, the case that the 2nd appointment
        overlaps the first and the case that the 2nd appointment
        starts during the duration of the 1st appointment."""
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM appointments
            WHERE date = ?
            AND ((start_time < ? AND end_time > ?) OR (start_time >= ? AND start_time < ?))""",
                    (date, start_time, start_time, start_time, end_time))
        no_availability = cur.fetchall()
        return no_availability
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return None


def add_appointment(conn, client_id, date, start_time, duration=30):
    """Create an appointment if there is availability and return 0 if there isn't"""
    try:
        # Calculate the end time
        end_time = appointment_end_time_calculate(start_time, duration)

        # Check for availability
        no_availability = check_availability(conn, date, start_time, end_time)

        if no_availability:
            print("No availability, check an other date/time.")
            return 0
        else:
            cur = conn.cursor()
            cur.execute("""
                INSERT INTO appointments (date, start_time, end_time, duration, client_id)
                VALUES (?, ?, ?, ?, ?)""", (date, start_time, end_time, duration, client_id))
            conn.commit()
            return cur.lastrowid
    except sqlite3.Error as e:
        print("SQLite error:", e)
        # undo all changes
        try:
            conn.rollback()
        except:
            print("Failed to undo all changes")
        return None


def change_appointment_details(conn, appointment_id, new_client_id=None, new_date=None, new_start_time=None, new_duration=None):
    """Change appointment details if there is availability and return 0 if there isn't"""
    try:
        cur = conn.cursor()
        # Save in Dictionary the fields which change
        changes = {}
        if new_client_id is not None:
            changes['client_id'] = new_client_id
        if new_date is not None:
            changes['date'] = new_date
        else:
            # If date doesn't change, save the date as new date
            # Thus, we are able to check availability later
            cur.execute("SELECT date FROM appointments WHERE id = ?", (appointment_id,))
            date = cur.fetchone()[0]
            new_date = date
        if new_start_time is not None:
            changes['start_time'] = new_start_time
        else:
            # If start time doesn't change, save the start time as new start time
            # Thus, we are able to check availability later
            cur.execute("SELECT start_time FROM appointments WHERE id = ?", (appointment_id,))
            start_time = cur.fetchone()[0]
            new_start_time = start_time
        if new_duration is not None:
            changes['duration'] = new_duration
        else:
            # If duration doesn't change, save the duration as new duration
            # Thus, we are able to check availability later
            cur.execute("SELECT duration FROM appointments WHERE id = ?", (appointment_id,))
            duration = cur.fetchone()[0]
            new_duration = duration

        # Calculate the end time. If start time or/and duration have changed, function will return new end time
        new_end_time = appointment_end_time_calculate(new_start_time, new_duration)

        # Check availability. If date or/and start time or/and duration have changes, we have to check availability again
        no_availability = check_availability(conn, new_date, new_start_time, new_end_time)

        # In order to end time be saved, we add it in Dictionary
        changes['end_time'] = new_end_time

        if no_availability:
            print("No availability, check an other date/time.")
            return 0
        else:
            # Create the query for execute, use dictionary keys and a loop for dynamically results
            set_fields = ', '.join([f"{key} = ?" for key in changes.keys()])
            set_criterion = f"UPDATE appointments SET {set_fields} WHERE id = ?"

            cur.execute(set_criterion, list(changes.values()) + [appointment_id])
            conn.commit()

    except sqlite3.Error as e:
        print("SQLite error:", e)
        # undo all changes
        try:
            conn.rollback()
        except:
            print("Failed to undo all changes")
        return None


def delete_appointment(conn, appointment_id):
    """Delete appointment"""
    try:
        cur = conn.cursor()
        cur.execute("""
            DELETE FROM appointments
            WHERE id = ?""", (appointment_id,))
        conn.commit()
    except sqlite3.Error as e:
        print("SQLite error:", e)
        # undo all changes
        try:
            conn.rollback()
        except:
            print("Failed to undo all changes")
        return None


def appointments_per_day(conn, date):
    """Get appointments for a specific day"""
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM appointments
            WHERE date = ? ORDER BY time(start_time)""", (date,))
        appointments = cur.fetchall()
        if appointments:
            return appointments
        else:
            return 0
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return None


def appointments_per_client(conn, client_id):
    """Get appointments for a specific client"""
    try:
        cur = conn.cursor()

        today = datetime.today().strftime('%Y-%m-%d')

        cur.execute("""
            SELECT * FROM appointments
            WHERE client_id = ?
            AND date(substr(date, 7, 4) || '-' || substr(date, 4, 2) || '-' || substr(date, 1, 2)) >= ?
            ORDER BY date(substr(date, 7, 4) || '-' || substr(date, 4, 2) || '-' || substr(date, 1, 2)) ASC, 
                     time(start_time) ASC
        """, (client_id, today))  # Pass both client_id and today
        appointments = cur.fetchall()
        if appointments:
            return appointments
        else:
            return 0
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return None


def search_appointment_by_id(conn, appointment_id):
    """Search appointment by id"""
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT * FROM appointments
            WHERE id = ?""", (appointment_id,))
        appointment = cur.fetchone()
        if appointment:
            return appointment
        else:
            return 0
    except sqlite3.Error as e:
        print("SQLite error:", e)
        return None
