from model.doctor import Doctor
from controller.storage import hospitals, doctors  # Lista global de hospitales y doctores

def create_doctor(doctor_info):
    """
    Crea un objeto Doctor y lo agrega a la lista global 'doctors'.
    Retorna el objeto creado.
    """
    doctor = Doctor(
        doctor_info["doctor_name"],
        doctor_info["speciality"],
        doctor_info["dni"]
    )
    doctors.append(doctor)
    return doctor

def delete_doctor(hospital_name, doctor_dni):
    """
    Elimina un doctor del hospital especificado por su DNI.
    Retorna True si se eliminó correctamente, False si no se encontró.
    """
    for hospital in hospitals:
        if hospital.hospital_name == hospital_name:
            for doctor in hospital.doctors:
                if doctor.dni == doctor_dni:
                    hospital.doctors = [d for d in hospital.doctors if d.dni != doctor_dni]
                    return True
    return False

def search_by_dni(dni):
    """
    Busca un doctor en todos los hospitales por su DNI.
    Retorna un diccionario con la información si lo encuentra, None si no.
    """
    for hospital in hospitals:
        for doctor in hospital.doctors:
            if doctor.dni == dni:
                return {
                    "Hospital": hospital.hospital_name,
                    "Doctor": doctor.doctor_name,
                    "Especialidad": doctor.speciality,
                    "DNI": doctor.dni
                }
    return None

def add_doctor_to_hospital(hospital_name, doctor_dni):
    """
    Mueve un doctor de la lista global a un hospital por DNI.
    """
    doctor_to_add = None
    for doctor in doctors:
        if doctor.dni == doctor_dni:
            doctor_to_add = doctor
            break
    if not doctor_to_add:
        return False  # No existe doctor en lista global

    for hospital in hospitals:
        if hospital.hospital_name == hospital_name:
            hospital.append_doctor(doctor_to_add)
            doctors[:] = [d for d in doctors if d.dni != doctor_dni]
            return True
    return False

def get_all_doctors():
    """
    Retorna la lista global de doctores no asignados.
    """
    return doctors