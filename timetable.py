class Timetable:
    def __init__(self, timetable_id=None, username=None, subject=None, day_of_week=None, location=None, description=None):
        self.timetable_id = timetable_id
        self.username = username
        self.subject = subject
        self.day_of_week = day_of_week
        self.location = location
        self.description = description

    def __str__(self):
        return (f"Timetable(id={self.timetable_id}, username={self.username}, subject={self.subject}, "
                f"day_of_week={self.day_of_week}, location={self.location}, description={self.description})")

