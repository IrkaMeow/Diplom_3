from faker import Faker

fake = Faker()

# генерирует случайный email
def email_generator():
    generated_email = fake.unique.email(domain='superpuper.ru')
    return generated_email

# генерирует случайное имя
def name_generator():
    generated_name = fake.unique.user_name()
    return generated_name

# генерирует случайный пароль
def password_generator():
    generated_password = fake.password()
    return generated_password
