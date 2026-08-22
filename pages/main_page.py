import allure
from data import Urls
from locators import MainLocators as ML
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage

class MainPage(BasePage):
    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        return self.open_page(Urls.MAIN_URL)

    @allure.step('Нажимаем кнопку Конструктор')
    def click_constructor(self):
        self.close_overlay
        constructor_order = self.find_clickable_element(ML.CONSTRUCTOR_BUTTON)
        constructor_order.click()
        return self

    @allure.step('Нажимаем кнопку Лента Заказов')
    def click_order_feed(self):
        self.close_overlay
        order_feed = self.find_clickable_element(ML.ORDER_FEED_BUTTON)
        order_feed.click()
        return self

    @allure.step('Нажимаем кнопку Оформить заказ')
    def click_order(self):
        self.close_overlay()
        button_order = self.find_clickable_element(ML.ORDER_BUTTON)
        button_order.click()
        return self
    
    @allure.step('Нажимаем на ингредиент {name}')
    def click_ingredient(self, name):
        ingredient = self.find_clickable_element(ML.get_ingredient_by_name(name))
        # принудительный клик через JS
        self.driver.execute_script("arguments[0].click();", ingredient)
        return self
    
    @allure.step('Добавляем ингредиент {name} в заказ')
    def drag_and_drop_ingredient(self, name):
        return self.drag_and_drop_elements(ML.get_ingredient_by_name(name), ML.BURGER_BASKET)

    @allure.step('Узнаем количество добавленных ингредиентов')
    def get_count_ingredient(self, name):
         return self.get_text(ML.get_count_by_name(name))
    
    @allure.step('Проверяем видимость модального окна Детали ингредиента')
    def open_modal_window(self):
        return self.is_element_present(ML.MODAL_WINDOW_HEADER)

    @allure.step('Проверяем, что модальное окно Детали ингредиента НЕ видимо')
    def close_modal_window(self):       
        return self.wait_for_invisibility(ML.MODAL_WINDOW_HEADER)
    
    @allure.step('Закрываем модальное окно нажатием на крестик')
    def click_x_modal_window(self):
        button_close = self.find_clickable_element(ML.MODAL_WINDOW_CLOSE)
        button_close.click()
        return self

    @allure.step('Ждем, пока трек заказа изменится')
    def wait_change_track_order(self):
        try:
            self.wait_text_to_change(ML.ORDER_TRACK, '9999')
        except TimeoutException:
            raise AssertionError('Трек заказа остался 9999')

    @allure.step('Получаем номер заказа')
    def get_order_track(self):
        self.wait_text_to_change(ML.ORDER_TRACK, '9999')
        element = self.find_visible_element(ML.ORDER_TRACK)
        return element.text
