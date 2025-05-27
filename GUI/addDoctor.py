from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidget, QPushButton, QHeaderView


class DoctorTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Barra de búsqueda (opcional, puedes conectar esto después)
        self.search_doctor = QLineEdit()
        self.search_doctor.setPlaceholderText('Buscar doctor...')
        layout.addWidget(self.search_doctor)

        # Tabla de doctores con 4 columnas: Hospital, Nombre, DNI, Especialidad
        self.doctor_table = QTableWidget()
        self.doctor_table.setColumnCount(4)
        self.doctor_table.setHorizontalHeaderLabels(['Hospital', 'Nombre', 'DNI', 'Especialidad'])
        layout.addWidget(self.doctor_table)

        self.doctor_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.doctor_table.setStyleSheet("""
        QTableWidget {
        background-color: #ffffff;
        border: 1px solid #ccc;
        font-family: Segoe UI;
        font-size: 13px;
    }
        QHeaderView::section {
        background-color: #007acc;
        color: white;
        font-weight: bold;
        padding: 4px;
        border: 1px solid #ddd;
    }
        QTableWidget::item {
        padding: 4px;
        border: none;
    }
        QTableWidget::item:selected {
        background-color: #cce5ff;
    }
    """)

        # Botones con ancho completo
        button_layout = QHBoxLayout()
        self.add_doctor_button = QPushButton('Crear doctor')
        self.delete_doctor_button = QPushButton('Eliminar doctor')

        # Hacer que los botones se expandan para llenar toda la barra
        self.add_doctor_button.setSizePolicy(self.add_doctor_button.sizePolicy().Expanding, 
                                           self.add_doctor_button.sizePolicy().Fixed)
        self.delete_doctor_button.setSizePolicy(self.delete_doctor_button.sizePolicy().Expanding, 
                                              self.delete_doctor_button.sizePolicy().Fixed)

        self.add_doctor_button.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: white;
                border-radius: 6px;
                padding: 8px 12px;
                font-weight: bold;
                font-size: 13px;
                min-height: 30px;
            }
            QPushButton:hover {
                background-color: #005f99;
            }
            QPushButton:pressed {
                background-color: #004080;
            }
        """)

        self.delete_doctor_button.setStyleSheet("""
            QPushButton {
                background-color: #dc3545;
                color: white;
                border-radius: 6px;
                padding: 8px 12px;
                font-weight: bold;
                font-size: 13px;
                min-height: 30px;
            }
            QPushButton:hover {
                background-color: #c82333;
            }
            QPushButton:pressed {
                background-color: #bd2130;
            }
        """)

        button_layout.addWidget(self.add_doctor_button)
        button_layout.addWidget(self.delete_doctor_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)