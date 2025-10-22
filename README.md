# petstore_tests_api
API tests for petstore

## Структура проекта
petstore_tests_api/
├── conftest.py # Фикстуры Pytest
├── requirements.txt # Зависимости проекта
├── README.md # Документация
│── helper.py # Генераторы данных
│── data.py # Тестовые данные
│── urls.py # Урлы 
│
├── tests/ # Тестовые сценарии
│ ├── test_pet_api.py # Тесты для эндпоинтов Pet
│ ├── test_store_api.py # Тесты для эндпоинтов Store
│ └── test_user_api.py # Тесты для эндпоинтов User
│
├── methods/ # API методы и клиенты
│ ├── pet_api.py # Методы для работы с Pet API
│ ├── store_api.py # Методы для работы с Store API
│ └── user_api.py # Методы для работы с User API

## Allure отчет
Для просмотра отчета выполнить команду в директории проекта
> allure serve allure-results

## Зависимости
Ддя уставновки зависимостей ввести команду
> pip install -r requirements.txt