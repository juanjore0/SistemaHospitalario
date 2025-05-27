from PyQt5.QtWidgets import QMessageBox, QDialog, QTableWidgetItem
from GUI.create_doctor_dialog import CreateDoctorDialog
from . import controller_doctor
from controller.storage import hospitals  # Lista global de hospitales
from controller.storage import doctors  # Lista global de doctores no asignados

class DoctorGUIController:
    def __init__(self, view):
        self.view = view
        self.assign_tab = None  # Inicializa assign_tab como None
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
            self.update_assign_tab()

    def refresh_table(self):
        self.view.doctor_table.setRowCount(0)
        for i, doctor in enumerate(doctors):
            self.view.doctor_table.insertRow(i)
            self.view.doctor_table.setItem(i, 0, QTableWidgetItem(doctor.hospital_name if doctor.hospital_name else ""))
            self.view.doctor_table.setItem(i, 1, QTableWidgetItem(doctor.name))
            self.view.doctor_table.setItem(i, 2, QTableWidgetItem(doctor.dni))
            self.view.doctor_table.setItem(i, 3, QTableWidgetItem(doctor.specialty))
        
        self.view.doctor_table.resizeColumnsToContents()

        # Esto actualiza la pestaña de asignaciones si se pasó
        if self.assign_tab:
            self.assign_tab.update_data(
                [h.hospital_name for h in hospitals],
                [d.dni for d in doctors]
            )
            
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
            self.update_assign_tab()
        else:
            QMessageBox.warning(self.view, "Error", "No se pudo eliminar el doctor.")

    def update_assign_tab(self):
        if self.assign_tab:
            hospital_names = [h.hospital_name for h in hospitals]
            doctor_dnis = [d.dni for h in hospitals for d in h.doctors]
            self.assign_tab.update_data(hospital_names, doctor_dnis)
