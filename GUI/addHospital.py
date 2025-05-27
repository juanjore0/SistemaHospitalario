from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidget, QPushButton

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

        # Botones
        button_layout = QHBoxLayout()
        self.add_hospital_button = QPushButton('Crear Hospital')
        self.delete_hospital_button = QPushButton('Eliminar Hospital')
        button_layout.addWidget(self.add_hospital_button)
        button_layout.addWidget(self.delete_hospital_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)
