# Step 1: Input Information
num_courses = int(input("How many courses do you have in the current semester? "))
course_grades = []
course_units = []

# Step 2: Collect Course Information
for i in range(num_courses):
    grade = input(f"Enter the grade for course {i + 1} (A, B, C, D, E, F): ").upper()
    units = int(input(f"Enter the course units for course {i + 1}: "))
    course_grades.append(grade)
    course_units.append(units)

# Step 3: Calculate Semester GPA
total_course_points = 0
total_course_units = 0

for i in range(num_courses):
    if course_grades[i] == 'A':
        gpa = 5.0
    elif course_grades[i] == 'B':
        gpa = 4.0
    elif course_grades[i] == 'C':
        gpa = 3.0
    elif course_grades[i] == 'D':
        gpa = 2.0
    elif course_grades[i] == 'E':
        gpa = 1.0
    else:
        gpa = 0.0

    total_course_points += gpa * course_units[i]
    total_course_units += course_units[i]

if total_course_units != 0:
    semester_gpa = total_course_points / total_course_units
    print(f"Semester GPA: {semester_gpa:.2f}")

# Step 4: Calculate CGPA
semester_GPAs = [semester_gpa]  # List to store semester GPAs
num_semesters = int(input("How many semesters do you want to include in the CGPA calculation? "))

for _ in range(num_semesters - 1):  # Loop for additional semesters
    # Repeat steps 2 and 3 to calculate semester GPA
    num_courses = int(input("How many courses do you have in this semester? "))
    course_grades = []
    course_units = []

    for i in range(num_courses):
        grade = input(f"Enter the grade for course {i + 1} (A, B, C, D, E, F): ").upper()
        units = int(input(f"Enter the course units for course {i + 1}: "))
        course_grades.append(grade)
        course_units.append(units)

    total_course_points = 0
    total_course_units = 0

    for i in range(num_courses):
        if course_grades[i] == 'A':
            gpa = 5.0
        elif course_grades[i] == 'B':
            gpa = 4.0
        elif course_grades[i] == 'C':
            gpa = 3.0
        elif course_grades[i] == 'D':
            gpa = 2.0
        elif course_grades[i] == 'E':
            gpa = 1.0
        else:
            gpa = 0.0

        total_course_points += gpa * course_units[i]
        total_course_units += course_units[i]

    if total_course_units != 0:
        semester_gpa = total_course_points / total_course_units
        semester_GPAs.append(semester_gpa)

# Calculate CGPA
total_course_points = sum(semester_GPAs) * sum(course_units)
total_course_units = sum(course_units)

if total_course_units != 0:
    cgpa = (total_course_points / total_course_units) / num_semesters
    print(f"CGPA: {cgpa:.2f}")

# End
