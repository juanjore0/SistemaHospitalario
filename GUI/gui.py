import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget
from GUI.addHospital import HospitalTab

from GUI.addDoctor import DoctorTab

# Importa el controlador gráfico que conecta la lógica con la vista
from controller.hospital_gui_controller import HospitalGUIController

class HospitalSystem(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Sistema Hospitalario')
        self.setGeometry(150, 150, 800, 600)

        main_layout = QVBoxLayout()

        self.tabs = QTabWidget()
        self.hospitals_tab = HospitalTab()
        self.doctors_tab = DoctorTab()

        self.controller_hospital = HospitalGUIController(self.hospitals_tab)

        self.tabs.addTab(self.hospitals_tab, "Hospitales")
        self.tabs.addTab(self.doctors_tab, "Doctores")

        main_layout.addWidget(self.tabs)

        self.setLayout(main_layout)

if __name__ == '__main__':
    print("Iniciando app")
    app = QApplication(sys.argv)
    window = HospitalSystem()
    window.show()
    sys.exit(app.exec_())
