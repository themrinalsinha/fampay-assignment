default: run

setup:
	@docker-compose build

run:
	@docker-compose up --build --remove-orphans

cli:
	@docker-compose exec webapp /bin/bash

shell:
	@docker-compose exec webapp python manage.py shell_plus

syncdb:
	@docker-compose exec webapp python manage.py makemigrations
	@docker-compose exec webapp python manage.py migrate

stop:
	@docker-compose stop

psql:
	@docker-compose exec db psql -U fampay

user:
	@docker-compose exec webapp python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@fampay.in', 'admin')"
