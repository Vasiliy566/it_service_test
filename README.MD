[![Build Status](https://travis-ci.com/Vasiliy566/it_service_test.svg?branch=main)](https://travis-ci.com/Vasiliy566/it_service_test)
### Основная часть
- [x] - Rest-api сервис с использованием flask
- [x] - Поиск кратчайшего пути в графе (длинна пути + сам путь) использовал свой же код, который немного модифицировал ( https://github.com/Vasiliy566/PolitekhArchive/tree/master/Dejkstra )
- [x] - Обработка ошибок 
- [x] - Авторизация по X-API-KEY ( 123321 )
### Дополнительная часть
- [x] - Упаковка в Docker
- [x] - Покрыть тестами (correctness)
- [ ] - Покрыть тестами (performance)
#### Было бы неплохо:
- [ ] - Кэшировать посчитанные пути (Redis, cachetools, ..)
- [ ] - Асинхронно считать Флойдом все расстояния, так же кэшировать
- [ ] - Сравнить performance
