import allure
import pytest
from data import Urls

@allure.epic('Тесты главной страницы')
class TestMainPage:
    @allure.title('Клик на кнопку Конструктор ведет на главную страницу')
    def test_click_constructor_return_main_page(self, main_page, order_feed_page):
        order_feed_page.open_order_feed()
        main_page.click_constructor()
        assert main_page.is_url_correct(Urls.MAIN_URL)

    @allure.title('Клик на кнопку Лента Заказов ведет на страницу заказов')
    def test_click_order_feed_switch_feed(self, main_page):
        main_page.open_main_page()
        main_page.click_order_feed()
        assert main_page.is_url_correct(Urls.ORDER_FEED_URL)

    @allure.title('Клик по ингредиенту ведет к открытию модального окна Детали ингредиента')
    def test_click_ingredient_open_model_window(self, main_page):
        main_page.open_main_page()
        main_page.click_ingredient('Соус Spicy-X')

        assert main_page.open_modal_window()

    @allure.title('Клик по крестику закрывает модальное окно Детали ингредиента')
    def test_click_x_modal_window_close(self, main_page):
        main_page.open_main_page()
        main_page.click_ingredient('Флюоресцентная булка R2-D3')
        main_page.click_x_modal_window()

        assert main_page.close_modal_window()

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    @pytest.mark.parametrize('ingredient, count', [
        ('Краторная булка N-200i', '2'),
        ('Соус фирменный Space Sauce','1')
    ])
    def test_add_ingredient_boost_count(self, main_page, ingredient, count):
        main_page.open_main_page()
        main_page.drag_and_drop_ingredient(ingredient)

        assert main_page.get_count_ingredient(ingredient) == count
