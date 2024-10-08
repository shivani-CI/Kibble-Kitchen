""" Module for django data models """
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models


class Ingredient(models.Model):
    """
    Stores a single ingredient
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Stores a single recipe
    """
    STATUS = (
        (0, 'Draft'),
        (1, 'Published'),
    )
    DIFFICULTY_LEVELS = (
        (0, 'Easy'),
        (1, 'Medium'),
        (2, 'Hard'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes_created')
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    difficulty = models.IntegerField(choices=DIFFICULTY_LEVELS)
    serves = models.PositiveIntegerField()
    image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """ Meta class for recipe model """
        # pylint: disable=too-few-public-methods
        ordering = ['-created_at']

    def total_time(self):
        """ Calculate total time to cook """
        return self.prep_time + self.cook_time

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    """
    Stores a single ingredient for a particular recipe
    """
    UNIT_CHOICES = (
        # Weight
        ('MG', 'Milligram'),
        ('GRAM', 'Gram'),
        ('KG', 'Kilogram'),
        ('OUNCE', 'Ounce'),
        ('LB', 'Pound'),

        # Volume
        ('ML', 'Milliliter'),
        ('LITRE', 'Litre'),
        ('TSP', 'Teaspoon'),
        ('TBSP', 'Tablespoon'),
        ('CUP', 'Cup'),
        ('PINT', 'Pint'),
        ('QUART', 'Quart'),
        ('GALLON', 'Gallon'),

        # Quantity / Size
        ('SMALL', 'Small'),
        ('MEDIUM', 'Medium'),
        ('LARGE', 'Large'),
        ('PIECE', 'Piece'),
        ('BUNCH', 'Bunch')
    )
    recipe = models.ForeignKey(Recipe,
                               on_delete=models.CASCADE,
                               related_name='ingredients_in_recipe')
    ingredient = models.ForeignKey(Ingredient,
                                   on_delete=models.CASCADE,
                                   related_name='used_in_recipes')
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=200, choices=UNIT_CHOICES)

    def __str__(self):
        return f"""{self.quantity} {self.get_unit_display()} of
        {self.ingredient.name} in {self.recipe.title}"""


class MealPlan(models.Model):
    """
    Stores a single recipe for a particular meal plan (a collection of recipes)
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meal_plans')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    recipes = models.ManyToManyField(Recipe)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def meal_plan_length(self):
        """ Calculate length of meal plan in days """
        if self.end_date and self.start_date:
            return (self.end_date - self.start_date).days
        return 0

    def __str__(self):
        return f'{self.title} - ({self.start_date} - {self.end_date})'

    def clean(self):
        """ Overwrite base cleaning for model """
        if self.end_date and self.start_date > self.end_date:
            raise ValueError('End date cannot be before start date.')


class Comment(models.Model):
    """
    Stores a single comment for a particular recipe
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments_on_recipe')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_by_user')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    approver_note = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """ Meta class for comment model """
        # pylint: disable=too-few-public-methods
        ordering = ['-approved', '-created_at']

    def __str__(self):
        return f'Comment by {self.user} on {self.recipe}'
