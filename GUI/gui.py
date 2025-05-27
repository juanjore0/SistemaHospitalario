import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget
from addHospital import HospitalTab
from addDoctor import DoctorTab

class HospitalSystem(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Sistema Hospitalario')
        self.setGeometry(150, 150, 800, 600)

        main_layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.hospitals_tab = HospitalTab()
        self.doctors_tab = DoctorTab()

        self.tabs.addTab(self.hospitals_tab, "Hospitales")
        self.tabs.addTab(self.doctors_tab, "Doctores")

        main_layout.addWidget(self.tabs)

        self.setLayout(main_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HospitalSystem()
    window.show()
    sys.exit(app.exec_())
