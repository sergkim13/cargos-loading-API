from fastapi import FastAPI

from cargo_app.api.v1.routes.cargos import router

app = FastAPI(
    title='Cargos API',
    description='Cargos API, powered by FastAPI',
    version='1.0.0',
    docs_url='/docs',
    redoc_url='/redoc',
)
app.include_router(router)
