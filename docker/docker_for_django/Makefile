build:
	docker-compose build --no-cache

start_db:
	docker-compose up db

start_web:
	docker-compose up web

start_shell:
	docker exec -i -t dockerfordjango_web_1 /bin/bash

stop:
	docker-compose stop

kill:
	docker-compose kill

remove_containers:
	docker-compose rm --force
