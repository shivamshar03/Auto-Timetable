# Main program

from timetable import generate_timetable, save_timetable
from models import Course, Faculty, Room

def main():
    courses = session.query(Course).all()
    faculties = session.query(Faculty).all()
    rooms = session.query(Room).all()

    timetable = generate_timetable(courses, faculties, rooms)
    save_timetable(timetable)

    print("Time table generated and saved successfully!")

if __name__ == "__main__":
    main()