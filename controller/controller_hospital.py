from model.hospital import Hospital
from controller.storage import hospitals
from model.doctor import Doctor

def create_hospital(name):
    """
    Crea un hospital vacío (sin doctores).
    """
    hospital = Hospital(name)
    hospitals.append(hospital)


def delete_hospital(name):
    """
    Elimina un hospital por su nombre.
    """
    hospitals[:] = [h for h in hospitals if h.hospital_name != name]


def find_hospital(name):
    """
    Busca un hospital por su nombre.
    Retorna el hospital si lo encuentra, None si no existe.
    """
    for hospital in hospitals:
        if hospital.hospital_name == name:
            return hospital
    return None

def add_doctor_to_hospital(hospital_name, doctor_name, speciality, dni):
    for hospital in hospitals:
        if hospital.hospital_name == hospital_name:
            new_doctor = Doctor(doctor_name, speciality, dni)
            hospital.append_doctor(new_doctor)
            return True
    return False