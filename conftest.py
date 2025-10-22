from helper import GenerateData
from methods.pet_api import PetApi
import pytest

from urls import Urls


@pytest.fixture()
def create_pet_data():
    generator = GenerateData()
    pet = generator.generate_pet_data()
    return pet

@pytest.fixture()
def add_pet_to_store(create_pet_data):
    api = PetApi()
    response = api.add_new_pet(create_pet_data)
    yield response
    pet_id = response.json()['id']
    api.delete_pet(pet_id)