from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ALL_ORDER = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class, "OrderFeed_number")]')
    TODAY_ORDER = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class, "OrderFeed_number")]')

    # динамический локатор для готового заказа
    @staticmethod
    def get_order_ready(number):
        return (By.XPATH, f'//ul[contains(@class, "orderListReady")]/li[contains(., "{number}")]')
