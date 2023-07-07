from datetime import date

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


def get_group_data_by_user_id(user_id):
    response = requests.get(f'http://127.0.0.1:8080/Group/userGroups/{user_id}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # TODO
        pass


def get_group_data_by_id(group_id):
    response = requests.get(f'http://127.0.0.1:8080/Group/groups/{group_id}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # TODO
        pass


def get_group_data_by_apartment_id(apartment_id):
    response = requests.get(f'http://127.0.0.1:8080/Apartment/getGroups/{apartment_id}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # TODO
        pass


def get_users_by_group_id(group_id):
    response = requests.get(f'http://127.0.0.1:8080/Group/groupUsers/{group_id}')
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        # TODO
        pass


def create_group(apartment_id: int,
                 title: str,
                 description: str,
                 settlers_limit: int,
                 start_of_lease: date,
                 end_of_lease: date,
                 ):
    data = {
        "apartment_id": apartment_id,
        "start_of_lease": str(start_of_lease),
        "end_of_lease": str(end_of_lease),
        "settlers_limit": settlers_limit,
        "title": title,
        "description": description
    }
    response = requests.post('http://127.0.0.1:8080/Group/groups', json=data)
    if response.status_code == 200:
        return response.json()
    else:
        pass


def add_user_to_group(user_id: int, group_id: int):
    data = {
        "user_id": user_id,
        "group_id": group_id
    }
    response = requests.post('http://127.0.0.1:8080/Group/groupUsers', json=data)
    if response.status_code == 200:
        return response.json()
    else:
        pass


def leave_from_group(user_id: int, group_id: int):
    requests.delete(f'http://127.0.0.1:8080/Group/groupUsers/{group_id}/{user_id}')


def delete_group(group_id: int):
    requests.delete(f'http://127.0.0.1:8080/Group/groups/{group_id}')
