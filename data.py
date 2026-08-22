class Urls:
    MAIN_URL = 'https://stellarburgers.education-services.ru/'
    REGISTRATION_URL = 'https://stellarburgers.education-services.ru/register'
    LOGIN_URL = 'https://stellarburgers.education-services.ru/login'
    ORDER_FEED_URL = 'https://stellarburgers.education-services.ru/feed'


class Api:
    # Ссылки для запросов по пользователям 
    REGISTR_USER = f"{Urls.MAIN_URL}api/auth/register"
    DATA_USER = f"{Urls.MAIN_URL}api/auth/user"