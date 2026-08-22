import allure
from data import Urls
from locators import OrderFeedLocators as OL
from .base_page import BasePage

class OrderFeedPage(BasePage):
    @allure.step('Открываем страницу Лента заказов')
    def open_order_feed(self):
        self.open_page(Urls.ORDER_FEED_URL)
        return self

    @allure.step('Получаем количество заказов за {counter_type}')
    def get_count_order_by_type(self, counter_type):
        if counter_type == 'все время':
            return self.get_text(OL.ALL_ORDER)
        elif counter_type == 'сегодня':
            return self.get_text(OL.TODAY_ORDER)

    @allure.step('Ждем, пока количество заказов изменится')
    def wait_count_order_change(self, counter_type, old_count):
        if counter_type == 'все время':
            return self.wait_text_to_change(OL.ALL_ORDER, old_count)
        elif counter_type == 'сегодня':
            return self.wait_text_to_change(OL.TODAY_ORDER, old_count)

    @allure.step('Ждем, пока трек заказа отобразится')
    def wait_order_track_in_work_section(self, number):
        return self.is_element_present(OL.get_order_ready(number))
    