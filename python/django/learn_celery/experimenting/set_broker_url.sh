export BROKER_URL=amqp://admin:mypass@`docker inspect -f '{{.NetworkSettings.Networks.experimenting_default.IPAddress}}' experimenting_rabbitmq_1`//
