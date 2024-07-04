from  .views import index, table, staticLayout, charts, login, register
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('table', table, name='table'),
    path('static-layout', staticLayout, name='static-layout'),
    path('charts', charts, name='charts'),
]