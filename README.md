Курсовая работа по DRF. Трекер полезных привычек.

Контекст
В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек
и искоренению старых плохих привычек. 


Запуск проекта.

1. Клонируйте проект 
        
        git clone git@github.com:DuckRainbow/cw7
2. Создайте виртуальное окружение

        python3 - m venv .venv
3. Активируйте виртуальное окружение Poetry

        venv/Scripts/activate
4. Установите зависимости виртуального окружения 

        pip install -r requirements.txt
5. Переименуйте файл .env.sample в .env и заполните необходимые данные
6. Создайте базу данных в PostgreSQL , которую указали в файле .env в параметре DATABASES_NAME
7. Выполните миграции

         python3 manage.py migrate
8. Создайте суперпользователя

         python3 manage.py csuser
9. Запустите Redis

         sudo service redis-server start
10. Запустите проект 

         python3 manage.py runserver
11. Перейдите в админку по адресу http://127.0.0.1:8000/admin. Введите параметры учетной записи admin@example.com
и пароль 123qwe. Заполните пользователей с указанием ID телеграма и привычки.
12. В терминале Pycharm запустить службы worker и beat 


         celery -A config beat -l info -S django 
         python3 -m celery -A config worker -l info 
либо одной командой 

    celery -A config  worker --beat --scheduler django --loglevel=info

После этого каждую минуту (время можно изменить в параметре CELERY_BEAT_SCHEDULE файла SETTINGS) будет выполняться 
задача, а именно отправка напоминания пользователю в телеграм.


После этого каждую минуту (время можно изменить в параметре CELERY_BEAT_SCHEDULE файла SETTINGS) будет выполняться 
задача, а именно отправка напоминания пользователю в телеграм..
