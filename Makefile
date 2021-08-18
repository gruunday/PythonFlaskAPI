config: 
	./configure

build:
	./configure
	docker-compose up -d --build

traefik:
	./configure
	docker-compose --file docker-compose-traefik.yml up -d --build

clean:
	rm -rf src/config/
	rm -rf api.keys

local:	
	./configure local
	docker-compose --file docker-compose-traefik-local.yml up -d --build

stop:
	docker-compose down
