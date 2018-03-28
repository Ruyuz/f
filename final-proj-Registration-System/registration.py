import pandas
import pickle as pk
from pathlib import Path
from registrar import *

institution_name = input('Welcome to the Registration System\nPlease enter the name of your institution: ')
institution = Institution(institution_name) # create an instance of Institution
path = Path('./data/{}.pkl'.format(institution_name))
if path.exists():
    with open(path, 'rb') as source:
        institution = pk.load(source) # referenced from Zhenghong Zhang
    print('The school already exists and is retrieved.')

Course_offering_lists = {}

while True: 
    try: # the program should run on a loop util the user elects to exit
        print('Please select an option from the following:')
        print('1   Create a course')
        print('2   Schedule a course offering ')
        print('3   List course catalog')
        print('4   List course schedule ')
        print('5   Hire an instructor')
        print('6   Assign a new instructor to a course ')
        print('7   Enroll a student ')
        print('8   Register a student for a course ')
        print('9   List enrolled students ')
        print('10  List students registered for a course')
        print('11  Submit student grade')
        print('12  Get student records')
        print('13  Exit')

        option = input('Please enter your choice: ')

        if option == '1':
            print('Create a course: \n eg: MPCS, 51042, Python Programming, 100')
            input_args = []
            course_args = ['department', 'number', 'name', 'credits'] #List Loop idea learned from Rex Zhou
            for args in course_args:
                input_args.append(input('Please input the {} argument of Course class: '.format(args)))
            course = Course(*input_args) # use a list to parse ragument to initial a course class
            print('course created successfully!')
            institution.add_course(course)
            print('course added successfully!')


        elif option == '2':
            print('Schedule a course offering : \n eg: MPCS, 51042, 1, Nicholas Flees, 2017, FALL')
            input_args = []
            course_offer_args = ['department', 'course number', 'section', 'instructor', 'year', 'quarter']
            for args in course_offer_args:
                input_args.append(input('Please input the {} argument of course offering: '.format(args)))
            for course in institution.course_catalog:
                if course.department == input_args[0] and course.number == input_args[1]:
                    cr = course
                    course_offering = CourseOffering(cr, *input_args[2:])
                    print('course_offering created successfully!')
                    institution.add_course_offering(course_offering)
                    Course_offering_lists[(course_offering.course.department, course_offering.course.number, course_offering.section_number, course_offering.year, course_offering.year)] = course_offering
                    print('course_offering added successfully!')


        elif option == '3':
            student = {'department': [i.department for i in institution.list_course_catalog()], 'number': [i.number for i in institution.list_course_catalog()],
                        'credits': [i.credits for i in institution.list_course_catalog()]}

            course_catalog = pandas.DataFrame(student)
            course_catalog.index = [i.name for i in institution.list_course_catalog()]
            print(course_catalog) # can use this format?


        elif option == '4':
            print('List course schedule \nPlease input year, quarter, and department(if necessary)')
            year = input('Please input year (eg: 2017, 2018): ')
            quarter = input('Please input quarter (eg: FALL, WINTER, SPRING, or SUMMER): ')
            department = input('Please input department: ') # How to handle when department is omitted
            courses = []
            for i in institution.course_offering:
                if year == i.year:
                    if quarter == i.quarter:
                        if i.course.department == department:
                            courses.append(i)

            data = pandas.DataFrame({'name': [x.course.name for x in courses], 'instructor':[x.instructor for x in courses], 'year':[x.year for x in courses ], 'quarter':[x.quarter for x in courses]})
            print(data)

        elif option == '5':
            print('Hire an instructor: \nPlease input last_name, first_name, username:')
            instructor_args = ['last name','first name', 'date_of_birth', 'username']
            input_args = []
            for args in instructor_args:
                input_args.append(input('Please input the {} argument of instructor: '.format(args)))
            instructor = Instructor(*input_args)
            print('instructor created successfully!')
            institution.hire_instructor(instructor)
            print('instructor hired successfully!')

        elif option == '6':
            print('Assign instructor to the given course:\nPlease enter the following information: \neg: MPCS, 55001, Section 1, 2017, Autumn, nickflees')
            assign_args = ['Username', 'Department' , 'Number', 'Section_number', 'Year', 'Quarter']
            input_args = []
            for args in assign_args:
                input_args.append(input('Please input {}: '.format(args)))
            name = input_args[0]
            for i in institution.course_offering:
                if input_args[1] == i.course.department and input_args[2] == i.course.number and input_args[3] == i.section_number and input_args[4] == i.year and input_args[5] == i.quarter:
                     for j in institution.employed_instructors:
                        if j.username == name:
                            i.instructor = j
    
        elif option == '7':
            print('Enrolling a new student:\nPlease enter the following information:\n eg: Zhou, Ruyu, 1994/01/01, ruyuz')
            assign_args = ['last_name', 'first_name', 'date of birth', 'username']
            input_args = []
            for i in assign_args:
                info = input(i + ": ")
                input_args.append(info)
            institution.enroll_student(Student(*input_args))

       
        elif option == '8':
            print('Register student to a course:\nPlease enter the following information: eg: ruyuz, MPCS, 51042, 1, 2017, Autumn')
            regist_args = ['Username', 'Department',  'Number', 'Section_number', 'Year', 'Quarter']
            input_args = []
            for args in regist_args:
                info = input(args + ": ")
                input_args.append(info)
            input_username = input_args[0]
            for i in institution.course_offering:
                if input_args[1] == i.course.department and input_args[2] == i.course.number and input_args[3] == i.section_number and input_args[4] == i.year and input_args[5] == i.quarter:
                    for stu in institution.enrolled_students:
                        if stu.username == input_username:
                            i.register_students(stu)
    
        elif option == '9':
            print('List enrolled students ')
            students = institution.list_students()
            student = { 'email': [i.email for i in institution.enrolled_students],
                        'username': [i.username for i in institution.enrolled_students], 'date of birth': [i.date_of_birth for i in institution.enrolled_students]}
            student = pandas.DataFrame(student)
            student.index = [i.first_name + ' ' + i.last_name for i in institution.enrolled_students]
            print(student)

      
        elif option == '10':
            print('Listing registered students for a course: \nPlease provide the following infomation:\neg: MPCS, 51042, 1, 2017, Fall')
            course_args = ['Department',  'Number', 'Section_number', 'Year', 'Quarter']
            input_args = []
            for args in course_args:
                info = input(args + ": ")
                input_args.append(info)
            for course_offering in institution.course_offering:
                if input_args[0] == i.course.department and input_args[1] == i.course.number and input_args[2] == i.section_number and input_args[3] == i.year and input_args[4] == i.quarter:
                    students = course_offering.registered_students
                    print("students in {} course are:".format(course_offering.course.name))
                    print(pandas.Series(students))

       
        elif option == '11':
            print('Submitting grade for a student in course.\neg: ruyuz, MPCS, 51042, Section 1, 2017, Fall, A')
            grade_args = ['Username', 'Department',  'Number', 'Section_number', 'Year', 'Quarter', 'Grade']
            input_args = []
            for i in grade_args:
                info = input(i + ": ")
                input_args.append(info)
            stu_name = input_args[0]
            for i in institution.course_offering:
                if input_args[1] == i.course.department and input_args[2] == i.course.number and input_args[3] == i.section_number and input_args[4] == i.year and input_args[5] == i.quarter:
                    for j in institution.enrolled_students:
                        if j.username == stu_name:
                            i.submit_grade(j, grade_args[-1])
                            break
    
    
        elif option == '12':
            print('Showing student\'s records. Input username, eg: ruyuz:')
            stu_name = input('Username:')
            for i in institution.enrolled_students:
                if i.username == stu_name:
                    print([j.course.name for j in i.list_courses()])
                    print('GPA: ' + str(i.gpa()))
                    print('Credits: ' + str(i.credits()))
        else:
            break

    except KeyboardInterrupt:
        continue

with open(f'./data/{institution.name}.pkl', 'wb') as output:
    pk.dump(institution,output,pk.HIGHEST_PROTOCOL)
del institution
print('Program exited.')








