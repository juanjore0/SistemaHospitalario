from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidget, QPushButton

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
        
        # Botones
        button_layout = QHBoxLayout()
        self.add_doctor_button = QPushButton('Agregar médico')
        self.delete_doctor_button = QPushButton('Eliminar médico')

        self.add_doctor_button.setStyleSheet("""
            QPushButton {
                background-color: #007acc;
                color: black;
                border-radius: 6px;
                padding: 6px 10px;
            }
            QPushButton:hover {
                background-color: #005f99;
            }
        """)

        self.delete_doctor_button.setStyleSheet("""
            QPushButton {
                background-color: #a6a6a6;
                color: black;
                border-radius: 6px;
                padding: 6px 10px;
            }
            QPushButton:hover {
                background-color: #808080;
            }
        """)

        button_layout.addWidget(self.add_doctor_button)
        button_layout.addWidget(self.delete_doctor_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)
