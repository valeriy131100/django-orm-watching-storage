# django-orm-watching-storage
Пульт охраны выполненный в виде сайта

# Установка
Вам понадобится установленный Python 3 и git

Склонируйте репозиторий
```bash
$ git clone https://github.com/valeriy131100/django-orm-watching-storage
```

Создайте в этой папке виртуальное окружение
```bash
$ python3 -m venv [полный путь до папки django-orm-watching-storage]
```

Активируйте виртуальное окружение и установите зависимости
```bash
$ cd django-orm-watching-storage
$ source bin/activate
$ pip install -r requirements.txt
```
# Использование
Заполните прилагающийся .env.example файл и переименуйте его в .env или иным образом задайте переменные среды:
* DB_HOST - хост с базой данных
* DB_PORT - порт
* DB_NAME - имя базы данных
* DB_USER - пользователь базы данных
* DB_PASS - пароль пользователя
* DEBUG - запускать ли сервер в режиме отладки, True/False

Перейдите в директорию программы и исполните
```bash
$ bin/python manage.py runserver 0.0.0.0:8000
```
Пульт охраны будет доступен по указаному адресу. Вы можете указать свой адрес и порт.