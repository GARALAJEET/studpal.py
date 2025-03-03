from database_connection import DatabaseConnection
from timetable import Timetable
from my_array_list import MyArrayList
import mysql.connector # type: ignore

class TimetableDAO:
    TABLE_NAME = "college_timetable"

    def __init__(self):
        self.db = DatabaseConnection()
        self.connection = self.db.get_connection()

    def add_timetable(self, timetable, username):
        try:
            cursor = self.connection.cursor()
            query = f"INSERT INTO {self.TABLE_NAME} (day, time, subject, number_of_lectures, username) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (timetable.day_of_week, timetable.location, timetable.subject, timetable.description, username))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    def viewTime(self,username):
            cursor = self.connection.cursor()
            cursor.execute("SELECT  * FROM college_timetable WHERE  username=%s",(username,))
            result1=cursor.fetchall()
            Timetable = f"tiemtable.txt"
            with open(Timetable, "w",encoding="utf-8") as bill_file:
                bill_file.write("Timetable\n")
                bill_file.write("---------------------------------\n")
                for time in result1:
                     bill_file.write(f"Day:{time[1]}\n")
                     bill_file.write(f"Location: {time[2]}\n")
                     bill_file.write(f"SUbject: {time[3]}\n")
                     bill_file.write(f"number of lectures: {time[4]}\n")
                bill_file.write("---------------------------------\n")
              
            print(f"📄 print as {Timetable}")