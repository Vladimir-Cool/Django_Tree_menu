from django.urls import path
from .views import *

'/'
urlpatterns = [
    path('', TreeView.as_view(), name='root'),
    path('1/', TreeLevelOneView.as_view(), name='1/'),
    path('1/1/', TreeLevelOneView.as_view(), name='1/1/'),
    path('1/1/1/', TreeLevelOneView.as_view(), name='1/1/1/'),
    path('1/2/', TreeLevelOneView.as_view(), name='1/2/'),
    path('1/2/1/', TreeLevelOneView.as_view(), name='1/2/1/'),
    path('1/2/2/', TreeLevelOneView.as_view(), name='1/2/2/'),
    path('1/2/3/', TreeLevelOneView.as_view(), name='1/2/3/'),
    path('1/3/', TreeLevelOneView.as_view(), name='1/3/'),
    path('1/3/1/', TreeLevelOneView.as_view(), name='1/3/1'),
    path('2/', TreeLevelOneView.as_view(), name='2/'),
    path('2/1/', TreeLevelOneView.as_view(), name='2/1/'),
    path('2/2/', TreeLevelOneView.as_view(), name='2/2/'),
    path('2/2/1/', TreeLevelOneView.as_view(), name='2/2/1'),
    path('2/2/2/', TreeLevelOneView.as_view(), name='2/2/2'),
    path('2/2/3/', TreeLevelOneView.as_view(), name='2/2/3'),
    path('2/3/', TreeLevelOneView.as_view(), name='2/3/'),
]