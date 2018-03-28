class Course(object):
    def __init__(self, department, number, name, credits):
        self.department = department
        self.number = number
        self.name = name
        self.credits = int(credits)
    def __str__(self):
        return self.name

class CourseOffering(object):
    def __init__(self, course, section_number, instructor, year, quarter):
        self.course = course
        self.section_number = section_number
        self.instructor = instructor
        self.year = year
        self.quarter = quarter
        self.registered_students = [] # a list to store the instance of Student registered into this course
        self.grades = {} # key is the username of student, value is the letter grade
    
    def register_students(self, *students):
        for stu_ins in students:
            if stu_ins in self.registered_students:
                print('{} already registered'.format(stu_ins.username))
            else:
                print('{} registered!'.format(stu_ins.username))
                self.registered_students.append(stu_ins)
            

    def get_students(self):
        return self.registered_students

    def submit_grade(self, student, letter_grade):
        if student in self.registered_students: # argument student is an instance
            self.grades[student.username] = letter_grade
        else: # argument student is a username
            self.grades[student] = letter_grade

    def get_grade(self, student):
        if type(student) is Student:
            return self.grades[student.username]
        else:
            return self.grades[student]


class Institution(object):
    def __init__(self, name, domain = None):
        self.name = name
        self.enrolled_students = [] # a list to store the instance of Student in this university
        self.employed_instructors = []
        self.course_catalog = [] # a list of instance of all available courses
        self.course_offering = []
        self.domain = domain

    def list_students(self):
        return self.enrolled_students # 返回什么？
    
    def enroll_student(self, student):
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)
            student.school = self
            print("{} enrolled".format(student.username))
        else:
            print("Already enrolled!")

    def list_instructors(self):
        return self.employed_instructors

    def hire_instructor(self, instructor):
        if instructor not in self.employed_instructors:
            self.employed_instructors.append(instructor)
            instructor.school = self
            print("{} hired".format(instructor.username))
        else:
            print("Already hired!")

    def list_course_catalog(self):
        return self.course_catalog # return a list of all courses available at the university

    def list_course_schedule(self, year, quarter, department = None ):
        courses = [] # a list of instances of CourseOffering
        for course in self.course_offering:
            if course.year == year and course.quarter == quarter:
                if department:
                    if course.course.department == department:
                        courses.append(course)
                else:
                    courses.append(course)
        return courses

    def add_course(self, course): # take an instance of course class
        if course not in self.course_catalog:
            self.course_catalog.append(course)
            print("add course successfully!")
        else:
            print('Already exist!')

    def add_course_offering(self, course_offering): # take an instance of CourseOffering class 
        if course_offering.course in self.course_catalog:
            self.course_offering.append(course_offering)
        else:
            print(f'Please add course {course_offering.course.name} first')






class Person(object):
    def __init__(self, last_name, first_name, date_of_birth):
        self.last_name = last_name
        self.first_name = first_name
        self.school = None # a reference to an instance of Institution class
        self.usename = None
        self.date_of_birth = date_of_birth
        self.affiliation = None
    
    @property
    def email(self):
        if not self.school:
            self.email = (str(self.username) +'@{}.edu'.format(self.domain))

class Instructor(Person):
    def __init__(self, last_name, first_name, username, date_of_birth):
        Person.__init__(self, last_name, first_name, date_of_birth)
        self.username = username
        self.affiliation = 'Instructor'

    def list_courses(self, year=None, quarter=None):
        course_list = []
        for offered_course in self.school.course_offering:
            if offered_course.instructor.username == self.username:
                if offered_course.year == year if year else True:
                    if offered_course.quarter == quarter if quarter else True:
                        course_list.append(offered_course)
        """
        This is my original version and Ziqing Zhang helped me make it concise:
        if year is None and quarter is None:
            for course in self.school.list_course.course_offering:
                if course.instructor == name:
                    course_list.append(course)
        elif quarter is None:
            for course in courses:
                if course.instructor == name and course.year == year:
                    course_list.append(course)
        elif year is None:
            for course in courses:
                if course.instructor == name and course.quarter == quarter:
                    course_list.append(course)
        else:
            for course in courses:
                if course.instructor == name and course.year == year and course.quarter == quarter:
                    course_list.append(course)
        """
                
        courses = sorted(course_list, key=lambda c: (c.year, c.quarter), reverse=True) 
        return courses

    def __str__(self):
        return self.username #print the username

class Student(Person):
    def __init__(self, last_name, first_name, date_of_birth, username):
        Person.__init__(self, last_name, date_of_birth, first_name)
        self.username = username
        self.affiliation = "student"

    def list_courses(self):
        course_all = []
        for course in self.school.course_offering:
            if self in course.registered_students:
                course_all.append(course)
        courses = sorted(course_all, key=lambda c: (c.year, c.quarter), reverse=True)
        return courses

    def credits(self):
        credits = 0
        for course_taken in self.list_courses():
            credits += course_taken.course.credits
        return credits

    def gpa(self):
        total_grade = 0
        Grade_Rank = {'A+': 4, 'A': 4, 'A-': 3.7, 'B+': 3.3, 'B': 3, 'B-': 2.7, 'C+': 2.3, 'C': 2, 'C-': 1.7, 'D+': 1.3, 'D': 1,'D-': 0.7, 'F': 0}
        for course in self.list_courses():
            try:
                grade = course.get_grade(self.username)
            except:
                continue
            credit = course.course.credits
            total_grade += Grade_Rank[grade] * credit
        credit =  self.credits()
        try: #there might be an exception
            return total_grade / credit
        except ZeroDivisionError:
            print("credit is 0")

    def __str__(self):
        return self.username


