1. Открыть папку с проектом
2. Установить виртуальное окружение 
- ```python3 -m venv venv```
- ```source env/bin/activate```
3. Установить зависимости ```pip install requirements.txt```
   

4. В файле ```config.py``` заполнить данные про базу данных, которые используется в ```settings.py```, в этом же файле устанавливаем константу ```BOT_TOKEN```
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
        'HOST': 'localhost',
    }
}
```
5. Сделать миграции ```python manage.py migrate```
   

6. В терминале запускаем команду ```python manage.py python loaddata data.json --app=referral_users ```, она создаст 4 записи в базу данных для второго задания

7. Запускаем сервер ```python manage.py runserver```

# Задание номер 1
1. В папке ```bot_task1``` запускаем файл ``` bot_1.py ```
   + В этой же папке есть ```credential.json``` с настройками для Google API 
2. Адрес Google Spread Sheet с доступом на чтение 
[Spread Sheet](https://docs.google.com/spreadsheets/d/1n_ar9Y1mS1OnZRekQ45MswV5HH6T4IhLZLE9IV2r-Vk/edit?usp=sharing)
3. Адрес бота [BOT](https://t.me/alpha_bots_form_bot)
4. Данные сохраняются в Google Sheet и в БД, их можно посмотреть в админке Джанго и в Google sheet

# Задание номер 2
1. В папке ```bot_task2``` запускаем файл ``` bot_2.py ```
2. В БД уже созданы 4 записи:
    * name: **Misha** referral_code **[44444444]**
    + name: **Leo**	referral_code **[33333333]**
    + name: **Ivan**	referral_code **[22222222]**
    + name: **Vadym**	referral_code **[11111111]**
3. Адрес бота с реферальной ссылкой [BOT](https://t.me/alpha_bots_test_bot?start=11111111) 
4. Адрес бота без реферальной ссылкой [BOT](https://t.me/alpha_bots_test_bot) 
