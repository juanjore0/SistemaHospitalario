from PyQt5.QtWidgets import QMessageBox, QDialog, QTableWidgetItem
from GUI.create_doctor_dialog import CreateDoctorDialog
from . import controller_doctor
from controller.storage import hospitals

class DoctorGUIController:
    def __init__(self, view):
        self.view = view
        self.view.add_doctor_button.clicked.connect(self.open_create_doctor_dialog)
        self.view.delete_doctor_button.clicked.connect(self.delete_selected_doctor)
        self.refresh_table()

    def open_create_doctor_dialog(self):
        dialog = CreateDoctorDialog(self.view)
        if dialog.exec_() == QDialog.Accepted:
            doctor_info = dialog.get_doctor_info()
            if not all(doctor_info.values()):
                QMessageBox.warning(self.view, "Error", "Todos los campos son obligatorios.")
                return
            success = controller_doctor.create_doctor(doctor_info)
            if not success:
                QMessageBox.warning(self.view, "Error", "No se pudo crear el doctor.")
                return
            self.refresh_table()

    def delete_selected_doctor(self):
        row = self.view.doctor_table.currentRow()
        if row < 0:
            return
        dni_item = self.view.doctor_table.item(row, 2)
        hospital_item = self.view.doctor_table.item(row, 0)
        if not dni_item or not hospital_item:
            QMessageBox.warning(self.view, "Error", "Fila inválida seleccionada.")
            return
        dni = dni_item.text()
        hospital_name = hospital_item.text()
        success = controller_doctor.delete_doctor(hospital_name, dni)
        if success:
            self.refresh_table()
        else:
            QMessageBox.warning(self.view, "Error", "No se pudo eliminar el doctor.")

    def refresh_table(self):
        self.view.doctor_table.setRowCount(0)
        row_index = 0
        for hospital in hospitals:
            for doctor in hospital.doctors:
                self.view.doctor_table.insertRow(row_index)
                self.view.doctor_table.setItem(row_index, 0, QTableWidgetItem(getattr(hospital, 'hospital_name', str(hospital))))
                self.view.doctor_table.setItem(row_index, 1, QTableWidgetItem(getattr(doctor, 'doctor_name', str(doctor))))
                self.view.doctor_table.setItem(row_index, 2, QTableWidgetItem(getattr(doctor, 'dni', '')))
                self.view.doctor_table.setItem(row_index, 3, QTableWidgetItem(getattr(doctor, 'speciality', '')))
                row_index += 1
        self.view.doctor_table.resizeColumnsToContents()
