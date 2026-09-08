import requests
import allure 
from data import Api

class ApiClient:
    @allure.step('Отправляем запрос на регистрацию пользователя')
    def create_user(self, payload):
        return requests.post(Api.REGISTR_USER, json=payload)

    @allure.step('Отправляем запрос на удаление пользователя')
    def delete_user(self, token):
        headers={'Authorization': token}
        return requests.delete(Api.DATA_USER, headers=headers)