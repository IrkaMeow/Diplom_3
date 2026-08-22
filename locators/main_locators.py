from selenium.webdriver.common.by import By

class MainLocators:
    CONSTRUCTOR_BUTTON = (By.LINK_TEXT, 'Конструктор') # кнопка Конструктор в шапке сайта
    ORDER_FEED_BUTTON = (By.LINK_TEXT, 'Лента Заказов') # кнопка Лента заказов в шапке сайта
    ACCOUNT_BUTTON = (By.LINK_TEXT, 'Личный Кабинет') # кнопка Личный кабинет
    ORDER_BUTTON = (By.XPATH, '//button[text()="Оформить заказ"]') # кнопка оформления заказа
    MODAL_WINDOW_HEADER = (By.XPATH, '//section//h2[text()="Детали ингредиента"]') # модульное окно Детали ингредиента - Заголовок
    MODAL_WINDOW_CLOSE = (By.XPATH, '//section[contains(@class, "modal_opened")]//button') # кнопка закрытия модульного окна Детали ингредиента
    BURGER_BASKET = (By.XPATH, '//ul[contains(@class, "basket__list")]') # корзина для сборки бургера
    ORDER_TRACK = (By.XPATH, '//h2[contains(@class, "modal__title_shadow")]') # номер заказа

    ''' Динамические локаторы '''
    
    @staticmethod
    # находит ингредиент по его названию
    def get_ingredient_by_name(name):
        return (By.XPATH, f'//p[text()="{name}"]/ancestor::a')

    # находит счетчик ингредиента по его названию
    @staticmethod
    def get_count_by_name(name):
        return (By.XPATH, f'//p[text()="{name}"]/ancestor::a//p[contains(@class, "counter__num")]')
