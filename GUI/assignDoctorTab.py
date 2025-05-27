from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton, QHBoxLayout, QMessageBox, QLineEdit

class AssignDoctorTab(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Nombre del hospital:"))
        self.hospital_input = QLineEdit()
        layout.addWidget(self.hospital_input)

        layout.addWidget(QLabel("DNI del doctor:"))
        self.doctor_input = QLineEdit()
        layout.addWidget(self.doctor_input)

        button_layout = QHBoxLayout()
        self.assign_button = QPushButton("Asignar doctor")
        self.delete_button = QPushButton("Eliminar doctor")
        button_layout.addWidget(self.assign_button)
        button_layout.addWidget(self.delete_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        self.assign_button.clicked.connect(self.assign_doctor_to_hospital)
        self.delete_button.clicked.connect(self.delete_doctor_from_hospital)

    def update_data(self, hospitals, doctors):
        # Este método puede quedar vacío o actualizar listas internas si usas combos
        # Si usas QLineEdit para inputs, no necesitas actualizar combos, pero podrías sugerir autocompletar aquí
        pass

    def assign_doctor_to_hospital(self):
        hospital_name = self.hospital_input.text().strip()
        doctor_dni = self.doctor_input.text().strip()

        if not hospital_name or not doctor_dni:
            QMessageBox.warning(self, "Error", "Debe ingresar ambos datos.")
            return

        if self.controller.assign_doctor(hospital_name, doctor_dni):
            QMessageBox.information(self, "Éxito", "Doctor asignado correctamente.")
        else:
            QMessageBox.warning(self, "Error", "No se pudo asignar el doctor.")

    def delete_doctor_from_hospital(self):
        hospital_name = self.hospital_input.text().strip()
        doctor_dni = self.doctor_input.text().strip()

        if not hospital_name or not doctor_dni:
            QMessageBox.warning(self, "Error", "Debe ingresar ambos datos.")
            return

        if self.controller.delete_doctor(hospital_name, doctor_dni):
            QMessageBox.information(self, "Éxito", "Doctor eliminado correctamente.")
        else:
            QMessageBox.warning(self, "Error", "No se pudo eliminar el doctor.")
