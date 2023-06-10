install:
	poetry install

dev:
	poetry run uvicorn cargo_app.main:app --reload
