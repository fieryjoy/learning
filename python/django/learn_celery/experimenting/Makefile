build_image:
	docker-compose build

start_servers: build_image
	docker-compose up -d

start_worker:
	BROKER_URL=amqp://admin:mypass@`docker inspect -f '{{.NetworkSettings.Networks.experimenting_default.IPAddress}}' experimenting_rabbitmq_1`// BACKEND_URL=redis://`docker inspect -f '{{.NetworkSettings.Networks.experimenting_default.IPAddress}}' experimenting_redis_1` ./start_worker.sh

test_chord:
	BROKER_URL=amqp://admin:mypass@`docker inspect -f '{{.NetworkSettings.Networks.experimenting_default.IPAddress}}' experimenting_rabbitmq_1`// BACKEND_URL=redis://`docker inspect -f '{{.NetworkSettings.Networks.experimenting_default.IPAddress}}' experimenting_redis_1` python3 test_chord.py


clean: stop_servers
	find . -name *.pyc | xargs rm
	rmdir __pycache__

stop_servers:
	docker-compose down
