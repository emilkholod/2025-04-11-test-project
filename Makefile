.PHONY: setup build up down test sh prod

setup:
	@if [ ! -f .env ]; then cp .env.template .env; fi

# Build the Docker images defined in docker-compose.yml
build:
	docker-compose build

# Start the containers defined in docker-compose.yml
up:
	docker-compose run --rm app

# Down the containers defined in docker-compose.yml
down:
	docker-compose down --remove-orphans

# Run tests inside the 'app' service using pytest with verbose output
test:
	docker-compose run --rm app pytest -v

# Open a shell inside the 'app' service container
sh:
	docker-compose run --rm app sh

# Build prod image and then you can push to docker repository
# TODO:
prod:
