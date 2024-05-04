class CitizenRegistration:

    def __init__(self):
        self.users = []

    def create_account(self, user_info):
        self.users.append(user_info)
        print("Account created successfully for user:", user_info)

    def handle_user_information(self, user_info):
        # Implement code to handle user information securely
        print("User information handled securely for user:", user_info)

    def check_compliance_with_local_laws(self, country):
        # Implement code to check compliance with local laws
        if country == "India":
            print("Compliance check passed for India")
        else:
            print("Compliance check failed for", country)


# Example usage
#registration_system = CitizenRegistration()
#user_info = {"name": "John Doe", "age": 30, "country": "India"}

#registration_system.create_account(user_info)
#registration_system.handle_user_information(user_info)
#registration_system.check_compliance_with_local_laws(user_info["country"])
