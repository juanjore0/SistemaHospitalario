from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QMessageBox

class AssignDoctorTab(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller

        layout = QVBoxLayout()

        layout.addWidget(QLabel("Seleccione un hospital:"))
        self.hospital_combo = QComboBox()
        layout.addWidget(self.hospital_combo)

        layout.addWidget(QLabel("Seleccione un doctor:"))
        self.doctor_combo = QComboBox()
        layout.addWidget(self.doctor_combo)

        button_layout = QHBoxLayout()
        self.assign_button = QPushButton("Asignar doctor")
        self.delete_button = QPushButton("Eliminar doctor")
        button_layout.addWidget(self.assign_button)
        button_layout.addWidget(self.delete_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        # Conexiones
        self.assign_button.clicked.connect(self.assign_doctor_to_hospital)
        self.delete_button.clicked.connect(self.delete_doctor_from_hospital)

    def update_data(self, hospitals, doctors):
        self.hospital_combo.clear()
        self.hospital_combo.addItems(hospitals)

        self.doctor_combo.clear()
        self.doctor_combo.addItems(doctors)

    def assign_doctor_to_hospital(self):
        hospital_name = self.hospital_combo.currentText()
        doctor_dni = self.doctor_combo.currentText()

        if self.controller.assign_doctor(hospital_name, doctor_dni):
            QMessageBox.information(self, "Éxito", "Doctor asignado correctamente.")
        else:
            QMessageBox.warning(self, "Error", "No se pudo asignar el doctor.")

    def delete_doctor_from_hospital(self):
        hospital_name = self.hospital_combo.currentText()
        doctor_dni = self.doctor_combo.currentText()

        if self.controller.delete_doctor(hospital_name, doctor_dni):
            QMessageBox.information(self, "Éxito", "Doctor eliminado correctamente.")
        else:
            QMessageBox.warning(self, "Error", "No se pudo eliminar el doctor.")
