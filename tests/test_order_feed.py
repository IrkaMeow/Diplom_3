import allure
import pytest

@allure.epic('Тесты страницы Лента Заказов')
class TestOrderFeed:

    @allure.title('При создании нового заказа счётчик за {counter_type} увеличивается')
    @pytest.mark.parametrize('counter_type', ['все время', 'сегодня'])
    def test_create_order_boost_counters(self, _login_user, main_page, order_feed_page, counter_type):
        order_feed_page.open_order_feed()
        old_count = order_feed_page.get_count_order_by_type(counter_type)

        main_page.click_constructor()
        main_page.drag_and_drop_ingredient('Флюоресцентная булка R2-D3')
        main_page.click_order()
        main_page.wait_change_track_order()


        order_feed_page.open_order_feed()
        order_feed_page.wait_count_order_change(counter_type, old_count)
        new_count = order_feed_page.get_count_order_by_type(counter_type)
        assert int(new_count) > int(old_count) 

    @allure.title('Трек заказа появляется в разделе «В работе»')
    def test_new_order_in_work_section(self, _login_user, main_page, order_feed_page):
        main_page.open_main_page()
        main_page.drag_and_drop_ingredient('Флюоресцентная булка R2-D3')
        main_page.click_order()
        main_page.wait_change_track_order()
        track = main_page.get_order_track()

        order_feed_page.open_order_feed()

        assert order_feed_page.wait_order_track_in_work_section(track)
