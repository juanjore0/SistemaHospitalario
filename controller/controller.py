from model.hospital import Hospital
from model.doctor import Doctor

hospitals = []

def create_hospital(name, doctor_info):
    hospital = Hospital(name)
    for doc in doctor_info:
        doctor = Doctor(doc["name"], doc["speciality"], doc["dni"])
        hospital.append_doctor(doctor)
    hospitals.append(hospital)

def search_by_dni(dni):
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
