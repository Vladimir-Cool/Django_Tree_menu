# Django_Tree_menu

Древовидное меню Django. Обучение.

1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django (admin/admin)
5) Активный пункт меню определяется исходя из URL текущей страницы
6) Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.

8) !!! На отрисовку каждого меню Отправляеться 2 запроса в базу данных, и 3 метода Django_MPTT которые, возможно тоже идет в БД, это я пока не изучил

9) На любую страницу меню можно добавить тегом {% show_menu request.path_info %} в тег передаеться url страницы для отрисовки.

