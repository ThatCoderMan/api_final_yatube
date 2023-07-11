# YaTube API

![workflows](https://github.com/ThatCoderMan/api_final_yatube/actions/workflows/workflow.yml/badge.svg)

<details>
<summary>Project stack</summary>

- Python 3.7
- Django 2.2
- Django REST Framework 
- Djoser 
- GitHub Actions

</details>

## Описание 
API для проекта "YaTube". Сайт "YaTube" - это онлайн-сервис для публикации, получения 
записей, комментирования записей других пльзователей и подписки на авторов.

### Инструкция по запуску:
Клонируйте репозиторий:
```commandline
git clone git@github.com:ThatCoderMan/foodgram-project-react.git
```
Установите и активируйте виртуальное окружение:

- *для MacOS:*
    ```commandline
    python3 -m venv venv
    ```
- *для Windows:*
    ```commandline
    python -m venv venv
    source venv/bin/activate
    source venv/Scripts/activate
    ```
Установите зависимости из файла requirements.txt:
```commandline
pip install -r requirements.txt
```
Перейти в папку yatube_api/
```commandline
cd yatube_api/
```
Примените миграции:
```commandline
python manage.py migrate
```
В папке с файлом manage.py выполните команду для запуска локально:
```commandline
python manage.py runserver
```
Документация к проекту доступна по адресу:
```
http://127.0.0.1:8000/redoc/
```

## Примеры работы API

Создание, изменение, удаление публиакаций; 
добавление, изменение, удаление комментариев; 
получение списка подсписок и подписка на пользователей 
доступно только для _авторизованных пользователей_.

Редактировать, удалять публикации и комментарии может только 
_автор публикации или комментария_.

### Получение публикаций
Пагинация при помощи параметров offset и limit
> GET /api/v1/posts/
 
response: [{id: int; author: str; text: str; pub_date: str <date-time>; 
image: str binary; group: int}]

### Создание публикации
> POST /api/v1/posts/
 
body: {text: str; image: str binary; group: int}

### Получение публикации
> GET /api/v1/posts/{id}/
 
response: {id: int; author: str; text: str; pub_date: str <date-time>; 
image: str binary; group: int}

### Обновление публикации
#### Полное обновление публикации
> PUT /api/v1/posts/{id}/

body: {text: str; image: str binary; group: int}

#### Частичное обновление публикации
> PATCH /api/v1/posts/{id}/

body: {text: str; image: str binary; group: int}

### Удаление публикации
> DEL /api/v1/posts/{id}/

### Получение комментариев
> GET /api/v1/posts/{post_id}/comments/

response: [{id: int; author: str; text: str, created: str <date-time>; 
post: int}]
  
### Добавление комментария
> POST /api/v1/posts/{post_id}/comments/

body: {text: str}

### Получение комментария
> GET /api/v1/posts/{post_id}/comments/{id}/

response: {id: int; author: str; text: str, created: str <date-time>; 
post: int}

### Обновление комментария
> PUT /api/v1/posts/{post_id}/comments/{id}/
> PATCH /api/v1/posts/{post_id}/comments/{id}/

body: {text: str}

### Удаление комментария
> DEL /api/v1/posts/{post_id}/comments/{id}/

### Список сообществ
> GET /api/v1/groups/

response: [{id: int; title: str; slug: str; description: str}]

### Информация о сообществе
> GET /api/v1/groups/{id}/

response: {id: int; title: str; slug: str; description: str}

### Подписоки на пользователей
поиск при помощи параметра search
> GET /api/v1/follow/

response: [{user: str; following: str}]

### Подписаться на пользователя
>POST /api/v1/follow/

body: {following: str}

### Получить JWT-токен
> POST /api/v1/jwt/create/

body: {username: str; password: str}
response: {refresh: str; access: str}

### Обновить JWT-токен
> POST /api/v1/jwt/refresh/

body: {refresh: str}
response: {access: str}

### Проверить JWT-токен
> POST /api/v1/jwt/verify/

body: {token: str}

### Автор проекта:

[Artemii Berezin](https://github.com/ThatCoderMan)
