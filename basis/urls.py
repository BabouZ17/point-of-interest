from django.urls import path

from . import views

app_name = 'basis'

urlpatterns = [
    path('', views.home, name='home'),
    path('board', views.board, name='board'),
    path('pois', views.pois, name='pois'),
    path('category/<int:id>', views.category, name='category'),
    path('category/<int:id>/pointofinterests', views.category, name='category_pois'),
    path('categories', views.categories, name='categories'),
    path('editcategory/<int:id>', views.edit_category, name='edit_category'),
    path('country/<int:id>', views.country, name='country'),
    path('countries', views.countries, name='countries'),
    path('editcountry/<int:id>', views.edit_country, name='edit_country'),
    path('pointofinterests', views.pointofinterests, name='pointofinterests'),
    path('contact', views.contact, name='contact'),
]
