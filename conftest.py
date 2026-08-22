import allure
import pytest
import requests
import generators
from data import Urls, Api
from pages import MainPage, OrderFeedPage
from locators import MainLocators as ML, LoginLocators as LL
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(params = ['chrome', 'firefox'])
def driver(request):

    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()

    yield driver

    driver.quit()



# объект для работы с главной страницей
@pytest.fixture()
def main_page(driver):
    return MainPage(driver)



# объект для работы со страницей Лента Заказов
@pytest.fixture()
def order_feed_page(driver):
    return OrderFeedPage(driver)



# регистрирует, логинит и удаляет пользователя
@pytest.fixture
def _login_user(driver, main_page):
    email = generators.email_generator()
    password = generators.password_generator()
    name = generators.name_generator()

    payload = {
        'email': email,
        'password': password,
        'name' : name
    }
    with allure.step('Отправляем запрос на регистрацию пользователя'):
        response = requests.post(Api.REGISTR_USER, json=payload)
    if response.status_code != 200:
        raise RuntimeError(f'Регистрация не удалась. Код: {response.status_code}, ответ: {response.text}')
    accessToken = response.json()['accessToken']

    driver.get(Urls.LOGIN_URL)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LL.EMAIL_INPUT)).send_keys(email)
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LL.PASSWORD_INPUT)).send_keys(password)
    main_page.close_overlay()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LL.LOGIN_SUBMIT_BUTTON)).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(ML.ORDER_BUTTON))

    yield 

    with allure.step('Отправляем запрос на удаление пользователя'):
        requests.delete(Api.DATA_USER, headers={'Authorization': accessToken})
