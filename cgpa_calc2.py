##These are the ways to import and use the GUI interface
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

def calculate_semester_gpa(course_grades, course_units):
    total_course_points = 0
    total_course_units = 0

    for i in range(len(course_grades)):
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
        return semester_gpa
    else:
        return 0

def collect_course_info():
    num_semesters = int(num_semesters_entry.get())

    total_semester_gpa = 0
    total_semester_count = 0

    for semester in range(num_semesters):
        num_courses = int(simpledialog.askstring(f"Semester {semester + 1}", "Enter the number of courses:"))

        course_grades = []
        course_units = []

        for i in range(num_courses):
            grade = simpledialog.askstring(f"Grade for course {i+1} - Semester {semester + 1}", "Enter the grade (A, B, C, D, E, F):")
            units = simpledialog.askinteger(f"Units for course {i+1} - Semester {semester + 1}", "Enter the course units:")

            course_grades.append(grade)
            course_units.append(units)

        semester_gpa = calculate_semester_gpa(course_grades, course_units)
        total_semester_gpa += semester_gpa
        total_semester_count += 1

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

root.mainloop()