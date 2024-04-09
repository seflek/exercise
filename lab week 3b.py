#SERHAT SEFLEK

#fix the problems with each of these classes (1-3)
#(run them to see the traceback)

#1
class MyClass():
    def __init__(self, a, b):
        self.a = 10
        self.b = 20
        self.x = a + b
my_instance = MyClass(10,20)
my_instance.x

#2
class MyClass():
    def __init__(self):
        a = 10
        b = 20
        self.x = a + b
my_instance = MyClass()
my_instance.x

#3
class MyClass():
    def __init__(self, a, b):
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x

#4 Create a class to hold all of the courses a student at Harris is enrolled in.
#  - The instance should take two arguments when created; student name, 
#    and student year
#  - At startup, each instance should have an empty list as an attribute 
#    named "enrolled_courses"
#  - Create a method named "enroll" that takes some arguments that describe
#    a course, e.g. name, course number, days, times
#  - When called, make the "enroll" method add a course to the "enrolled_courses"
#    list
#  - Finally, think about what other methods you could add. One to drop a course?
#    One to display the enrolled courses?  Or could you modify "enroll" to make
#    sure times don't overlap, or there aren't too many courses in the list?
#    Work on these if you would like an extra challenge.


class Enrollment:
    def __init__(self, student_name, student_year):
        self.student_name = student_name
        self.student_year = student_year
        self.enrolled_course = []
        
    def enroll(self, course_name, course_number, day, time):
        course = {"name": course_name,
                  "number" : course_number,
                  "day": day,
                  "time": time}
        self.enrolled_course.append(course)

    def drop(self, course_name, course_number, day, time):
        course = {"name": course_name,
                  "number" : course_number,
                  "day": day,
                  "time": time}
        self.enrolled_course.remove(course)

student = Enrollment("Serhat Seflek", "First Year")

student.enroll("Microeconomics", "32100", "MondayFriday", "11:00")
student.enroll("AP", "3300", "TuesdayThursday", "12:00")

print(student.enrolled_course)

student.drop("Microeconomics", "32100", "MondayFriday", "11:00")

print(student.enrolled_course)
    