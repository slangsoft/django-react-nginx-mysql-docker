# django-react-nginx-mysql-docker

## Modify the time for wait.sh

Modify the timeout seconds in `frontend/nginx/wait.sh` if the frontend nginx server starts earlier than react. (e.g. 15 -> 120)

```bash
WAITFORIT_TIMEOUT=${WAITFORIT_TIMEOUT:-15}
```

## create `backend/web-back/.env` just for development

```text
SECRET_KEY='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
DEBUG=False
HOST=db
USER=user
```

## migration for database

```bash
docker-compose run --rm web-back sh -c "python manage.py makemigrations"
```

```bash
docker-compose run --rm web-back sh -c "python manage.py migrate"
```

## create superuser

```bash
docker-compose run --rm web-back sh -c "python manage.py createsuperuser"
```

## collectstatic

```bash
docker-compose run --rm web-back sh -c "python manage.py collectstatic"
```

## add packages

```bash
docker-compose run --rm web-front sh -c "yarn install"
```

## run server

```bash
docker-compose up --build
```
