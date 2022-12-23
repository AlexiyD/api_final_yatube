# Проект «API для Yatube»
API для Yatube - Позволяет запрашивать данные о постах, группах, комментариях в социальной сети Yatube, а также создавать новые.

### Технологии:
* Python 3.7.9 
* Django 3.2.16
* Django REST framework 3.12.4
* JWT + Djoser 2.1.0

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
* Получить список всех постов (GET):
http://127.0.0.1:8000/api/v1/posts/

* Получить определенный пост (GET):
http://127.0.0.1:8000/api/v1/posts/1/

* Получить коментарии определенного поста (GET):
http://127.0.0.1:8000/api/v1/posts/1/comments/

* Получить список всех групп (GET):
http://127.0.0.1:8000/api/v1/groups/

* Создать новый пост (POST):
(Требуется аутентификация)/
http://127.0.0.1:8000/api/v1/posts/

* Полная документация доступна по адресу: http://localhost:8000/redoc/

Автор: Зубков Алексей *AlexiyD*