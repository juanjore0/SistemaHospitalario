from controller.storage import hospitals

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
