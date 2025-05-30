from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidget, QPushButton, QHeaderView

class HospitalTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Barra de búsqueda
        self.search_hospital = QLineEdit()
        self.search_hospital.setPlaceholderText('Buscar hospital...')
        layout.addWidget(self.search_hospital)

        # Tabla de hospitales
        self.hospital_table = QTableWidget()
        self.hospital_table.setColumnCount(2)
        self.hospital_table.setHorizontalHeaderLabels(['Nombre', 'Doctores'])
        layout.addWidget(self.hospital_table)

        # Hacer que las columnas ocupen todo el ancho
        self.hospital_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.hospital_table.setStyleSheet("""
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
        self.add_hospital_button = QPushButton('Crear Hospital')
        self.delete_hospital_button = QPushButton('Eliminar Hospital')

        self.add_hospital_button.setStyleSheet("""
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

        self.delete_hospital_button.setStyleSheet("""
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
        
        button_layout.addWidget(self.add_hospital_button)
        button_layout.addWidget(self.delete_hospital_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)
