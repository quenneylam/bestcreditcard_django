up:
	docker-compose up -d

down: 
	docker-compose down

restart: down up

container-list: 
	docker-compose ps
