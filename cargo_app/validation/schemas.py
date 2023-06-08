from pydantic import BaseModel, validator


class Cargo(BaseModel):
    length: int
    width: int
    height: int
    weight: int


class CoordinatePoint(BaseModel):
    x: int
    y: int
    z: int


class LoadedCargo(BaseModel):
    cargo: Cargo
    coordinates: list[CoordinatePoint]

    @validator('coordinates')
    def validate_coordinates(cls, v):
        if len(v) != 8:
            raise ValueError('Number of coordinates should be 8')
        return v


class PayloadResponse(BaseModel):
    loaded_cargos: list[LoadedCargo]
    denied: list[Cargo]
