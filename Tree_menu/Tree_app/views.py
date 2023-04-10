from django.shortcuts import render
from django.views.generic import View


from .models import MenuItem


class TreeView(View):
    """
    Класс отрисовки всего дерева, для просмотра.
    """
    def get(self, request):
        menu_data = MenuItem.objects.all()
        return render(request, 'Tree_app/menu.html', context={'menu_items': menu_data})


class TreeLevelOneView(View):
    """
    Пример класса для просмторта любых страниц.
    Дерево Меню отрисовываеться исходя из url страницы.
    """
    def get(self, request):
        return render(request, 'Tree_app/index.html', )

