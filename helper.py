from faker import Faker
import random
import string


class GenerateData:
    faker = Faker()

    def generate_string(length: int = 8):
        return ''.join(random.choices(string.ascii_lowercase, k=length))


    def generate_pet_data(self):
        payload_pet = {
            "name": self.faker.first_name(),
            "photoUrls": [self.faker.image_url()],
            "status": random.choice(["available", "pending", "sold"])
        }
        return payload_pet

    def generate_user_data(self):
        payload_user = {
            "username": self.generate_string(10),
            "firstName": self.faker.first_name(),
            "lastName": self.faker.last_name(),
            "email": self.faker.email(),
            "password": self.generate_string(12),
            "phone": self.faker.phone_number(),
            "userStatus": random.randint(0, 1)
        }
        return payload_user

    def generate_order_data(self, pet_id: int) -> dict:
        payload_order = {
            "petId": pet_id,
            "quantity": random.randint(1, 10),
            "status": "placed",
            "complete": False
        }
        return payload_order



# def generate_user():
        
# # Генерируем гарантированно уникальный email
#         timestamp = int(time.time() * 1000)  # текущее время в миллисекундах
#         random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        
#         email = f"test{timestamp}{random_suffix}@example.com"
#         name = faker.first_name()
#         password = faker.password()  # Используем надежный пароль
        
#         payload_user_registration = {
#             'email': email, 
#             'password': password, 
#             'name': name
#         }
#         payload_user_login = {
#             'email': email, 
#             'password': password
#         }
        
#         return payload_user_registration, payload_user_login