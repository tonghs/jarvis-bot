.PHONY: build publish run test

test:
	sudo docker-compose -f docker-compose.test.yml up

run:
	sudo docker-compose -f docker-compose.yml up

build:
	sudo docker build . -t jarvis
	sudo docker image tag jarvis tonghs/jarvis:latest

publish:
	sudo docker push tonghs/jarvis -a
