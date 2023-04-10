from django import template


from Tree_app.models import MenuItem


register = template.Library()


@register.inclusion_tag('Tree_app/menu.html')
def show_menu(current_url):
    """
    Функция которая собирает QuveriSet для отрисовки меню.
    Нужно было 1 запрос в БД, я не сумел, сроки подходили нужно было как то решать.
    Нужно оптимизировать.

    Исключение нужно для страниц которые не участвуют в дереве меню. как пример '/'
    """

    try:
        root_list = MenuItem.objects.filter(level__exact=0)
        current_item = MenuItem.objects.get(url__exact=current_url[:-1])
        item_ancestors = current_item.get_ancestors(include_self=True)
        item_children = current_item.get_children()
        item_siblings = current_item.get_siblings()
        menu_items = item_ancestors | item_children | item_siblings | root_list

        return {'menu_items': menu_items, 'current_item': current_item}
    except:
        pass
