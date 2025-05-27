from PyQt5.QtWidgets import QMessageBox, QDialog
from GUI.create_hospital_dialog import CreateHospitalDialog  # Ajusta el import según tu estructura
from . import controller_hospital
from controller.storage import hospitals
from PyQt5.QtWidgets import QTableWidgetItem
from controller.controller_hospital import find_hospital
from controller.controller_doctor import search_by_dni

class HospitalGUIController:
    def __init__(self, view, assign_tab=None):
        self.view = view
        self.assign_tab = assign_tab  # Inicializa assign_tab como None
        self.view.add_hospital_button.clicked.connect(self.open_create_hospital_dialog)
        self.view.delete_hospital_button.clicked.connect(self.delete_selected_hospital)
        self.refresh_table()

    def open_create_hospital_dialog(self):
        dialog = CreateHospitalDialog(self.view)
        if dialog.exec_() == QDialog.Accepted:
            name = dialog.get_name()
            if not name:
                QMessageBox.warning(self.view, "Error", "El nombre no puede estar vacío.")
                return
            if controller_hospital.find_hospital(name):
                QMessageBox.warning(self.view, "Error", "El hospital ya existe.")
                return
            controller_hospital.create_hospital(name)
            self.refresh_table()
            self.update_assign_tab()

    def delete_selected_hospital(self):
        row = self.view.hospital_table.currentRow()
        if row < 0:
            return

        name = self.view.hospital_table.item(row, 0).text()
        controller_hospital.delete_hospital(name)
        self.refresh_table()
        self.update_assign_tab()

    def refresh_table(self):
        self.view.hospital_table.setRowCount(0)
        for i, hospital in enumerate(hospitals):
            self.view.hospital_table.insertRow(i)
            self.view.hospital_table.setItem(i, 0, QTableWidgetItem(hospital.hospital_name))
            self.view.hospital_table.setItem(i, 1, QTableWidgetItem(str(len(hospital.doctors))))
        self.view.hospital_table.resizeColumnsToContents()

    def update_assign_tab(self):
        if self.assign_tab:
            hospital_names = [h.hospital_name for h in hospitals]
            doctor_dnis = [d.dni for h in hospitals for d in h.doctors]
            self.assign_tab.update_data(hospital_names, doctor_dnis)
    
    
