# from django.urls import path, re_path
from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),
    path('recipes/<int:id>/', views.recipe_view, name='view'),
    path('recipes/category/<int:category_id>/',
         views.category, name='category-view')
    # re_path(
    #     r'^recipes/category/(?P<category_id>\d+)(?:/(?P<category_name>\S+))?/$',  # noqa: 501
    #     views.category, name='category-view'),
]
