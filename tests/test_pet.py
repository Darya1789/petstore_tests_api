import pytest
from methods.pet_api import PetApi
from data import ExpectedData, TestData


class TestPet:
    def test_add_new_pet(self, create_pet_data):
        pet = create_pet_data
        api = PetApi()
        response = api.add_new_pet(pet)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['name'] == create_pet_data['name']
        assert response_data['photoUrls'] == create_pet_data['photoUrls']
        assert response_data['status'] == create_pet_data['status']

    @pytest.mark.parametrize('param', ['name', 'photoUrls'])
    def test_add_new_pet_without_required_param(self, create_pet_data, param):
        pet = create_pet_data
        pet[f'{param}'] = ''
        api = PetApi()
        response = api.add_new_pet(pet)
        assert response.status_code == 405
        response_data = response.json()
        assert response_data['message'] == ExpectedData.ADD_PET_INCORRECT_INPUT

    def test_update_pet(self, add_pet_to_store):
        new_pet = add_pet_to_store.json()
        new_pet['name'] = TestData.new_name_for_update_pet
        api = PetApi()
        response = api.update_pet(new_pet)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['name'] == TestData.new_name_for_update_pet
    
    def test_get_pet_by_id(self, add_pet_to_store):
        pet_id = add_pet_to_store.json()['id']
        api = PetApi()
        response = api.get_pet_by_id(pet_id)
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['name'] == add_pet_to_store.json()['name']
        assert response_data['photoUrls'] == add_pet_to_store.json()['photoUrls']
        assert response_data['status'] == add_pet_to_store.json()['status']

    def test_delete_pet(self, create_pet_data):
        pet = create_pet_data
        api = PetApi()
        response_add = api.add_new_pet(pet)
        pet_id = response_add.json()['id']
        response = api.delete_pet(pet_id)
        assert response.status_code == 200
        response_get = api.get_pet_by_id(pet_id)
        assert response_get.status_code == 404        
        
