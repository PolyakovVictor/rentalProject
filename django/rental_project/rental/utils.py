import requests


def get_apartment_data():
    response = requests.get('http://127.0.0.1:8080/Apartment/apartments')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # Обработка ошибки при запросе к FastAPI
        # Верните сообщение об ошибке или выполните другие действия
        pass


def get_apartment_data_by_id(apartment_id):
    response = requests.get(f'http://127.0.0.1:8080/Apartment/apartments/{apartment_id}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # Обработка ошибки при запросе к FastAPI
        # Верните сообщение об ошибке или выполните другие действия
        pass
