# Проект «API для Yatube»
API для Yatube - Позволяет делать запросы к моделям проекта.

## Как запустить проект:

### Клонировать репозиторий и перейти в него в командной строке:
* git clone 
https://github.com/AlexiyD/api_final_yatube


### Cоздать и активировать виртуальное окружение:
* python -m venv env
* source venv/Scripts/activate

### Установить зависимости из файла requirements.txt:
* python -m pip install --upgrade pip
* pip install -r requirements.txt

### Выполнить миграции:
* python manage.py makemigrations
* python manage.py migrate

### Запустить проект:
* python manage.py runserver

## Примеры:

Полная документация доступна по адресу: http://localhost:8000/redoc/