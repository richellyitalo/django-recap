from django.core.exceptions import ValidationError

from .test_recipe_base import RecipeBaseTest


class RecipeModelCategoryTest(RecipeBaseTest):
    def setUp(self) -> None:
        self.category = self.make_category(
            name='Category in Category test'
        )
        return super().setUp()

    def test_recipe_category_max_length_field(self):
        self.category.name = 'A'*166
        with self.assertRaises(ValidationError):
            self.category.full_clean()

    def test_recipe_category_if_return_name_in_str(self):
        needed_name = 'Category to compare'
        self.category.name = needed_name
        self.category.save()

        self.assertEqual(str(self.category), needed_name)
