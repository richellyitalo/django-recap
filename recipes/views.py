from django.shortcuts import render

from utils.recipes.factory import make_recipe

from .models import Category, Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def category(request, category_id, category_name=''):
    category = Category.objects.filter(id=category_id).first()

    recipes = Recipe.objects.filter(
        is_published=True,
        category__id=category_id).order_by('-created_at')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'title': category.name
    })


def recipe_view(request, id):
    recipe = Recipe.objects.get(id=id)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True
    })
