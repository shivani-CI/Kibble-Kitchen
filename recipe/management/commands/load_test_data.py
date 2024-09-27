from recipe.models import Recipe, Ingredient, RecipeIngredient
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random


class Command(BaseCommand):
    help = 'Load test data into the database'

    def handle(self, *args, **options):
        user = User.objects.get(username='monkey1')

        # Create test data
        for i in range(25):
            Recipe.objects.create(
                title=f'Test Recipe {i + 1}',
                author=user,
                description='Test description.',
                prep_time=5 * i,
                cook_time=10 * i,
                difficulty=0,
                serves=i + 1,
                status=1
            )

            Ingredient.objects.create(
                name=f'Beef - {i}'
            )

        for i in range(25):
            recipe = Recipe.objects.get(id=i+1)

            for j in range(5):
                rand_j = random.randint(1, 24)
                ingredient = Ingredient.objects.get(id=rand_j)

                RecipeIngredient.objects.create(
                    recipe=recipe,
                    ingredient=ingredient,
                    unit='GRAM',
                    quantity=10*i
                )

        self.stdout.write(self.style.SUCCESS('Test data created successfully!'))
