## Тестовое задание "Сарафан"

#### Задание №1: 
запустить task_1/main.py

#### Задание №2:
#### Установка

1. Склонируйте репозиторий:
```
git clone https://github.com/Shebelnitskii/test_task_sarafan.git
```

2. Перейдите в каталог проекта:
```
cd task_2/product_shop
```

3. Установите зависимости:
``` 
pip install -r requirements.txt
```

4. Запуск сервера
- Примените миграции:
```
python manage.py migrate
```
- Запустите сервер:
```
python manage.py runserver
```
5. Сервер готов к работе

#### Использование API
- Создайте учетную запись пользователя:
```
POST http://127.0.0.1:8000/users/create/
```
```
{
    "email": "your_email@example.com",
    "password": "your_password"
}
```
- Получите токен аутентификации:
```
POST http://127.0.0.1:8000/users/token/
```
```
{
    "username": "your_username",
    "password": "your_password"
}
```
- Используйте полученный токен( "access") для аутентификации в других запросах("Bearer Token").

- Используйте различные эндпоинты API для работы с товарами, корзиной и другими сущностями магазина.
```http://127.0.0.1:8000/redoc/```  - здесь можно посмотреть документацию по API(после запуска сервера)