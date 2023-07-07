import requests


def get_apartment_data():
    response = requests.get('http://127.0.0.1:8080/Apartment/apartments')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        pass


def get_filter_apartment(max_price, title, country, city, type, room_count):
    response = requests.get(f'http://127.0.0.1:8080/Apartment/filter?max_price={max_price}&title={title}&country={country}&city={city}&type={type}&room_count={room_count}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        pass


def get_apartment_data_by_id(apartment_id):
    response = requests.get(f'http://127.0.0.1:8080/Apartment/apartments/{apartment_id}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        pass
