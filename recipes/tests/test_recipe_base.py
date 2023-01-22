from django.contrib.auth.models import User
from django.test import TestCase

from recipes.models import Category, Recipe


class RecipeBaseTest(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_recipe(
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
        preparation_steps_is_html=False,
        is_published=True
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
            preparation_steps=preparation_steps,
            preparation_steps_is_html=preparation_steps_is_html,
            is_published=is_published
        )

    def make_author(
        self,
        first_name='John',
        last_name='Doo',
        email='john.doo@email.com',
        username='john.doo',
        password='123'
    ):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=password,
        )

    def make_category(self, name='First Recipe Category'):
        return Category.objects.create(name=name)
