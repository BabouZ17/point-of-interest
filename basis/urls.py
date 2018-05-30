from django.urls import path

from . import views

app_name = 'basis'

urlpatterns = [
    path('', views.home, name='home'),
    path('board', views.board, name='board'),
    path('categories', views.categories, name='categories'),
    path('countries', views.countries, name='countries'),
    path('contact', views.contact, name='contact'),
]
