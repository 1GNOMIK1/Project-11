from datetime import datetime, timedelta, date
birthdate = datetime.strptime(input('Введите ваш день рождения (гггг-мм-дд): '),"%Y-%m-%d").date().year
gender = int(input("Введите пол 1=мужской, 2=женский: "))
surname = input("Введите фамилию: ")

if birthdate in ('1900', '1949'):
    first = 1
elif birthdate in ('1950', '1999'):
    first = 2
elif birthdate in ('1800', '1849'):
    first = 3
elif birthdate in ('1850', '1899'):

#   <= надо поставить
