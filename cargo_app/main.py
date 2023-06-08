from fastapi import FastAPI


app = FastAPI(
    title='Cargos API',
    description='Cargos API, powered by FastAPI',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redoc',
)
