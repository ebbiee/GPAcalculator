import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QInputDialog

class GPA_Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GPA Calculator")
        self.setGeometry(100, 100, 400, 300)

        self.initUI()

    def initUI(self):
        self.num_semesters_label = QLabel("Number of semesters to include in CGPA calculation:")
        self.num_semesters_input = QLineEdit()
        
        self.collect_info_button = QPushButton("Collect Course Information")
        self.collect_info_button.clicked.connect(self.collect_course_info)

        self.result_label = QLabel("")

        vbox = QVBoxLayout()
        vbox.addWidget(self.num_semesters_label)
        vbox.addWidget(self.num_semesters_input)
        vbox.addWidget(self.collect_info_button)
        vbox.addWidget(self.result_label)

        self.setLayout(vbox)

    def collect_course_info(self):
        num_semesters, ok = QInputDialog.getInt(self, "Number of Semesters", "How many semesters do you want to include in the CGPA calculation?")
        if not ok:
            return

        total_semester_gpa = 0
        total_semester_count = 0

        for semester in range(num_semesters):
            num_courses, ok = QInputDialog.getInt(self, f"Number of Courses - Semester {semester + 1}", f"Enter the number of courses in Semester {semester + 1}:")
            if not ok:
                continue

            semester_gpa, course_count = self.calculate_semester_info(num_courses, semester + 1)
            total_semester_gpa += semester_gpa
            total_semester_count += course_count

        if total_semester_count != 0:
            average_gpa = total_semester_gpa / total_semester_count
            self.result_label.setText(f"Average GPA: {average_gpa:.2f}")
        else:
            self.result_label.setText("No courses entered.")

    def calculate_semester_info(self, num_courses, semester):
        course_grades = []
        course_units = []

        for i in range(num_courses):
            grade, ok = QInputDialog.getText(self, f"Grade for course {i+1} - Semester {semester}", "Enter the grade (A, B, C, D, E, F):")
            if not ok:
                return 0, 0
            units, ok = QInputDialog.getInt(self, f"Units for course {i+1} - Semester {semester}", "Enter the course units:")
            if not ok:
                return 0, 0

            course_grades.append(grade)
            course_units.append(units)

        semester_gpa = self.calculate_semester_gpa(course_grades, course_units)
        return semester_gpa, num_courses

    def calculate_semester_gpa(self, course_grades, course_units):
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GPA_Calculator()
    window.show()
    sys.exit(app.exec_())
