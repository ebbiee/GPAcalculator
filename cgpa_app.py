import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QInputDialog

class GPA_Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GPA Calculator")
        self.setGeometry(100, 100, 400, 300)

        self.initUI()

    def initUI(self):
        self.num_courses_label = QLabel("Number of courses in the current semester:")
        self.num_courses_input = QLineEdit()
        
        self.collect_info_button = QPushButton("Collect Course Information")
        self.collect_info_button.clicked.connect(self.collect_course_info)

        self.result_label = QLabel("")

        vbox = QVBoxLayout()
        vbox.addWidget(self.num_courses_label)
        vbox.addWidget(self.num_courses_input)
        vbox.addWidget(self.collect_info_button)
        vbox.addWidget(self.result_label)

        self.setLayout(vbox)

    def collect_course_info(self):
        num_courses = int(self.num_courses_input.text())

        course_grades = []
        course_units = []

        for i in range(num_courses):
            grade, ok = QInputDialog.getText(self, f"Grade for course {i+1}", "Enter the grade (A, B, C, D, E, F):")
            if not ok:
                return
            units, ok = QInputDialog.getInt(self, f"Units for course {i+1}", "Enter the course units:")
            if not ok:
                return

            course_grades.append(grade)
            course_units.append(units)

        semester_gpa = self.calculate_semester_gpa(course_grades, course_units)
        self.result_label.setText(f"Semester GPA: {semester_gpa:.2f}")

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
