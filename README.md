Weather Forecast

Простой Django-проект для прогноза погоды.

Описание

Проект позволяет искать информацию о погоде по запросу, имеет регистрацию и авторизацию пользователей.
Собран в Docker для быстрого развёртывания.

Технологии
	•	Python 3.14
	•	Django 5.2.8
	•	Docker Compose
	•	SQLite (по умолчанию)
	•	requests, python-dotenv, boto3
    •	Django Rest Framework

Установка и запуск

Локально (без Docker)
	1.	Клонируем репозиторий:

git clone https://github.com/nasrdnvv/Weather_Forecast
cd Weather_Forecast/src

	2.	Создаём и активируем виртуальное окружение:

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

	3.	Устанавливаем зависимости:

pip install -r requirements.txt

	4.	Применяем миграции:

python manage.py migrate

	5.	Запускаем сервер:

python manage.py runserver

Сайт доступен: http://127.0.0.1:8000￼

C Docker Compose

# Собрать и запустить контейнеры
docker-compose up --build

# В фоне
docker-compose up -d

# Остановить и удалить контейнеры
docker-compose down