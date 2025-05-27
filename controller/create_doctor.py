from model.doctor import Doctor

def create_doctor(doctor_info):
    """
    Crea y retorna un objeto Doctor a partir de un diccionario con los datos.
    
    doctor_info debe contener las claves: "doctor_name", "speciality", "dni".
    """
    doctor = Doctor(
        doctor_info["doctor_name"],
        doctor_info["speciality"],
        doctor_info["dni"]
    )
    return doctor