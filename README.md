# Readthat
Forum for readers to share their experiences. Learning Django as well :D
@ ODAW/UDESC

## Requirements

- Python
- Pip
- MySQL

## Install

``` bash
> pip install django==1.9
> sudo apt-get install libmysqlclient-dev
> pip install mysql
> pip install mysqlclient
```
MySQL:
- Database: readthat
- User: root
- Password: senha

## Run
``` bash
> python manage.py makemigrations core
> python manage.py sqlmigrate core 0001
> python manage.py migrate
> python manage.py runserver
```

- Running at: http://localhost:8000/
