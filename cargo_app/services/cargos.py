from math import ceil
from config import (
    TRUCK_LENGTH,
    TRUCK_WIDTH,
    TRUCK_HEIGHT,
    TRUCK_CAPACITY,
    TRUCK_AREA,
    GAP,
)

from cargo_app.validation.schemas import Cargo, CoordinatePoint, LoadedCargo, PayloadResponse


class CargoService:
    """Service class which provides operations with cargos."""

    def load_cargos(self, cargos: list[Cargo]) -> PayloadResponse:
        """Loads given cargos into car and returns loaded and denied cargos."""
        loaded_cargos = []
        denied_cargos = []
        cargos.sort(key=lambda c: c.weight, reverse=True)
        cargos, denied_by_dimensions = self.filter_cargos(cargos)
        denied_cargos.extend(denied_by_dimensions)

        cargo_weights = [cargo.weight for cargo in cargos]
        cargo_areas = [ceil((cargo.length + 5) * (cargo.width + 5)) for cargo in cargos]
        total_cargos_weight = sum(cargo_weights)
        total_cargos_area = sum(cargo_areas)
        best_cargos = cargos
        if total_cargos_weight > TRUCK_CAPACITY and total_cargos_area <= TRUCK_AREA:
            best_cargos, not_fitted_cargos = self.find_best_combination(
                cargos, cargo_weights, cargo_areas, total_cargos_area
            )
            denied_cargos.extend(not_fitted_cargos)
        elif total_cargos_weight <= TRUCK_CAPACITY and total_cargos_area > TRUCK_AREA:
            best_cargos, not_fitted_cargos = self.find_best_combination(
                cargos, cargo_weights, cargo_areas, TRUCK_AREA
            )
            denied_cargos.extend(not_fitted_cargos)
        elif total_cargos_weight > TRUCK_CAPACITY and total_cargos_area > TRUCK_AREA:
            best_cargos, not_fitted_cargos = self.find_best_combination(
                cargos, cargo_weights, cargo_areas, TRUCK_AREA
            )
            denied_cargos.extend(not_fitted_cargos)
        if best_cargos:
            loaded_cargos.extend(self.pack_cargos(best_cargos))

        return PayloadResponse(
            loaded_cargos=loaded_cargos,
            denied=denied_cargos,
        )

    def find_best_combination(self, cargos: list[Cargo], weights: list[int],
                              areas: list[int], max_area: int) -> tuple[list[Cargo]]:
        """
        Find best combination of cargos with max summary weight which can fit in max_area.
        Using dynamic programming algorythm.
        """
        table = self.build_table(weights, areas, max_area)
        return self.get_best_combination(table, cargos, weights, areas, max_area)

    def build_table(self, weights: list[int], areas: list[int], max_area: int) -> list[list]:
        """Creates and fills in table for dynamic programming algorythm."""
        cargos_count = len(weights)
        table = [[0] * (max_area + 1) for _ in range(cargos_count + 1)]

        for line in range(1, cargos_count + 1):
            for column in range(1, max_area + 1):
                if areas[line - 1] <= column:
                    table[line][column] = max(
                        table[line - 1][column],
                        weights[line - 1] + self._estimate_increment(
                            weights[line - 1],
                            table[line - 1][column - areas[line - 1]]
                        )
                    )
                else:
                    table[line][column] = table[line - 1][column]
        print('LAST COLUMN', column)
        return table

    def get_best_combination(self, table: list[list], cargos: list[Cargo],
                             weights: list[int], areas: list[int], max_area: int) -> tuple[list[Cargo]]:
        """
        Returns best combination cargos and denied cargos.
        """
        best_cargo_indexes = []
        cargos_count = len(cargos)
        current_weight = table[cargos_count][max_area]
        a = max_area
        for i in range(cargos_count, 0, -1):
            if current_weight <= 0:
                break
            if current_weight == table[i-1][a]:
                continue
            else:
                best_cargo_indexes.append(i-1)
                current_weight -= weights[i-1]
                a -= areas[i-1]
        best_cargos = [cargo for i, cargo in enumerate(cargos) if i in best_cargo_indexes]
        denied_cargos = [cargo for i, cargo in enumerate(cargos) if i not in best_cargo_indexes]
        return best_cargos, denied_cargos

    def pack_cargos(self, cargos: list[Cargo]) -> list[LoadedCargo]:
        """Places best combination cargos into a truck and add coordinates."""
        loaded_cargos = []
        cargos.sort(key=lambda c: c.length, reverse=True)
        level_length = GAP + cargos[0].length
        x, y = 0, 0
        for cargo in cargos:
            if x + cargo.width > TRUCK_WIDTH:
                x = 0
                y = level_length
                level_length += GAP + cargo.length
            loaded_cargos.append(
                LoadedCargo(
                    length=cargo.length,
                    width=cargo.width,
                    height=cargo.height,
                    weight=cargo.weight,
                    coordinates=[
                        CoordinatePoint(x=x, y=y),
                        CoordinatePoint(x=x, y=y+cargo.length),
                        CoordinatePoint(x=x+cargo.width, y=y),
                        CoordinatePoint(x=x+cargo.width, y=y+cargo.length),
                    ])
            )
            x += GAP + cargo.width

        return loaded_cargos

    def _estimate_increment(self, arg1: int, arg2: int):
        """Controls that summary of arguments lower than truck capacity."""
        return arg2 if (arg1 + arg2) <= TRUCK_CAPACITY else 0

    def filter_cargos(self, cargos: list[Cargo]) -> tuple[list[Cargo]]:
        """
        Compares cargo's size and weight with truck's size and weight.
        Returns two lists: filtered and denied cargos.
        """
        filtered_cargos = cargos[:]
        denied = []
        for cargo in cargos:
            if (
                cargo.height > TRUCK_HEIGHT or
                (cargo.length > TRUCK_LENGTH and cargo.length > TRUCK_WIDTH) or
                (cargo.width > TRUCK_LENGTH and cargo.width > TRUCK_WIDTH) or
                cargo.weight > TRUCK_CAPACITY
            ):
                filtered_cargos.remove(cargo)
                denied.append(cargo)

        return filtered_cargos, denied


def get_cargo_service() -> CargoService:
    """Returns a `CargoService` instance."""
    return CargoService()
