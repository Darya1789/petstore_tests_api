import pytest
import allure
from methods.pet_api import PetApi
from data import ExpectedData, TestData

@allure.suite('API тесты для pet')
class TestPet:

    @allure.title('Проверка создания питомца с обязательными параметрами')
    def test_add_new_pet(self, create_pet_data):
        with allure.step('Генерируем данные для создания питомца'):
            pet = create_pet_data
        api = PetApi()
        with allure.step('Отправляем запрос на создание питомца'):
            response = api.add_new_pet(pet)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 200
        with allure.step('Сохраняем данные ответа'):
            response_data = response.json()
        with allure.step('Проверяем имя созданного питомца'):
            assert response_data['name'] == create_pet_data['name']
        with allure.step('Проверяем url фото созданного питомца'):
            assert response_data['photoUrls'] == create_pet_data['photoUrls']
        with allure.step('Проверяем статус сохданного питомца'):
            assert response_data['status'] == create_pet_data['status']
    
    
    @allure.title('Проверка создания питомца без параметра {param}')
    @pytest.mark.parametrize('param', ['name', 'photoUrls'])
    def test_add_new_pet_without_required_param(self, create_pet_data, param):
        with allure.step('Генерируем данные для создания питомца'):
            pet = create_pet_data
        with allure.step(f'Обнуляем параметр {param}'):
            pet[f'{param}'] = ''
        api = PetApi()
        with allure.step('Отправляем запрос на создание питомца'):
            response = api.add_new_pet(pet)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 405
        with allure.step('Сохраняем данные ответа'):
            response_data = response.json()
        with allure.step('Проверяем сообщение об ошибке'):
            assert response_data['message'] == ExpectedData.ADD_PET_INCORRECT_INPUT

    @allure.title('Проверка обновления данных питомца')
    def test_update_pet(self, add_pet_to_store):
        with allure.step('Создаем питомца'):
            new_pet = add_pet_to_store.json()
        with allure.step('Обновляем имя питомца'):
            new_pet['name'] = TestData.new_name_for_update_pet
        api = PetApi()
        with allure.step('Отправляем запрос на обновление питомца'):
            response = api.update_pet(new_pet)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 200
        with allure.step('Сохраняем данные ответа'):
            response_data = response.json()
        with allure.step('Проверяем обновленное имя питомца'):
            assert response_data['name'] == TestData.new_name_for_update_pet
    
    @allure.title('Проверка получения информации о питомце по id')
    def test_get_pet_by_id(self, add_pet_to_store):
        with allure.step('Создаем питомца и получаем id'):
            pet_id = add_pet_to_store.json()['id']
        api = PetApi()
        with allure.step('Отправляем запрос на получение информации о питомце'):
            response = api.get_pet_by_id(pet_id)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 200
        with allure.step('Сохраняем данные ответа'):
            response_data = response.json()
        with allure.step('Проверяем имя питомца'):
            assert response_data['name'] == add_pet_to_store.json()['name']
        with allure.step('Проверяем url фото питомца'):
            assert response_data['photoUrls'] == add_pet_to_store.json()['photoUrls']
        with allure.step('Проверяем статус питомца'):
            assert response_data['status'] == add_pet_to_store.json()['status']

    
    @allure.title('Проверка удаления питомца')
    def test_delete_pet(self, create_pet_data):
        with allure.step('Генерируем данные для создания питомца'):
            pet = create_pet_data
        api = PetApi()
        with allure.step('Отправляем запрос на создание питомца'):
            response_add = api.add_new_pet(pet)
        with allure.step('Получаем id созданного питомца'):
            pet_id = response_add.json()['id']
        with allure.step('Отправляем запрос на удаление питомца'):
            response = api.delete_pet(pet_id)
        with allure.step('Проверяем код ответа'):
            assert response.status_code == 200
        with allure.step('Отправляем запрос на получение информации об удаленном питомце'):
            response_get = api.get_pet_by_id(pet_id)
        with allure.step('Проверяем код ошибки'):
            assert response_get.status_code == 404        
        
