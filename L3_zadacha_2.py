# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def personal_info(name, surname, year_of_birth, city, email, tel):
    print(f'Имя: {name} Фамилия: {surname} Год рождения: {year_of_birth} Город проживания: {city} Email: {email} Телефон: {tel}')

personal_info(name = input('Имя: '),
         surname = input('Фамилия: '),
         year_of_birth = input('Год рождения: '),
         city = input('Город проживания: '),
         email = input('Email: '),
         tel = input('Телефон: '))