from PyQt5.QtWidgets import QMessageBox, QDialog, QTableWidgetItem, QInputDialog
from GUI.create_doctor_dialog import CreateDoctorDialog
from . import controller_doctor
from . import controller_hospital
from controller.storage import doctors, hospitals


class DoctorGUIController:
    def __init__(self, view):
        self.view = view
        self.view.add_doctor_button.clicked.connect(self.assign_doctor_to_hospital)
        self.view.delete_doctor_button.clicked.connect(self.delete_doctor_from_hospital)
        self.refresh_table()

    def assign_doctor_to_hospital(self):
        """
        Asigna un doctor a un hospital pidiendo el DNI del doctor y nombre del hospital.
        """
        # Pedir DNI del doctor
        dni, ok = QInputDialog.getText(self.view, "Asignar Doctor", "Ingrese el DNI del doctor:")
        if not ok or not dni.strip():
            return
        
        # Buscar el doctor
        doctor = controller_doctor.find_doctor(dni.strip())
        if not doctor:
            QMessageBox.warning(self.view, "Error", f"No se encontró un doctor con DNI: {dni}")
            return
        
        # Pedir nombre del hospital
        hospital_name, ok = QInputDialog.getText(self.view, "Asignar Doctor", "Ingrese el nombre del hospital:")
        if not ok or not hospital_name.strip():
            return
        
        # Buscar el hospital
        hospital = controller_hospital.find_hospital(hospital_name.strip())
        if not hospital:
            QMessageBox.warning(self.view, "Error", f"No se encontró un hospital con nombre: {hospital_name}")
            return
        
        # Asignar doctor al hospital
        try:
            hospital.add_doctor(doctor)
            QMessageBox.information(self.view, "Éxito", f"Doctor {doctor.doctor_name} asignado al hospital {hospital.hospital_name}")
            self.refresh_table()
        except Exception as e:
            QMessageBox.warning(self.view, "Error", f"No se pudo asignar el doctor: {str(e)}")

    def delete_doctor_from_hospital(self):
        """
        Elimina un doctor de un hospital pidiendo el DNI del doctor y nombre del hospital.
        """
        # Pedir DNI del doctor
        dni, ok = QInputDialog.getText(self.view, "Eliminar Doctor", "Ingrese el DNI del doctor:")
        if not ok or not dni.strip():
            return
        
        # Buscar el doctor
        doctor = controller_doctor.find_doctor(dni.strip())
        if not doctor:
            QMessageBox.warning(self.view, "Error", f"No se encontró un doctor con DNI: {dni}")
            return
        
        # Pedir nombre del hospital
        hospital_name, ok = QInputDialog.getText(self.view, "Eliminar Doctor", "Ingrese el nombre del hospital:")
        if not ok or not hospital_name.strip():
            return
        
        # Buscar el hospital
        hospital = controller_hospital.find_hospital(hospital_name.strip())
        if not hospital:
            QMessageBox.warning(self.view, "Error", f"No se encontró un hospital con nombre: {hospital_name}")
            return
        
        # Verificar que el doctor esté en el hospital
        if doctor not in hospital.doctors:
            QMessageBox.warning(self.view, "Error", f"El doctor {doctor.doctor_name} no está asignado al hospital {hospital.hospital_name}")
            return
        
        # Eliminar doctor del hospital
        try:
            hospital.remove_doctor(doctor)
            QMessageBox.information(self.view, "Éxito", f"Doctor {doctor.doctor_name} eliminado del hospital {hospital.hospital_name}")
            self.refresh_table()
        except Exception as e:
            QMessageBox.warning(self.view, "Error", f"No se pudo eliminar el doctor: {str(e)}")

    def open_create_doctor_dialog(self):
        """
        Función original para crear doctores (mantenida por si la necesitas).
        """
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

    def refresh_table(self):
        """
        Actualiza la tabla mostrando qué doctores están asignados a qué hospitales.
        """
        self.view.doctor_table.setRowCount(0)
        
        # Obtener todos los doctores
        all_doctors = controller_doctor.get_all_doctors()
        
        row = 0
        for doctor in all_doctors:
            # Buscar en qué hospital está asignado este doctor
            assigned_hospital = "No asignado"
            for hospital in hospitals:
                if doctor in hospital.doctors:
                    assigned_hospital = hospital.hospital_name
                    break
            
            self.view.doctor_table.insertRow(row)
            self.view.doctor_table.setItem(row, 0, QTableWidgetItem(assigned_hospital))
            self.view.doctor_table.setItem(row, 1, QTableWidgetItem(doctor.doctor_name))
            self.view.doctor_table.setItem(row, 2, QTableWidgetItem(doctor.dni))
            self.view.doctor_table.setItem(row, 3, QTableWidgetItem(doctor.speciality))
            row += 1
        
        self.view.doctor_table.resizeColumnsToContents()

    def set_assign_tab(self, assign_tab):
        """
        Guarda la referencia a la pestaña AssignDoctorTab para que este controlador pueda actualizar sus combos.
        """
        self.assign_tab = assign_tab