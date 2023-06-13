from fastapi import APIRouter, Depends, status
from cargo_app.services.cargos import CargoService, get_cargo_service

from cargo_app.validation.schemas import Cargo, PayloadResponse


router = APIRouter(
    prefix='/api/v1/cargos',
    tags=['cargo'],
)


@router.post(
    path='/load',
    status_code=status.HTTP_200_OK,
    response_model=PayloadResponse,
    summary='Погрузка грузов в кузов автомобиля',
)
async def load_cargos(
    cargos: list[Cargo],
    cargo_service: CargoService = Depends(get_cargo_service),
) -> PayloadResponse:
    """
    Loads given cargos into car and returns loaded and denied cargos.

    :param cargos: list of cargos with given length, width, height in centimeters
    and weight in kilograms
    :param cargo_service: service class which provides operations with cargos.
    """
    return cargo_service.load_cargos(cargos=cargos)
