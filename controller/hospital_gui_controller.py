from PyQt5.QtWidgets import QMessageBox, QDialog, QTableWidgetItem
from GUI.create_hospital_dialog import CreateHospitalDialog  # Ajusta según tu estructura
from . import controller_hospital
from controller import controller_doctor
from controller.storage import hospitals


class HospitalGUIController:
    def __init__(self, view, assign_tab=None):
        self.view = view
        self.assign_tab = assign_tab  # Inicializa assign_tab como None
        self.view.add_hospital_button.clicked.connect(self.open_create_hospital_dialog)
        self.view.delete_hospital_button.clicked.connect(self.delete_selected_hospital)
        self.refresh_table()

    def set_assign_tab(self, assign_tab):
        self.assign_tab = assign_tab

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

    def assign_doctor(self, hospital_name, doctor_dni):
        hospital = controller_hospital.find_hospital(hospital_name)
        doctor = controller_doctor.search_by_dni(doctor_dni)

        if hospital and doctor:
            try:
                hospital.add_doctor(doctor)
                self.refresh_table()           # <--- refrescar tabla aquí
                self.update_assign_tab()       # <--- refrescar datos en pestaña asignar doctor
                return True
            except Exception as e:
                print(f"Error asignando doctor: {e}")
                return False
        return False

    def delete_doctor(self, hospital_name, doctor_dni):
        hospital = controller_hospital.find_hospital(hospital_name)
        doctor = controller_doctor.search_by_dni(doctor_dni)

        if hospital and doctor and doctor in hospital.doctors:
            try:
                hospital.remove_doctor(doctor)
                self.refresh_table()           # <--- refrescar tabla aquí
                self.update_assign_tab()       # <--- refrescar datos en pestaña asignar doctor
                return True
            except Exception as e:
                print(f"Error eliminando doctor: {e}")
                return False
        return False


    def refresh_table(self):
        self.view.hospital_table.setRowCount(0)
        for i, hospital in enumerate(hospitals):
            self.view.hospital_table.insertRow(i)
            self.view.hospital_table.setItem(i, 0, QTableWidgetItem(hospital.hospital_name))
            self.view.hospital_table.setItem(i, 1, QTableWidgetItem(str(len(hospital.doctors))))
        self.view.hospital_table.resizeColumnsToContents()

    def update_assign_tab(self):
        pass
    
