from timetable_dao import TimetableDAO
from timetable import Timetable
from my_array_list import MyArrayList
import mysql.connector # type: ignore

class TimetableService:
    def __init__(self):
        self.dao = TimetableDAO()

    

    def add_timetable_entry(self, timetable):
        try:
            self.dao.add_timetable(timetable, timetable.username)
            print("Timetable entry added successfully.")
        except mysql.connector.Error as e:
            print(f"Error: {e}")
    def viewTimeTable(self, username):
        try:
            self.dao.viewTime(username)
        except mysql.connector.Error as e:
            print(f"Error: {e}")
        

