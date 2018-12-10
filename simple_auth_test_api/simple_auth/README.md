## Getting started

#### install Postgres DB

```
$ sudo docker stack deploy -c stack.yml postgres
```
<small>for more detail, see [Docker Hub Page](https://hub.docker.com/_/postgres/)</small>

#### python django
```
$ pip install -r requirement.pip
$ python manage.py migrate  # create default tables and some superusers
$ python manage.py runserver
```
