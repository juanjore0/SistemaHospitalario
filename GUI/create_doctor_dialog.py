from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton

class CreateDoctorDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Agregar nuevo doctor")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()

        # Campo para el nombre
        name_label = QLabel("Nombre del doctor:")
        self.name_input = QLineEdit()
        layout.addWidget(name_label)
        layout.addWidget(self.name_input)

        # Campo para el DNI
        dni_label = QLabel("DNI:")
        self.dni_input = QLineEdit()
        layout.addWidget(dni_label)
        layout.addWidget(self.dni_input)

        # Campo para la especialidad
        speciality_label = QLabel("Especialidad:")
        self.speciality_input = QLineEdit()
        layout.addWidget(speciality_label)
        layout.addWidget(self.speciality_input)

        # Botones
        buttons_layout = QHBoxLayout()
        self.ok_button = QPushButton("Aceptar")
        self.cancel_button = QPushButton("Cancelar")
        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_doctor_info(self):
        return {
            "doctor_name": self.name_input.text().strip(),
            "speciality": self.speciality_input.text().strip(),
            "dni": self.dni_input.text().strip()
        }
