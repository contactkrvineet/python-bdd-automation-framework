from faker import Faker


class DataGenerator:
    def __init__(self):
        self.fake = Faker()

    def generate_user_data(self):
        """Generate random user data"""
        return {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'email': self.fake.email(),
            'phone': self.fake.phone_number(),
            'address': self.fake.address(),
            'company': self.fake.company(),
            'job_title': self.fake.job()
        }

    def generate_email(self):
        return self.fake.email()

    def generate_password(self, length=12):
        return self.fake.password(length=length, special_chars=True, digits=True, upper_case=True, lower_case=True)

    def generate_name(self):
        return self.fake.name()

    def generate_address(self):
        return self.fake.address()

    def generate_phone(self):
        return self.fake.phone_number()