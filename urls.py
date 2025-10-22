

class Urls:
    BASE_URL = 'https://petstore.swagger.io/v2'
    ADD_PET = f'{BASE_URL}/pet'
    UPDATE_PET = f'{BASE_URL}/pet'
    GET_PET_BY_ID = f'{BASE_URL}/pet/'
    DELETE_PET = f'{BASE_URL}/pet/'

    GET_INVENTORY = f'{BASE_URL}/story/inventory'
    PLACE_ORDER = f'{BASE_URL}/store/order'
    DELETE_ORDER = f'{BASE_URL}/store/order/'

    CREATE_USER_ARRAY = f'{BASE_URL}/user/createWithArray'
    CREATE_USER_LIST = f'{BASE_URL}/user/createWithList'
    GET_USER = f'{BASE_URL}/user/'
    UPDATE_USER = f'{BASE_URL}/user/'
    DELETE_USER = f'{BASE_URL}/user/'
    LOGIN_USER = f'{BASE_URL}/user/login'
    LOGOUT_USER = f'{BASE_URL}/user/logout'
    CREATE_USER = f'{BASE_URL}/user'