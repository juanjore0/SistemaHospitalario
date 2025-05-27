import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget
from GUI.addHospital import HospitalTab
from GUI.addDoctor import DoctorTab

# Importa el controlador gráfico que conecta la lógica con la vista
from controller.hospital_gui_controller import HospitalGUIController
from controller.doctor_gui_controller import DoctorGUIController
from GUI.assignDoctorTab import AssignDoctorTab


class HospitalSystem(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Sistema Hospitalario')
        self.setGeometry(150, 150, 800, 600)
        

        main_layout = QVBoxLayout()

        self.tabs = QTabWidget()

        self.hospitals_tab = HospitalTab()
        self.doctors_tab = DoctorTab()

        self.assign_tab = AssignDoctorTab(None)
        
        print("Creando controlador HospitalGUIController")

        self.controller_hospital = HospitalGUIController(self.hospitals_tab)
        self.controller_doctor = DoctorGUIController(self.doctors_tab)
        self.controller_hospital.set_assign_tab(self.assign_tab)
        self.controller_doctor.set_assign_tab(self.assign_tab)

        
        self.assign_tab.controller = self.controller_hospital

        
        self.tabs.addTab(self.hospitals_tab, "Hospitales")
        self.tabs.addTab(self.doctors_tab, "Doctores")
        self.tabs.addTab(self.assign_tab, "Asignaciones")

        main_layout.addWidget(self.tabs)

        self.setLayout(main_layout)

if __name__ == '__main__':
    print("Iniciando app")
    app = QApplication(sys.argv)
    window = HospitalSystem()
    window.show()
    sys.exit(app.exec_())
