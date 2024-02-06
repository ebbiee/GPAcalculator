# import the tkinter module and alias it as tk
import tkinter as tk
# import the messagebox module from tkinter
from tkinter import messagebox
# import the simpledialog module from tkinter
from tkinter import simpledialog

# Function to calculate semester GPA based on course grades and units
def calculate_semester_gpa(course_grades, course_units):
    total_course_points = 0
    total_course_units = 0

    # Loop through each course grade and unit
    for i in range(len(course_grades)):
        # Assign GPA value based on the grade
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

        # Calculate total course points and units
        total_course_points += gpa * course_units[i]
        total_course_units += course_units[i]

    # Calculate semester GPA
    if total_course_units != 0:
        semester_gpa = total_course_points / total_course_units
        return semester_gpa
    else:
        return 0

# Function to collect course information from the user
def collect_course_info():
    # Get the number of semesters from the entry field
    num_semesters = int(num_semesters_entry.get())

    total_semester_gpa = 0
    total_semester_count = 0

    # Loop through each semester
    for semester in range(num_semesters):
        # Prompt the user to enter the number of courses for the semester
        num_courses = int(simpledialog.askstring(f"Semester {semester + 1}", "Enter the number of courses:"))

        course_grades = []
        course_units = []

        # Loop through each course in the semester
        for i in range(num_courses):
            # Prompt the user to enter the grade and units for each course
            grade = simpledialog.askstring(f"Grade for course {i+1} - Semester {semester + 1}", "Enter the grade (A, B, C, D, E, F):")
            units = simpledialog.askinteger(f"Units for course {i+1} - Semester {semester + 1}", "Enter the course units:")

            course_grades.append(grade)
            course_units.append(units)

        # Calculate semester GPA and accumulate total GPA and count
        semester_gpa = calculate_semester_gpa(course_grades, course_units)
        total_semester_gpa += semester_gpa
        total_semester_count += 1

    # Calculate average GPA across all semesters and display the result
    if total_semester_count != 0:
        average_gpa = total_semester_gpa / total_semester_count
        result_label.config(text=f"Average GPA: {average_gpa:.2f}")
    else:
        result_label.config(text="No courses entered.")

root = tk.Tk()
root.title("GPA Calculator")

num_semesters_label = tk.Label(root, text="Number of Semesters:")
num_semesters_entry = tk.Entry(root)
collect_info_button = tk.Button(root, text="Collect Course Info", command=collect_course_info)
result_label = tk.Label(root, text="")

num_semesters_label.pack()
num_semesters_entry.pack()
collect_info_button.pack()
result_label.pack()

# Start the tkinter event loop
root.mainloop()
