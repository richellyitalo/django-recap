from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_recipe_base import RecipeBaseTest


class RecipeTestModelRecipe(RecipeBaseTest):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()

        return super().setUp()

    # Teste individual
    # Para campos semelhantes, há o teste parametrizado logo abaixo
    # def test_recipe_saving_with_title_above_the_allowed(self):
    #     self.recipe.title = 'a'*70

    #     with self.assertRaises(ValidationError):
    #         self.recipe.full_clean()

    #     self.recipe.save()

    # maneira simples e nativa de usar teste parametrizado
    # Desvantagem: não cria contexto por campos
    # def test_recipe_max_length_fields(self):
    #     fields_to_test = [
    #         ('title', 65),
    #         ('description', 255),
    #         ('preparation_time_unit', 65),
    #         ('servings_unity', 65),
    #     ]

    #     for field, max_length in fields_to_test:
    #         setattr(self.recipe, field, 'A' * (max_length + 1))

    #         with self.assertRaises(ValidationError):
    #             self.recipe.full_clean()

    #         self.recipe.save()

    # Maneira com package 'parameterized'
    # https://pypi.org/project/parameterized/
    @parameterized.expand([
        ('title', 65),
        ('description', 255),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_recipe_max_length_fields(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
