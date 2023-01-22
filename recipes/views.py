from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import get_list_or_404, render

from .models import Category, Recipe

# from utils.recipes.factory import make_recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def category(request, category_id):
    category = Category.objects.filter(id=category_id).first()

    recipes = get_list_or_404(
        Recipe.objects.filter(
            is_published=True,
            category__id=category_id
        ).order_by('-created_at')
    )

    # if not recipes:
    #     return HttpResponse(content='Teste', status=404)
    # if not category:
    #     raise Http404('Category Not Found')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        'title': f'{category.name} - Category'
    })


def recipe_view(request, id):
    try:
        recipe = Recipe.objects.get(id=id)
    except ObjectDoesNotExist:
        raise Http404('Recipe not found')

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True
    })
