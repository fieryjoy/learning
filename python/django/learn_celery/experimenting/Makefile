build_image:
	docker-compose build

start_container: build_image
	docker-compose up -d

set_broker_url: start_container
	./set_broker_url.sh

start_worker: get_broker_url
	./start_worker.sh

clean:
	find . -name *.pyc | xargs rm
	rmdir __pycache__
