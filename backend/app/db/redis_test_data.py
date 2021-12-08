from app.db.redis_models import Semester
from app.db.redis_models import SemesterCourse
from app.db.redis_models import SemesterCourseAttendance
from app.db.redis_models import Student
from app.db.redis_models import StudentCourse


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

test_semesters = [
    Semester(
        id=1,
        name="Class 1",
        courses=[
            SemesterCourse(
                id=1,
                name="Math",
                course_attendance=[
                    SemesterCourseAttendance(name="John", attendance_percentage=90),
                    SemesterCourseAttendance(name="Jane", attendance_percentage=95),
                ],
            ),
            SemesterCourse(
                id=2,
                name="English",
                course_attendance=[
                    SemesterCourseAttendance(name="John", attendance_percentage=80),
                    SemesterCourseAttendance(name="Jane", attendance_percentage=85),
                ],
            ),
            SemesterCourse(
                id=3,
                name="Physics",
                course_attendance=[
                    SemesterCourseAttendance(name="John", attendance_percentage=70),
                    SemesterCourseAttendance(name="Jane", attendance_percentage=75),
                ],
            ),
        ],
    ),
    Semester(
        id=2,
        name="Class 2",
        courses=[
            SemesterCourse(
                id=1,
                name="Math",
                course_attendance=[
                    SemesterCourseAttendance(name="Bob", attendance_percentage=40),
                    SemesterCourseAttendance(name="Alice", attendance_percentage=10),
                ],
            ),
            SemesterCourse(
                id=2,
                name="English",
                course_attendance=[
                    SemesterCourseAttendance(name="Bob", attendance_percentage=50),
                    SemesterCourseAttendance(name="Alice", attendance_percentage=20),
                ],
            ),
            SemesterCourse(
                id=3,
                name="Physics",
                course_attendance=[
                    SemesterCourseAttendance(name="Bob", attendance_percentage=60),
                    SemesterCourseAttendance(name="Alice", attendance_percentage=30),
                ],
            ),
        ],
    ),
]
