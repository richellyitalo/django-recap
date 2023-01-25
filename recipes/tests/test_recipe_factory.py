from django.test import TestCase

from utils.recipes.factory import make_recipe, rand_ratio


class RecipeFactoryTest(TestCase):
    def test_randomization_method_factory(self):
        self.assertNotEqual(rand_ratio(), rand_ratio())

    def test_if_make_recipe_generate_object(self):
        recipe = make_recipe()
        self.assertIsNotNone(recipe['id'])
