# Проект расчета квартплаты

## Описание

Это проект для расчета квартплаты для домов, включающий модели данных для домов, квартир, водомеров и тарифов, а также API для ввода и вывода данных. Проект реализован на Django, с использованием Celery для асинхронных задач и PostgreSQL в качестве базы данных.

## Стек технологий

- Python 3.8+
- Django
- Django REST Framework (DRF)
- Celery
- PostgreSQL
- Redis
- Docker (для удобства развертывания)

## Установка

### Склонируйте репозиторий

```sh
git clone https://github.com/yourusername/yourproject.git
cd yourproject
```

### Создайте и активируйте виртуальное окружение

```sh
python -m venv venv
source venv/bin/activate  # Для Linux/MacOS
venv\Scripts\activate  # Для Windows
```

### Установите зависимости

```sh
pip install -r requirements.txt
```

### Настройка базы данных

Создайте базу данных PostgreSQL и настройте параметры подключения в файле `myproject/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yourdbname',
        'USER': 'yourdbuser',
        'PASSWORD': 'yourdbpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Примените миграции

```sh
python manage.py migrate
```

### Создайте суперпользователя

```sh
python manage.py createsuperuser
```

### Настройка Celery

Убедитесь, что Redis запущен, и добавьте следующие настройки в `myproject/settings.py`:

```python
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
```

Запустите Celery в отдельном терминале:

```sh
celery -A myproject worker --loglevel=info
```

### Запуск проекта

Запустите сервер разработки:

```sh
python manage.py runserver
```

Откройте браузер и перейдите по адресу `http://127.0.0.1:8000/admin/`, чтобы войти в админку Django.

## API Endpoints

### Получение информации о домах

- `GET /api/buildings/` - список всех домов
- `GET /api/buildings/{id}/` - информация о конкретном доме

### Запуск расчета квартплаты

- `POST /api/calculate_rent/{building_id}/` - запуск процесса расчета квартплаты для всех квартир в доме за указанный месяц

Пример тела запроса:

```json
{
    "month": "2023-07-01"
}
```

## Структура проекта

- `buildings/` - приложение для управления домами и квартирами
- `watermeters/` - приложение для управления водомерами и их показаниями
- `tariffs/` - приложение для управления тарифами
- `myproject/` - основная конфигурация проекта Django

## Лицензия

Этот проект лицензирован под MIT License - подробности см. в файле `LICENSE`.

## Авторы

- [Daniil Miroshnichenko]([https://github.com/yourusername](https://github.com/daniilmir3105))

