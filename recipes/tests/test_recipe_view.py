from unittest import skip

from django.urls import resolve, reverse

from recipes import views

from .test_recipe_base import RecipeBaseTest


# @skip('Estou skipando a classe toda')
class RecipeViewTest(RecipeBaseTest):
    # @skip('Estou skipando apenas o primeiro método')
    def test_recipe_home_view_is_correct(self):
        view = resolve(
            reverse('recipes:home')
        )
        self.assertIs(view.func, views.home)
        # self.fail('DEU ruim camarada')  # Fail proposital

    def test_recipe_category_view_is_correct(self):
        view = resolve(
            reverse('recipes:category-view', kwargs={'category_id': 30})
        )
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_is_correct(self):
        view = resolve(
            reverse('recipes:view', kwargs={'id': 30})
        )
        self.assertIs(view.func, views.recipe_view)

    def test_recipe_response_status_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_template_used_is_correct(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_show_recipes_not_found_if_not_has_recipe(self):  # noqa: 501
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes found here',
            response.content.decode('utf-8')
        )

    def test_recipe_category_view_return_404_if_no_recipes_found(self):
        response = self.client.get(
            reverse('recipes:category-view',
                    kwargs={'category_id': 9999})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_template_load_recipes(self):
        recipe = self.make_recipe()

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')

        recipe_context = response.context['recipes'].first()

        # context
        self.assertEqual(recipe.title, recipe_context.title)
        self.assertEqual(recipe.category.name,
                         recipe_context.category.name)

        # content
        self.assertIn(recipe.title, content)
        self.assertIn(recipe.category.name, content)
