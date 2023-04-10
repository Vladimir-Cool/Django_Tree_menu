from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, raise_if_unsaved



class MenuItem(MPTTModel):
    name = models.CharField(max_length=40)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    url = models.CharField(max_length=100)
    level = models.PositiveIntegerField(null=True, blank=True)

    class MPTTMeta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

