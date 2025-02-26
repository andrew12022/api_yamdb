# YaMDb

**YaMDb** —  это API-сервис, предназначенный для сбора отзывов пользователей на различные произведения. Сервис позволяет пользователям выражать свои мнения, оставляя текстовые отзывы и выставляя оценки произведениям в диапазоне от одного до десяти.

## Функции:

- Сбор отзывов и оценок произведений.
- Категоризация произведений и присвоение им жанров.
- Аутентификация пользователей и их разрешения на добавление отзывов, комментариев и оценок.
- Возможность оставлять комментарии к отзывам пользователей.

## Установка:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:andrew12022/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Примеры API-запросов:

> POST http://127.0.0.1:8000/api/v1/auth/signup/
Регистрация нового пользователя.
```
{
"email": "user@example.com",
"username": "string"
}
```

Статус код ```200:```
Ответ:
```
{
"email": "user@example.com",
"username": "string"
}
```
> POST http://127.0.0.1:8000/api/v1/auth/token/
Получение JWT-токена.
```
{
"username": "string",
"confirmation_code": "string"
}
```

Статус код ```200:```
Ответ:
```
{
"token": "string"
}
```
> GET http://127.0.0.1:8000/api/v1/posts/
Получение публикаций.
Статус код ```200:```
```
{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Побег из Шоушенка",
            "year": 1994,
            "rating": 10,
            "description": "",
            "genre": [
                {
                    "name": "Драма",
                    "slug": "drama"
                }
            ],
            "category": {
                "name": "Фильм",
                "slug": "movie"
            }
        },
        {
            "id": 2,
            "name": "Крестный отец",
            "year": 1972,
            "rating": 4,
            "description": "",
            "genre": [
                {
                    "name": "Драма",
                    "slug": "drama"
                }
}
```
> POST http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/
Добавление нового отзыва.
```
{
"text": "string".
"score": 1
}
```
Статус код ```201:```
Ответ:
```
{
"id": 0,
"text": "string",
"author": "string",
"score": 1,
"pub_date": "2019-08-24T14:15:22Z"
}
```

Документация данного проекта находится по адресу: http://127.0.0.1:8000/redoc/

## Технологии и необходимые инструменты
- Python
- Django
- Django REST framework
- SQLite

## Авторы
- [Андрей Елистратов](https://github.com/andrew12022)
- [Кирилл Новоселов](https://github.com/Scorcer777)
- [Владимир Шевченко](https://github.com/vladimir-shevchenko01)
