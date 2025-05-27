import unittest
from model.hospital import Hospital
from controller import controller_hospital
from controller.storage import hospitals

class TestHospitalController(unittest.TestCase):
    def setUp(self):
        # Limpiar hospitales antes de cada test
        hospitals.clear()

    def test_create_hospital(self):
        controller_hospital.create_hospital("Hospital Central")
        self.assertEqual(len(hospitals), 1)
        self.assertEqual(hospitals[0].hospital_name, "Hospital Central")

    def test_find_hospital_exists(self):
        controller_hospital.create_hospital("Hospital del Norte")
        result = controller_hospital.find_hospital("Hospital del Norte")
        self.assertIsInstance(result, Hospital)
        self.assertEqual(result.hospital_name, "Hospital del Norte")

    def test_find_hospital_not_exists(self):
        result = controller_hospital.find_hospital("Hospital Fantasma")
        self.assertIsNone(result)

    def test_delete_hospital(self):
        controller_hospital.create_hospital("Hospital del Sur")
        controller_hospital.delete_hospital("Hospital del Sur")
        self.assertEqual(len(hospitals), 0)
        self.assertIsNone(controller_hospital.find_hospital("Hospital del Sur"))

if __name__ == '__main__':
    unittest.main()
