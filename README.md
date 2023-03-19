# **YaMDb API**
## Overview
**YaMDb API** это веб-API, основанный на фреймворке Django REST.
Он позволяет людям и сторонним приложениям подключаться к базе отзывов и информации о медиа различных категорий.
таких как фильмы, музыка, книги и многие другие.

Запустив проект вы получите доступ к различным url-маршрутам, чтобы включить использование функций веб-сайта:
* добавление и поиск информации о названиях, жанрах и категориях
* просмотр заголовков
* комментирование отзывов
* редактирование профилей пользователей в качестве администратора или собственного профиля в качестве аутентифицированного пользователя


Список всех URL будет доступен по ссылке `/redoc/` после запуска проекта.


## Требования к системеЖ
   * Python 3.7+
   * Django REST Framework 5.1.0+

## Инструкция к запуску:

#### 1. Склонировать репозиторий и открыть папку проекта используя командную строку:

    git clone https://github.com/Zhenia2665/api_yamdb.git
    cd api_yamdb

#### 2. Создать и активировать виртуальное окружение
   
   * GNU/Linux or MacOS:

       ```
       python3 -m venv venv
       ```
       ```
       source venv/bin/activate
       ```
   * Windows:
       ```
       python -m venv venv
       ```
       ```
       source venv/Scripts/activate
       ```

#### 3. Установить необходимые зависимости из `requirements.txt`:

    python -m pip install --upgrade pip
    pip install -r requirements.txt

#### 4. Применить миграции:

    python manage.py migrate

#### 5. Запустить проект:

    python manage.py runserver

#### Все готово! Теперь вы можете использовать возможности проекта!

### Примеры запросов API:
* Создание заголовка под админом `/api/v1/titles/`:
    ```json
    {
      "name": "Titanic",
      "year": 1997,
      "description": "A seventeen-year-old aristocrat falls in love...",
      "genre": [
        "drama",
        "romance"
      ],
      "category": "movie"
    }
    ```
* Получить список разбитый на страницы заголовков определенного жанра и категории  
`/api/v1/titles/?genre={genre_slug}&category={category_slug}`:
    ```json
    {
      "count": 0,
      "next": "string",
      "previous": "string",
      "results": [
        {
          "id": 0,
          "name": "string",
          "year": 0,
          "rating": 0,
          "description": "string",
          "genre": [
            {
              "name": "string",
              "slug": "string"
            }
          ],
          "category": {
            "name": "string",
            "slug": "string"
          }
        }
      ]
    }
    ```
* Оставить новый отзыв как аутентифицированный пользователь`/api/v1/titles/{title_id}/reviews/`:
    ```json
    {
      "text": "string"
    }
    ```
* Оставить комментарий как аутентифицированный пользователь `/api/v1/titles/{title_id}/reviews/{review_id}/comments/`:
    ```json
    {
      "following": "string"
    }
    ```

* Зарегистрировать нового пользователя или получить код подтверждения по электронной почте для существующего пользователя `/api/v1/auth/signup/`:
    ```json
    {
      "username": "my_username",
      "email": "my_email@example.com"
    }
    ```
* Получить токен аутентификации после предоставления кода подтверждения `/api/v1/auth/token/`:
    ```json
    {
      "username": "me_username",
      "confirmation_code": "ab1234-cdefghi567890jklmnopqrstuvwxyz123"
    }
    ```