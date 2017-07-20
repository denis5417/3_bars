# Ближайшие бары

Скрипт расчитывает
1. Самый большой бар
2. Самый маленький бар
3. Самый близкий бар

Работает с данными [отсюда](https://apidata.mos.ru/v1/datasets/1796/rows?api_key=e1a2169e5e05bdbcf1b768af34764fd7)

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5 и библиотеку [geopy](https://github.com/geopy/geopy)

Установка библиотеки:

```#!bash
pip install -r requirements.txt
```

Запуск на Linux:

```#!bash

$ python3 bars.py <path_to_file_with_JSON_data> <longitude> <latitude>
Самый большой бар – Спорт бар «Красная машина»
Самый маленький бар - БАР. СОКИ
Самый близкий бар – Таверна


```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
