from django.core.exceptions import ValidationError
from parameterized import parameterized

from recipes.models import Recipe

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

    def make_recipe_without_default_fields(
        self,
        author_data=None,
        category_data=None,
        title='Recipe Title',
        description='Recipe Description',
        slug='recipe-slug',
        preparation_time='10',
        preparation_time_unit='Minutos',
        servings='30',
        servings_unit='Pratos',
        preparation_steps='Prepation Steps',
    ):
        if author_data is None:
            author_data = {}

        if category_data is None:
            category_data = {}

        return Recipe.objects.create(
            author=self.make_author(**author_data),
            category=self.make_category(**category_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps
        )

    def test_recipe_field_preparation_steps_is_html_is_saved_as_default(self):
        recipe = self.make_recipe_without_default_fields(
            category_data={
                'name': 'Category 2'
            },
            author_data={
                'username': 'author-02'
            }
        )

        self.assertFalse(
            recipe.preparation_steps_is_html,
            f'Esperado que "preparation_steps_is_html" seja False\
                mas foi salvo como {recipe.preparation_steps_is_html}'
        )

    def test_recipe_field_is_published_saved_as_default_false(self):
        recipe = self.make_recipe_without_default_fields(
            category_data={
                'name': 'Category 2'
            },
            author_data={
                'username': 'author-02'
            }
        )

        self.assertFalse(
            recipe.is_published,
            f'Esperado que "is_published" seja False\
            mas foi salvo como {recipe.is_published}'
        )

    def test_recipe_if_return_str_cast_is_title_recipe(self):
        needed_title = 'Recipe title to compare'
        self.recipe.title = needed_title
        self.recipe.save()
        self.assertEqual(str(self.recipe), needed_title)
