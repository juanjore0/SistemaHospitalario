from model.doctor import Doctor
from controller.storage import hospitals

def add_doctor_to_hospital(hospital_name, doctor_info):
    """
    Agrega un doctor a un hospital existente.
    doctor_info debe ser un diccionario con name, speciality y dni.
    """
    for hospital in hospitals:
        if hospital.hospital_name == hospital_name:
            doctor = Doctor(doctor_info["name"], doctor_info["speciality"], doctor_info["dni"])
            hospital.append_doctor(doctor)
            return True
    return False  # Hospital no encontrado
