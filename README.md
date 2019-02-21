# Django-Library

### Installation & Setup

```sh
$ git clone https://github.com/jaselnik/Django-Library.git
$ cd Django-Library
```
```sh
$ sudo -u postgres psql postgres
=# CREATE DATABASE library_db;
```
```sh
$ virtualenv venv
$ source venv/bin/activate 
```
```sh
(venv) $ pip install -r requirements.txt
(venv) $ python manage.py migrate
(venv) $ python manage.py loaddata fixtures/initial_data.json
(venv) $ python manage.py runserver 0.0.0.0:8090
```

### FrontEnd!

- [Local Home](http://127.0.0.1:8090) or [Server Home](http://68.183.75.150:8090)
- [Local User-Library](http://127.0.0.1:8090/lib/1/) or [Server User-Library](http://68.183.75.150:8090/lib/1/)
- [Local Book-Edit](http://127.0.0.1:8090/book/3/edit/) or [Server Book-Edit](http://68.183.75.150:8090/book/3/edit/)

### REST API!

- [Local Home](http://127.0.0.1:8090/api/) or [Server Home](http://68.183.75.150:8090/api/)
- [Local User-Library](http://127.0.0.1:8090/lib/1/) or [Server User-Library](http://68.183.75.150:8090/api/lib/1/)
- [Local Book-Edit](http://127.0.0.1:8090/api/book/3/edit/) or [Server Book-Edit](http://68.183.75.150:8090/api/book/3/edit/)
