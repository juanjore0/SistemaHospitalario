import unittest
from model.hospital import Hospital
from model.doctor import Doctor
from controller import storage
from controller import controller_doctor

class TestDoctorController(unittest.TestCase):

    def setUp(self):
        # Limpia la lista de hospitales antes de cada prueba
        storage.hospitals.clear()

        # Crea hospital de prueba
        self.hospital = Hospital("Hospital Central")
        storage.hospitals.append(self.hospital)

    def test_create_doctor(self):
        doctor_info = {
            "doctor_name": "Dr. Ana",
            "speciality": "Cardiología",
            "dni": "123"
        }
        doctor = controller_doctor.create_doctor(doctor_info)
        self.assertIsInstance(doctor, Doctor)
        self.assertEqual(doctor.doctor_name, "Dr. Ana")

    def test_add_doctor_to_hospital(self):
        doctor_info = {
            "doctor_name": "Dr. Juan",
            "speciality": "Neurología",
            "dni": "456"
        }
        result = controller_doctor.add_doctor_to_hospital("Hospital Central", doctor_info)
        self.assertTrue(result)
        self.assertEqual(len(self.hospital.doctors), 1)
        self.assertEqual(self.hospital.doctors[0].dni, "456")

    def test_search_by_dni(self):
        doctor = Doctor("Dr. Laura", "Dermatología", "789")
        self.hospital.append_doctor(doctor)
        result = controller_doctor.search_by_dni("789")
        self.assertIsNotNone(result)
        self.assertEqual(result["Doctor"], "Dr. Laura")

    def test_delete_doctor(self):
        doctor = Doctor("Dr. Mario", "Pediatría", "321")
        self.hospital.append_doctor(doctor)
        result = controller_doctor.delete_doctor("Hospital Central", "321")
        self.assertTrue(result)
        self.assertEqual(len(self.hospital.doctors), 0)

    def test_delete_nonexistent_doctor(self):
        result = controller_doctor.delete_doctor("Hospital Central", "999")
        self.assertFalse(result)

    def test_add_doctor_to_nonexistent_hospital(self):
        doctor_info = {
            "doctor_name": "Dr. X",
            "speciality": "Gastroenterología",
            "dni": "111"
        }
        result = controller_doctor.add_doctor_to_hospital("Inexistente", doctor_info)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
