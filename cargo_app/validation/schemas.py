from pydantic import BaseModel, Field, validator


class Cargo(BaseModel):
    length: int = Field(gt=0)
    width: int = Field(gt=0)
    height: int = Field(gt=0)
    weight: int = Field(gt=0)


class CoordinatePoint(BaseModel):
    x: int
    y: int


class LoadedCargo(Cargo):
    coordinates: list[CoordinatePoint]

    @validator('coordinates')
    def validate_coordinates(cls, v):
        if len(v) != 4:
            raise ValueError('Number of coordinates should be 4')
        return v


class PayloadResponse(BaseModel):
    loaded_cargos: list[LoadedCargo]
    denied: list[Cargo]
