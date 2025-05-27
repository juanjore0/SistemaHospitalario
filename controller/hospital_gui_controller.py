from PyQt5.QtWidgets import QTableWidgetItem
from controller import controller_hospital
from controller.storage import hospitals

class HospitalGUIController:
    def __init__(self, view):
        self.view = view

        # Conectar botones
        self.view.add_hospital_button.clicked.connect(self.add_hospital)
        self.view.delete_hospital_button.clicked.connect(self.delete_selected_hospital)

        self.refresh_table()

    def add_hospital(self):
        name = self.view.search_hospital.text().strip()
        if not name:
            return
        if controller_hospital.find_hospital(name):  # Evitar duplicados
            return
        controller_hospital.create_hospital(name)
        self.view.search_hospital.clear()
        self.refresh_table()

    def delete_selected_hospital(self):
        row = self.view.hospital_table.currentRow()
        if row < 0:
            return

        name = self.view.hospital_table.item(row, 0).text()
        controller_hospital.delete_hospital(name)
        self.refresh_table()

    def refresh_table(self):
        self.view.hospital_table.setRowCount(0)
        for i, hospital in enumerate(hospitals):
            self.view.hospital_table.insertRow(i)
            self.view.hospital_table.setItem(i, 0, QTableWidgetItem(hospital.hospital_name))
            self.view.hospital_table.setItem(i, 1, QTableWidgetItem(str(len(hospital.doctors))))
