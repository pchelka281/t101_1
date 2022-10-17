# Лабораторная работа №1
## Старт
* Чтобы собрать Docker образ в текущей директории нужно использовать команду
```bash
[sudo] docker build -t <name> .
``` 
* Дабы запустить Docker-контейнер по уже существующему образу используем следующую команду:
```bash
[sudo] docker run -it --rm <name>
```
Флаг **--rm** нуден для удаления контейнера после завершения работы скрипта

## Описание алгоритма

1. Генерируются факты и правила.

2. Правила приводятся к более удобному виду.
Правила имеют вид:
```
[ { if:{'operand : [numbers]'},then: number}, ...]
```

Факты сортируются в **3** отдельных массива по логическому операнду
```
[ [ [if], then ], ...]
```

3. Приводим факты к человекочитаемому виду. Факты содержатся в массиве, а так как мы хотим избежать прогона по всему массиву и повтора фактов, помещаем их в словарь.
```
**{ number:True }**,
```
если number -, то метод **get()** возвращает *None*

4. Запускается скрипт для проверки фактов. 

* При проверке правила **OR** ищем **хотя бы одно совпадение** условия и факт ---> добавляем в базу знаний. 

* При проверке правила **AND** ищем **хотя бы одно несовпадение** условия и факта ---> не добавляем в базу знаний.
 
* При проверке праила **NOT** ищем **хотя бы одно совпадение** условия и факта ---> не добавляем в базу знаний. 

5. При помощи обёртки **timer()** замеряем время работы.
