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

def delete_hospital(name):
    global hospitals
    hospitals = [hospital for hospital in hospitals if hospital.hospital_name != name]

def delete_doctor(dni, hospital_name):
    for hospital in hospitals:
        if hospital.hospital_name == hospital_name:
            hospital.doctors = [doctor for doctor in hospital.doctors if doctor.dni != dni]
            if not hospital.doctors:
                delete_hospital(hospital_name)
            break  # Ya lo encontramos, no necesitamos seguir buscando
