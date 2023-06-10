from config import TRUCK_LENGTH, TRUCK_WIDTH, TRUCK_HEIGHT, TRUCK_CAPACITY

from cargo_app.validation.schemas import Cargo, LoadedCargo, PayloadResponse


class CargoService:
    """Service class which provides operations with cargos."""
    def __init__(
            self,
    ) -> None:
        """Inits `CargoService` instance."""
        self.TRUCK_AREA = TRUCK_LENGTH * TRUCK_WIDTH

    async def load_cargos(self, cargos: list[Cargo]):
        """Loads given cargos into car and returns loaded and denied cargos."""
        denied_cargos = []
        cargos.sort(key=lambda c: c.weight, reverse=True)
        cargos, denied = self.filter_cargos(cargos)
        if denied:
            denied_cargos.append(denied)

        cargo_weights = [cargo.weight for cargo in cargos]
        cargo_areas = [cargo.length * cargo.width for cargo in cargos]
        total_cargos_weight = sum(cargo_weights)
        total_cargos_area = sum(cargo_areas)
        best_weight = total_cargos_weight
        best_cargos = cargos
        print('TRUCK_CAPACITY', TRUCK_CAPACITY)
        print('TRUCK_AREA', self.TRUCK_AREA)
        print(total_cargos_weight)
        print(total_cargos_area)
        if total_cargos_weight > TRUCK_CAPACITY and total_cargos_area <= self.TRUCK_AREA:
            print('SWITCH 1')
            best_weight, best_cargos, denied = await self.find_best_combination(cargos, cargo_weights, cargo_areas, total_cargos_area)
        elif total_cargos_weight <= TRUCK_CAPACITY and total_cargos_area > self.TRUCK_AREA:
            print('SWITCH 2')
            best_weight, best_cargos, denied = await self.find_best_combination(cargos, cargo_weights, cargo_areas, self.TRUCK_AREA)
        elif total_cargos_weight > TRUCK_CAPACITY and total_cargos_area > self.TRUCK_AREA:
            print('SWITCH 3')
            best_weight, best_cargos, denied = await self.find_best_combination(cargos, cargo_weights, cargo_areas, self.TRUCK_AREA)
        denied_cargos.append(denied)
        return best_weight, best_cargos, denied_cargos

    async def find_best_combination(self, cargos: list[Cargo], weights: list[int], areas: list[int], max_area: int):
        table = self.build_table(weights, areas, max_area)
        return self.get_best_combination(table, cargos, weights, areas, max_area)

    def build_table(self, weights: list[int], areas: list[int], max_area: int) -> list[list]:
        cargos_count = len(weights)
        # Создаем таблицу размером (n+1) x (capacity+1)
        table = [[0] * (max_area + 1) for _ in range(cargos_count + 1)]

        # Заполняем таблицу
        for line in range(1, cargos_count + 1):
            for column in range(1, max_area + 1):
                if areas[line - 1] <= column:
                    table[line][column] = max(
                        table[line - 1][column],
                        weights[line - 1] + self.estimate_increment(
                            weights[line - 1],
                            table[line - 1][column - areas[line - 1]]
                        )
                    )
                else:
                    table[line][column] = table[line - 1][column]
        print('LAST COLUMN', column)
        return table

    def get_best_combination(self, table: list[list], cargos: list[Cargo],
                             weights: list[int], areas: list[int], max_area: int):
        # Определяем оптимальную комбинацию
        best_cargo_indexes = []
        cargos_count = len(cargos)
        best_weight = table[cargos_count][max_area]
        a = max_area
        res = best_weight
        for i in range(cargos_count, 0, -1):
            if res <= 0:
                break
            if res == table[i-1][a]:
                continue
            else:
                best_cargo_indexes.append(i-1)
                res -= weights[i-1]
                a -= areas[i-1]
        best_cargos = [cargo for i, cargo in enumerate(cargos) if i in best_cargo_indexes]
        denied_cargos = [cargo for i, cargo in enumerate(cargos) if i not in best_cargo_indexes]
        return best_weight, best_cargos, denied_cargos

    def estimate_increment(self, arg1: int, arg2: int):
        return arg2 if (arg1 + arg2) <= TRUCK_CAPACITY else 0

    def filter_cargos(self, cargos: list[Cargo]) -> tuple[list[Cargo]]:
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
    return CargoService()
