from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.XPATH, "//div[label[text()='Email']]/input") # поле ввода email
    PASSWORD_INPUT = (By.XPATH, "//div[label[text()='Пароль']]/input") # поле ввода пароля
    LOGIN_SUBMIT_BUTTON = (By.XPATH, '//button[text()="Войти"]') # кнопка Войти на странице логина

