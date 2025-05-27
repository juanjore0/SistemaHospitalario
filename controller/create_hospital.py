from model.hospital import Hospital
from controller.storage import hospitals

def create_hospital(name):
    """
    Crea un hospital vacío (sin doctores).
    """
    hospital = Hospital(name)
    hospitals.append(hospital)
