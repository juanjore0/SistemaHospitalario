from PyQt5.QtWidgets import QMessageBox, QDialog, QTableWidgetItem
from GUI.create_doctor_dialog import CreateDoctorDialog
from . import controller_doctor
from controller.storage import doctors  # Lista global de doctores no asignados

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
        if not dni_item:
            QMessageBox.warning(self.view, "Error", "Fila inválida seleccionada.")
            return
        dni = dni_item.text()
        success = controller_doctor.delete_doctor(dni)
        if success:
            self.refresh_table()
        else:
            QMessageBox.warning(self.view, "Error", "No se pudo eliminar el doctor.")

    def refresh_table(self):
        # Actualizar la lista de doctores antes de mostrarla
        global doctors
        doctors = controller_doctor.get_all_doctors()  # Asegúrate de que este método exista y retorne la lista actualizada
        self.view.doctor_table.setRowCount(0)
        for i, doctor in enumerate(doctors):
            self.view.doctor_table.insertRow(i)
            self.view.doctor_table.setItem(i, 0, QTableWidgetItem("No asignado"))  # Hospital vacío
            self.view.doctor_table.setItem(i, 1, QTableWidgetItem(doctor.doctor_name))
            self.view.doctor_table.setItem(i, 2, QTableWidgetItem(doctor.dni))
            self.view.doctor_table.setItem(i, 3, QTableWidgetItem(doctor.speciality))
        self.view.doctor_table.resizeColumnsToContents()
