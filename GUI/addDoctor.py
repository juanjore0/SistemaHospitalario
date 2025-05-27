from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QTableWidget, QPushButton

class DoctorTab(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Barra de búsqueda
        self.search_doctor = QLineEdit()
        self.search_doctor.setPlaceholderText('Buscar doctor...')
        layout.addWidget(self.search_doctor)

        # Tabla de doctores
        self.doctor_table = QTableWidget()
        self.doctor_table.setColumnCount(3)
        self.doctor_table.setHorizontalHeaderLabels(['ID', 'Nombre', 'Especialidad'])
        layout.addWidget(self.doctor_table)

        # Botones
        button_layout = QHBoxLayout()
        self.add_doctor_button = QPushButton('Agregar médico')
        self.delete_doctor_button = QPushButton('Eliminar médico')
        button_layout.addWidget(self.add_doctor_button)
        button_layout.addWidget(self.delete_doctor_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)
