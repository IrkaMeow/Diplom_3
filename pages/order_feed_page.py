import allure
from data import Urls, CounterType
from locators import OrderFeedLocators as OL
from .base_page import BasePage

class OrderFeedPage(BasePage):
    @allure.step('Открываем страницу Лента заказов')
    def open_order_feed(self):
        self.open_page(Urls.ORDER_FEED_URL)
        return self

    @allure.step('Получаем количество заказов')
    def get_count_order_by_type(self, counter_type:CounterType):
        locator = OL._COUNTER_LOCATOR_MAP[counter_type]
        return self.get_text(locator)

    @allure.step('Ждем, пока количество заказов изменится')
    def wait_count_order_change(self, counter_type:CounterType, old_count):
        locator = OL._COUNTER_LOCATOR_MAP[counter_type]
        return self.wait_text_to_change(locator, old_count)
    
    @allure.step('Ждем, пока трек заказа отобразится')
    def wait_order_track_in_work_section(self, number):
        return self.is_element_present(OL.get_order_ready(number))
    