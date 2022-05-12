clean:
	docker-compose down && docker rmi $$(docker images -a -q) && docker volume prune && docker-compose up -d

log:
	docker-compose logs -f

up:
	docker-compose up -d && docker ps

reset:
	docker-compose down && docker-compose up -d && docker-compose up -d && docker ps