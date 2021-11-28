from app.db.redis import Class
from app.db.redis import ClassCourse
from app.db.redis import ClassCourseAttendance
from app.db.redis import Student
from app.db.redis import StudentCourse


test_students = [
    Student(
        id=1,
        name="John",
        courses=[
            StudentCourse(id=1, name="Math", attendance_percentage=90),
            StudentCourse(id=2, name="English", attendance_percentage=80),
            StudentCourse(id=3, name="Physics", attendance_percentage=70),
        ],
    ),
    Student(
        id=2,
        name="Jane",
        courses=[
            StudentCourse(id=1, name="Math", attendance_percentage=95),
            StudentCourse(id=2, name="English", attendance_percentage=85),
            StudentCourse(id=3, name="Physics", attendance_percentage=75),
        ],
    ),
    Student(
        id=3,
        name="Bob",
        courses=[
            StudentCourse(id=1, name="Math", attendance_percentage=40),
            StudentCourse(id=2, name="English", attendance_percentage=50),
            StudentCourse(id=3, name="Physics", attendance_percentage=60),
        ],
    ),
    Student(
        id=4,
        name="Alice",
        courses=[
            StudentCourse(id=1, name="Math", attendance_percentage=10),
            StudentCourse(id=2, name="English", attendance_percentage=20),
            StudentCourse(id=3, name="Physics", attendance_percentage=30),
        ],
    ),
]

test_classes = [
    Class(
        id=1,
        name="Class 1",
        courses=[
            ClassCourse(
                id=1, name="Math", course_attendance=[
                    ClassCourseAttendance(name="John", attendance_percentage=90),
                    ClassCourseAttendance(name="Jane", attendance_percentage=95),
                ],
            ),
            ClassCourse(
                id=2, name="English", course_attendance=[
                    ClassCourseAttendance(name="John", attendance_percentage=80),
                    ClassCourseAttendance(name="Jane", attendance_percentage=85),
                ],
            ),
            ClassCourse(
                id=3, name="Physics", course_attendance=[
                    ClassCourseAttendance(name="John", attendance_percentage=70),
                    ClassCourseAttendance(name="Jane", attendance_percentage=75),
                ],
            ),
        ],
    ),
    Class(
        id=2,
        name="Class 2",
        courses=[
            ClassCourse(
                id=1, name="Math", course_attendance=[
                    ClassCourseAttendance(name="Bob", attendance_percentage=40),
                    ClassCourseAttendance(name="Alice", attendance_percentage=10),
                ],
            ),
            ClassCourse(
                id=2, name="English", course_attendance=[
                    ClassCourseAttendance(name="Bob", attendance_percentage=50),
                    ClassCourseAttendance(name="Alice", attendance_percentage=20),
                ],
            ),
            ClassCourse(
                id=3, name="Physics", course_attendance=[
                    ClassCourseAttendance(name="Bob", attendance_percentage=60),
                    ClassCourseAttendance(name="Alice", attendance_percentage=30),
                ],
            ),
        ],
    ),
]
