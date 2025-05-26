class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.doctors = []

    def append_doctor(self, doctor):
        self.doctors.append(doctor)
