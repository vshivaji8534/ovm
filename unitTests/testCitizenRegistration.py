import unittest
from CitizenRegistration import CitizenRegistration

class TestCitizenRegistration(unittest.TestCase):

    def setUp(self):
        self.citizen_registration = CitizenRegistration()

    def test_create_account(self):
        user_info = {"name": "John Doe", "age": 30, "country": "India"}

        self.citizen_registration.create_account(user_info)

        self.assertIn(user_info, self.citizen_registration.users)

    def test_check_compliance_with_local_laws_pass(self):
        country = "India"

        self.citizen_registration.check_compliance_with_local_laws(country)

        self.assertIn("Compliance check passed for India", self.capturedOutput.getvalue().strip())

    def test_check_compliance_with_local_laws_fail(self):
        country = "USA"

        self.citizen_registration.check_compliance_with_local_laws(country)

        self.assertIn("Compliance check failed for USA", self.capturedOutput.getvalue().strip())

if __name__ == "__main__":
    unittest.main()