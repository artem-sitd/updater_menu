### Быстрый старт

1.
2.
3. ыв

### Требования тз:
| №  | Задача :                                                                                                                                           | Решение:             |
|----|----------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| 1  | Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:                                                |                      |
| 2  | Меню реализовано через template tag                                                                                                                |                      |
| 3  | Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.                                    |                      |
| 4  | Хранится в БД.                                                                                                                                     | используется sqlite3 |
| 5  | Редактируется в стандартной админке Django                                                                                                         | есть                 |
| 6  | Активный пункт меню определяется исходя из URL текущей страницы                                                                                    |                      |
| 7  | Меню на одной странице может быть несколько. Они определяются по названию.                                                                         |                      |
| 8  | При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.                        |                      |
| 9  | На отрисовку каждого меню требуется ровно 1 запрос к БД                                                                                            |                      |
| 10 |  Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию. |                      |
| 11 |  {% draw_menu 'main_menu' %}                                                                                                                       |                      |
| 12 |  При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.                                           |                      |



