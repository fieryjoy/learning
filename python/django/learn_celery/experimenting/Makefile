build_image:
	docker-compose build

start_rabbitmq: build_image
	docker-compose up -d

start_worker:
	BROKER_URL=amqp://admin:mypass@`docker inspect -f '{{.NetworkSettings.Networks.experimenting_default.IPAddress}}' experimenting_rabbitmq_1`// ./start_worker.sh

clean: stop_all
	find . -name *.pyc | xargs rm
	rmdir __pycache__

stop_rabbitmq:
	docker-compose stop
