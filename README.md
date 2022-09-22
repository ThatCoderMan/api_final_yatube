# **YaTube API**

### технологии в проекте
- Python 3.7
- Django 2.2.16
- Django rest framework 3.12.4
- Djoser 2.1.0

## Описание 
API для проекта YaTube с возможностями публиковать, получать записи; 
комментировать записи; подписываться на авторов.

## Установка 
- Клонировать репозиторий с GitHub и перейти в него
    ~~~
    git clone https://github.com/ThatCoderMan/api_final_yatube.git
    cd api_final_yatube
  ~~~
- Создать и активировать виртульное окружение, 
установить зависимости из файла requirements.txt
    ~~~
    python -m venv venv
    venv/Scripts/activate
    pip install -r requirements.txt
    ~~~
- Выполнить миграции
    ~~~
    python yatube_api/manage.py migrate
    ~~~
- Запустить сервер 
    ~~~
    python yatube_api/manage.py runserver
    ~~~
  
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

#### Автор: [Артемий Березин](https://github.com/ThatCoderMan)