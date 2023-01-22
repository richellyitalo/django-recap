from django.test import TestCase
from django.urls import reverse


class RecipeUrlTest(TestCase):
    def test_recipe_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recipe_category_url_is_correct(self):
        # category_url = reverse('recipes:category-view', args=(1,))
        category_url = reverse('recipes:category-view',
                               kwargs={'category_id': 30})
        self.assertEqual(category_url, '/recipes/category/30/')

    def test_recipe_view_url_is_correct(self):
        recipe_view_url = reverse('recipes:view', kwargs={'id': 30})
        self.assertEqual(recipe_view_url, '/recipes/30/')
