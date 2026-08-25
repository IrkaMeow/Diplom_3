import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

''' Базовый класс для всех Page Object страниц проекта '''
class BasePage:
    def __init__(self, driver):
        self.driver = driver  
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Ищем видимый элемент на странице')
    def find_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))  

     
    @allure.step('Ищем кликабельный элемент на странице')
    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))


    @allure.step('Проверяем наличие элемента на странице')
    def is_element_present(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False


    @allure.step('Ждем, пока элемент станет невидимым')
    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

        
    @allure.step('Получаем текст элемента')
    def get_text(self, locator):
        element = self.find_visible_element(locator)
        return element.text


    @allure.step('Ждем, пока текст элемента изменится')
    def wait_text_to_change(self, locator, old_text):
        return self.wait.until_not(EC.text_to_be_present_in_element(locator, old_text))


    @allure.step('Открываем нужный Url')
    def open_page(self, url):
        self.driver.get(url)


    @allure.step('Проверяем, что мы на нужной странице')
    def is_url_correct(self, expected_url, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.url_to_be(expected_url))
            return True
        except TimeoutException:
            return False


    @allure.step('Перетаскиваем элемент')
    def drag_and_drop_elements(self, source_locator, target_locator):
        source_element = self.wait.until(EC.visibility_of_element_located(source_locator))
        target_element = self.wait.until(EC.visibility_of_element_located(target_locator))

        js_script = """
            var source = arguments[0];
            var target = arguments[1];
            
            function createEvent(type) {
                var event = new DragEvent(type, {bubbles: true, cancelable: true, dataTransfer: new DataTransfer()});
                return event;
            }
            
            source.dispatchEvent(createEvent('dragstart'));
            var start = Date.now();
            while (Date.now() - start < 150) {
                // Пустой цикл удерживает выполнение 
            }
            target.dispatchEvent(createEvent('drop'));
        """
        self.driver.execute_script(js_script, source_element, target_element)

    @allure.step('Закрываем невидимое модальное окно')
    def close_overlay(self):
        js_hide_overlays = """
            var overlays = document.querySelectorAll('div[class*="Modal_modal_overlay"]');
            overlays.forEach(function(el) {
                el.style.display = 'none';
            });
        """
        try:
            self.driver.execute_script(js_hide_overlays)
        except Exception:
            pass

    @allure.step('Принудительный клик')
    def forceful_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)
