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
Заполните прилагающийся project/settings.py.exapmle файл и переименуйте его в settings.py

Перейдите в директорию программы и исполните
```bash
$ bin/python main.py
```
Пульт охраны будет доступен по адресу 127.0.0.1:8000