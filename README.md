[![Requirements Status](https://requires.io/github/lancelote/bike_store/requirements.svg?branch=master)](https://requires.io/github/lancelote/bike_store/requirements/?branch=master)
[![Build Status](https://travis-ci.org/lancelote/bike_store.svg)](https://travis-ci.org/lancelote/bike_store)

# bike_store

Мини-проект "Сайт для обмена велосипедными запчастями" - каталог объявлений о продаже запчастей с одноуровневым
рубрикатором и формой добавления

## Environment Variables

Служебная информация (`SECRET_KEY` и т.д.) хранится в системных переменных. Любая отсутствующая переменная вызовет
исключение `ImproperlyConfigured`. Список обязательных переменных:

| Переменная | Пример | Описание |
| --- | --- | --- |
| `SECRET_KEY` | `z)bvej^e3r23wrg&l7b0!r0p1y%5!*3@&c+-66&)p816yic^h!` | Секретный ключ Django проекта |

## API

- Список запчасей `.../api/list/`
    - Пагинация списка `.../api/list/?page=2`
    - Поиск по названию запчасти/марки `.../api/list/?search=<search-query>`
- Создание новой запчасти `.../api/create/`
- Статистика по маркам с наибольшим числом запчастей `.../api/stats/`

### Примеры

#### Запчасть из списка

```
{
    "name": "Spare Part Name",
    "brand": {
        "name": "Spare Part Name"
    },
    "price": "123",
    "contact": "Tel. 12345"
}
```

#### Марка из списка наиболее популярных

```
{
    "brand": "Spare Part Name",
    "parts_num": 10
}
```

#### Запрос на POST

```
{
    "name": "Spare Part Name",
    "brand": 1,
    "price": "123",
    "contact": "Tel. 12345,
}
```

- Поле `price` опционально, не меньше `0.01` и не больше `999.99`

## Test

- Syntax validation: `python -m pylint bike_store/store/`
- Functional tests: `python3 mysite/manage.py test store`
