from model.doctor import Doctor
from controller.storage import hospitals

def create_doctor(doctor_info):
    """
    Crea y retorna un objeto Doctor a partir de un diccionario con los datos.
    
    doctor_info debe contener las claves: "doctor_name", "speciality", "dni".
    """
    return Doctor(
        doctor_info["doctor_name"],
        doctor_info["speciality"],
        doctor_info["dni"]
    )

def delete_doctor(hospital_name, doctor_dni):
    """
    Elimina un doctor de un hospital por su DNI.
    Retorna True si se eliminó correctamente, False si no se encontró el doctor.
    """
    for hospital in hospitals:
        if hospital.hospital_name == hospital_name:
            for doctor in hospital.doctors:
                if doctor.dni == doctor_dni:
                    hospital.remove_doctor(doctor)
                    return True
    return False  # Doctor no encontrado

def add_doctor_to_hospital(hospital_name, doctor_info):
    """
    Agrega un doctor a un hospital existente.
    doctor_info debe contener las claves: "doctor_name", "speciality", "dni".
    """
    for hospital in hospitals:
        if hospital.hospital_name == hospital_name:
            doctor = create_doctor(doctor_info)
            hospital.append_doctor(doctor)
            return True
    return False  # Hospital no encontrado

def search_by_dni(dni):
    """
    Busca un doctor en todos los hospitales por su DNI.
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
