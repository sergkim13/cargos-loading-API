install:
	poetry install

dev:
	poetry run uvicorn cargo_app.main:app --reload

test:
	poetry run pytest -vv

compose:
	docker compose up -d

stop:
	docker compose down

compose-test:
	docker compose -f docker-compose.test.yaml -p testing up -d

stop-test:
	docker compose -f docker-compose.test.yaml -p testing down