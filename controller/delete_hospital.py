from controller.storage import hospitals

def delete_hospital(name):
    """
    Elimina un hospital por su nombre.
    """
    hospitals[:] = [h for h in hospitals if h.hospital_name != name]
