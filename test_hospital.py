import unittest
from hospital_logic import HospitalSystem

class TestHospital(unittest.TestCase):
    def setUp(self):
        self.system = HospitalSystem()

    def test_registration(self):
        # Test if a patient is correctly added to the queue
        p_id, p_data = self.system.register_patient("Test User", "30", "Flu")
        self.assertEqual(len(self.system.waiting_list), 1)
        self.assertIn(p_id, self.system.waiting_list)

    def test_queue_order(self):
        # Test First-In-First logic
        self.system.register_patient("User 1", "20", "A")
        self.system.register_patient("User 2", "25", "B")
        first = self.system.get_next_patient()
        self.assertEqual(first, 'P101')

if __name__ == "__main__":
    unittest.main()