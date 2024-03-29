# Разработка онлайн платформу торговой сети электроники.

# Технические требования:

- Python 3.8+
- Django 3+
- DRF 3.10+
- PostgreSQL 10+

# Задание:

- Создайте веб-приложение, с API интерфейсом и админ-панелью.
- Создайте базу данных используя миграции Django.

# Требования к реализации:

1) Необходимо реализовать модель сети по продаже электроники.
   Сеть должна представлять собой иерархическую структуру из 3 уровней:

- Завод;
- Розничная сеть;
- Индивидуальный предприниматель.

Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии).
Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети,
т.е. завод всегда находится на 0 уровне, а если розничная сеть относится напрямую к заводу,
минуя остальные звенья - её уровень - 1.

2) Каждое звено сети должно обладать следующими элементами:

- Название;

- Контакты:  
  - Email;  
  - Страна;  
  - Город;  
  - Улица;  
  - Номер дома;
- Продукты:  
  - Название;  
  - Модель;  
  - Дата выхода продукта на рынок;
- Поставщик (предыдущий по иерархии объект сети);
- Задолженность перед поставщиком в денежном выражении с точностью до копеек;
- Время создания (заполняется автоматически при создании).

3) Сделать вывод в админ-панели созданных объектов  
- На странице объекта сети добавить:  
     - ссылку на «Поставщика»;    
     - фильтр по названию города;  
- «admin action», очищающий задолженность перед поставщиком у выбранных объектов.

4) Используя DRF, создать набор представлений:
- CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед поставщиком»);
- Добавить возможность фильтрации объектов по определенной стране.  

5) Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.

# Запуск проекта:
- Клонируйте репозиторий с проектом:
git clone

- В созданной директории установите виртуальное окружение, активируйте его и установите необходимые зависимости:
    - python3 -m venv venv
    - source venv/bin/activate для Linux
    - venv\Scripts\activate для Windows
    - pip install -r requirements.txt

- Создайте свою базу данных psql -U postgres / CREATE DATABASE

- Выполните миграции: python manage.py migrate

- Создайте суперпользователя: python manage.py createsuperuser

- Запустите сервер: python manage.py runserver

- Ваш проект запустился на http://127.0.0.1:8000/
- Примеры запросов в файле Sales network API.postman_collection.json
