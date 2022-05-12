clean:
	docker-compose down && docker rmi $$(docker images -a -q) && docker volume prune && docker-compose up -d
