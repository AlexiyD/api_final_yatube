# Проект «API для Yatube»
=========================



## Как запустить проект:
---------------------
### Клонировать репозиторий и перейти в него в командной строке:
https://github.com/AlexiyD/api_final_yatube
git clone 

### Cоздать и активировать виртуальное окружение:
python -m venv env
source venv/Scripts/activate

### Установить зависимости из файла requirements.txt:
python -m pip install --upgrade pip
pip install -r requirements.txt

### Выполнить миграции:
python manage.py makemigrations
python manage.py migrate

### Запустить проект:
python manage.py runserver