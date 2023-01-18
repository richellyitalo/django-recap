from django.urls import path, re_path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.recipe_view, name='view'),
    re_path(
        r'^category/(?P<category_id>\d+)(?:/(?P<category_name>\S+))?/$',
        views.category, name='category-view'),
]
