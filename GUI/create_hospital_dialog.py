from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QHBoxLayout, QPushButton

class CreateHospitalDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Crear nuevo hospital")
        self.setFixedSize(300, 120)

        self.setStyleSheet("""
            background-color: #e6f2ff;
            font-family: Verdana;
        """)

        layout = QVBoxLayout()

        label = QLabel("Ingrese el nombre del hospital:")
        label.setStyleSheet("color: #004080; font-weight: bold;")
        layout.addWidget(label)

        self.name_input = QLineEdit()
        self.name_input.setStyleSheet("padding: 5px; border: 1px solid #007acc; border-radius: 4px;")
        layout.addWidget(self.name_input)

        buttons_layout = QHBoxLayout()
        self.ok_button = QPushButton("Aceptar")
        self.cancel_button = QPushButton("Cancelar")

        
        self.ok_button.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border-radius: 6px;
                padding: 6px 10px;
            }
            QPushButton:hover {
                background-color: #005f99;
            }
        """)

        self.cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #a6a6a6;
                color: white;
                border-radius: 6px;
                padding: 6px 10px;
            }
            QPushButton:hover {
                background-color: #808080;
            }
        """)

        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

    def get_name(self):
        return self.name_input.text().strip()
