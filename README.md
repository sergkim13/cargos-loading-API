# Cargos-loading API (FastApi)


### Description:
API endpoint which allows you to load given cargos into truck with best max weight combination. See 'Task description' for more info.


### Requirements:
1. MacOS (prefer) / Linux / Windows10
2. `Docker`
3. `Make` utily for MacOS, Linux.

### Install:
1. Clone repository: https://github.com/sergkim13/cargos-loading-API
2. Type `make compose` for running application in docker container. App will be running at http://0.0.0.0:8000. See docs at http://0.0.0.0:8000/docs after starting app. Type `make stop` to stop app container.
3. Type `make compose-test` for running tests in docker container. Type `make stop-test` to stop app container.


### Task description
<details>
    <summary>Click to show</summary>
Предположим, что данные прилетают через POST-запрос в JSON-формате.
 
В кузов автомашины (длиной L, шириной W, высотой H и погрузочной массой M) необходимо равномерно по осям подгрузить N грузов, каждый из которых имеет свою длину, ширину, высоту и массу.
 
Параметры кузова (L, W, H и М) сделать константами,
количество грузов (N) , а также их длина, высота и ширина передается через передачу JSON-файла.

Если суммарный вес грузов превышает погрузочную массу, то необходимо загрузить оптимально (по максимальной массе размещенных грузов).
 
Внимание. Грузы размещаются в один ярус(!!!). Допуск примыкания груза 5 см по всем измерениям.
 
На выходе программа формирует JSON-файл, как расположены грузы в исходном JSON-файл добавляются координаты для каждого груза. Если имеются грузы, которые не могут быть погружены в силу ограничений кузова, то необходимо поместить их в поле-массив denied.
</details>
