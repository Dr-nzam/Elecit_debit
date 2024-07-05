from  .views import (index, table, staticLayout,
                      charts, login, register, erro401,
                        erro404, erro500, changerPassword)
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('table', table, name='table'),
    path('static-layout', staticLayout, name='static-layout'),
    path('charts', charts, name='charts'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('error401', erro401, name='error401'),
    path('error404', erro404, name='error404'),
    path('error500', erro500, name='error500'),
    path('changer-password', changerPassword, name='changer-password'),
]