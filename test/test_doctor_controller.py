import unittest
from model.doctor import Doctor
from model.hospital import Hospital
import controller.controller_doctor as controller
from controller.storage import hospitals, doctors  # Lista global de hospitales y doctores

class TestDoctorController(unittest.TestCase):
    def setUp(self):
        # Limpiamos la lista global de hospitales antes de cada test
        controller.hospitals.clear()

    def test_create_doctor(self):
        info = {"doctor_name": "Laura", "speciality": "Pediatría", "dni": "123"}
        doctor = controller.create_doctor(info)
        self.assertIsInstance(doctor, Doctor)
        self.assertEqual(doctor.doctor_name, "Laura")
        self.assertEqual(doctor.speciality, "Pediatría")
        self.assertEqual(doctor.dni, "123")

    def test_add_doctor_to_hospital(self):
        hospital = Hospital("San José")
        hospitals.append(hospital)  # Muy importante: agregar hospital a la lista global

        # Crear doctor y agregarlo a la lista global (doctors)
        doctor_info = {"doctor_name": "Dr. Juan", "speciality": "Cardiología", "dni": "123"}
        doctor = controller.create_doctor(doctor_info)  # Esto agrega a doctors

        result = controller.add_doctor_to_hospital("San José", "123")
        self.assertTrue(result)
        self.assertIn(doctor, hospital.doctors)
        self.assertNotIn(doctor, doctors)

    def test_delete_doctor_from_hospital(self):
        hospital = Hospital("Central")
        doctor = Doctor("Marta", "Neurología", "789")
        hospital.append_doctor(doctor)
        controller.hospitals.append(hospital)

        result = controller.delete_doctor("Central", "789")

        self.assertTrue(result)
        self.assertEqual(len(hospital.doctors), 0)

    def test_search_doctor_by_dni(self):
        hospital = Hospital("Regional")
        doctor = Doctor("Andrés", "Oncología", "111")
        hospital.append_doctor(doctor)
        controller.hospitals.append(hospital)

        result = controller.search_by_dni("111")

        self.assertIsNotNone(result)
        self.assertEqual(result["Doctor"], "Andrés")
        self.assertEqual(result["Hospital"], "Regional")

if __name__ == '__main__':
    unittest.main()
