#Command Line Interface version of CGPA Calculator App

#Ask for the User's Course Information
num_courses = input("How many courses are you offering? ")

course_grades = []
course_units = []

def course_info():
    grade = input("Input your grade for the course (A, B, C, D, E, F): ")
    course_grades.append(grade)
    units = input("Input the number of unis for the course: ")
    course_units.append(units)

    re_enter = input("Do you want to input another course? \n")
    if re_enter.lower() == "yes":
        course_info()
    else:
        print("All courses recorded successfully! ")

#Caculate the Semester GPA
def calc_semester_gpa():
    total_course_points = 0
    total_course_units = 0

    for grades in course_grades:
        if grades.upper() == "A":
            GPA = 5
        elif grades.upper() == "B":
            GPA = 4
        elif grades.upper() == "C":
            GPA = 3
        elif grades.upper() == "D":
            GPA = 2
        elif grades.upper() == "E":
            GPA = 1
        else:
            GPA = 0

        for unit in course_units:
            total_course_points = GPA * int(unit)
            total_course_units = total_course_units + int(unit)

    if total_course_units > 0:
        semester_gpa = total_course_points / total_course_units
        print(f"Your Semester GPA is {semester_gpa}")


#Calculate CGPA
def calc_cgpa ():
    semester_GPAs = []
    semester_GPAs.append(semester_gpa)
    
    num_semesters = input("How many semesters do you want to include in the CGPA calculation?: ")
    




course_info()
calc_semester_gpa()