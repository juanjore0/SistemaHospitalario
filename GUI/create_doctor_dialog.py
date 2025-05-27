from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton

class CreateHospitalDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Agregar nuevo doctor")
        self.setFixedSize(300, 120)

        layout = QVBoxLayout()

        label = QLabel("Ingrese el nombre del doctor:")
        layout.addWidget(label)

        label = QLabel("Ingrese el dni:")
        layout.addWidget(label)

        label = QLabel("Ingrese la especialidad:")
        layout.addWidget(label)


        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

        buttons_layout = QHBoxLayout()
        self.ok_button = QPushButton("Aceptar")
        self.cancel_button = QPushButton("Cancelar")

        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_name(self):
        return self.name_input.text().strip()
