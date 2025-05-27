from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton, QMessageBox, QInputDialog
from PyQt5.QtCore import Qt
from controller import controller_doctor
from controller import controller_hospital
from controller.storage import doctors, hospitals

class AssignDoctorTab(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        layout = QVBoxLayout()

        self.title_label = QLabel("Asignar o Eliminar Doctor de un Hospital")
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.title_label)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)

        self.assign_button = QPushButton("Asignar doctor")
        self.delete_button = QPushButton("Eliminar doctor")

        # Estilo para agrandar botones
        btn_common_style = """
            font-size: 16px;
            padding: 12px 24px;
            min-width: 150px;
            min-height: 40px;
            color: white;
            border: none;
            border-radius: 6px;
        """

        # Asignar estilos específicos de color
        self.assign_button.setStyleSheet(btn_common_style + "background-color: #007bff;")  # azul
        self.delete_button.setStyleSheet(btn_common_style + "background-color: #dc3545;")  # rojo

        button_layout.addWidget(self.assign_button)
        button_layout.addWidget(self.delete_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        self.assign_button.clicked.connect(self.assign_doctor_to_hospital)
        self.delete_button.clicked.connect(self.delete_doctor_from_hospital)

    def update_data(self, hospitals, doctors):
        pass

    def assign_doctor_to_hospital(self):
        dni, ok = QInputDialog.getText(self, "Asignar Doctor", "Ingrese el DNI del doctor:")
        if not ok or not dni.strip():
            return
        hospital_name, ok = QInputDialog.getText(self, "Asignar Doctor", "Ingrese el nombre del hospital:")
        if not ok or not hospital_name.strip():
            return
        
        success = controller_doctor.add_doctor_to_hospital(hospital_name.strip(), dni.strip())
        if success:
            QMessageBox.information(self, "Éxito", f"Doctor con DNI {dni.strip()} asignado al hospital {hospital_name.strip()}.")
            if hasattr(self.controller, "refresh_table"):
                self.controller.refresh_table()
        else:
            QMessageBox.warning(self, "Error", "No se pudo asignar el doctor. Verifique que el hospital y doctor existan y que el doctor no esté ya asignado.")

    def delete_doctor_from_hospital(self):
        dni, ok = QInputDialog.getText(self, "Eliminar Doctor", "Ingrese el DNI del doctor:")
        if not ok or not dni.strip():
            return
        hospital_name, ok = QInputDialog.getText(self, "Eliminar Doctor", "Ingrese el nombre del hospital:")
        if not ok or not hospital_name.strip():
            return
        
        success = controller_doctor.delete_doctor_from_hospital(hospital_name.strip(), dni.strip())
        if success:
            QMessageBox.information(self, "Éxito", f"Doctor con DNI {dni.strip()} eliminado del hospital {hospital_name.strip()}.")
            if hasattr(self.controller, "refresh_table"):
                self.controller.refresh_table()
        else:
            QMessageBox.warning(self, "Error", "No se pudo eliminar el doctor. Verifique que el hospital y doctor existan y que el doctor esté asignado al hospital.")
