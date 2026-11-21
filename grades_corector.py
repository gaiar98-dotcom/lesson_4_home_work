import os
import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QLabel,
    QLineEdit,
    QFileDialog,
    QMessageBox,
    QHeaderView,
)
from PySide6.QtGui import QIntValidator


class GradesCorrectorWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grades Corrector")
        self.resize(700, 600)

        
        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.file_path = ""

        self.setup_ui()
        self.load_stylesheet()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # שורה עליונה: כפתור טעינת קובץ וכפתור About
        top_layout = QHBoxLayout()
        self.load_btn = QPushButton("Load File")
        self.load_btn.clicked.connect(self.load_file)

        self.about_btn = QPushButton("About")
        self.about_btn.setObjectName("aboutBtn")
        self.about_btn.clicked.connect(self.show_about)

        top_layout.addWidget(self.load_btn)
        top_layout.addStretch()
        top_layout.addWidget(self.about_btn)
        main_layout.addLayout(top_layout)

        # טבלה: 50 שורות ו-3 עמודות
        self.table = QTableWidget(50, 3)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Original Grades", "Corrected Grades"]
        )
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        main_layout.addWidget(self.table)

        # שורה תחתונה: הזנת נקודות בונוס + כפתור Update File
        bottom_layout = QHBoxLayout()
        bonus_label = QLabel("Bonus Points (press Enter):")

        self.bonus_input = QLineEdit()
        self.bonus_input.setPlaceholderText("Enter integer...")
        self.bonus_input.setValidator(QIntValidator(-100, 100))
        self.bonus_input.returnPressed.connect(self.apply_bonus)

        self.update_btn = QPushButton("Update File")
        self.update_btn.setObjectName("updateBtn")
        self.update_btn.clicked.connect(self.update_file)

        bottom_layout.addWidget(bonus_label)
        bottom_layout.addWidget(self.bonus_input)
        bottom_layout.addWidget(self.update_btn)
        main_layout.addLayout(bottom_layout)

    def load_stylesheet(self):
        qss_path = os.path.join(os.path.dirname(__file__), "style.qss")
        if os.path.exists(qss_path):
            with open(qss_path, "r", encoding="utf-8") as f:
                self.setStyleSheet(f.read())

    def update_table(self):
        """מעדכנת את הטבלה מתוך שלוש הרשימות של החלון"""
        self.table.setRowCount(len(self.student_ids))
        for row in range(len(self.student_ids)):
            self.table.setItem(row, 0, QTableWidgetItem(str(self.student_ids[row])))
            self.table.setItem(row, 1, QTableWidgetItem(str(self.original_grades[row])))
            self.table.setItem(row, 2, QTableWidgetItem(str(self.corrected_grades[row])))

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select Grades File", "", "CSV Files (*.csv);;All Files (*)"
        )
        if not file_path:
            return

        # TODO (שלב 3): כאן תכתבי את הקוד שטוען את הקובץ לרשימות ומעדכן את הטבלה

    def apply_bonus(self):
        # TODO (שלב 4): כאן תכתבי את הקוד שמחשב את הציונים המתוקנים ומעדכן את הטבלה
        pass

    def update_file(self):
        # TODO (שלב 5): כאן תכתבי את הקוד שדורס את הקובץ המקורי ופותח אותו באקסל
        pass

    def show_about(self):
        QMessageBox.about(
            self,
            "About Grades Corrector",
            "<h3>Grades Corrector</h3>"
            "<p>Created by Gaia</p>"
            "<p>GitHub Repository:<br>"
            "<a href='https://github.com/gaiar98-dotcom/lesson_4_home_work'>"
            "https://github.com/gaiar98-dotcom/lesson_4_home_work</a></p>",
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GradesCorrectorWindow()
    window.show()
    sys.exit(app.exec())