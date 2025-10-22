import requests
from urls import Urls

class PetApi:
    def add_new_pet(self, pet):
        payload_pet = pet
        response = requests.post(Urls.ADD_PET, json = payload_pet)
        return response
    
    def delete_pet(self, pet_id):
        delete_url = f'{Urls.DELETE_PET}{pet_id}'
        response = requests.delete(delete_url)
        return response

    def get_pet_by_id(self, pet_id):
        get_url = f'{Urls.GET_PET_BY_ID}{pet_id}'
        response = requests.get(get_url)
        return response
    
    def update_pet(self, pet):
        payload_pet = pet
        response = requests.post(Urls.UPDATE_PET, json = payload_pet)
        return response
