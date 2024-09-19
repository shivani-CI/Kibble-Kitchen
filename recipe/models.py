from django.db import models
from django.contrib.auth.models import User


STATUS =((0, "Draft"), (1, "Published"))
# Create your models here.
class Recipe(models.Model):
    """
    Stores a single recipe entry related to :model:`auth.User`. 
    """
    recipe_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete= models.CASCADE, related_name="recipe_book")
    title = models.CharField(max_length=200, unique=True)
    description =models.TextField()
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    difficulty = models.CharField(max_length=200)
    serves = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    def total_time(self):
        return self.prep_time + self.cook_time

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.title}"


class Ingredient(models.Model):
    """
    Stores ingredients for recipe related to :model:`auth.User`.
    """
    class CategoryChoices(models.TextChoices):
        MEAT = 'Meat'
        VEGETABLE = 'Vegetable'
        FISH = 'Fish'
        OTHER = 'Other'

    
    class UnitChoices(models.TextChoices):
        GRAM = 'Gram'
        KILOGRAM = 'Kilogram'
        TEASPOON = 'Teaspoon'
        TABLESPOON = 'Tablespoon'
        OUNCE = 'Ounce'
        LITRE = 'Litre'
        MILLILITRE = 'Millilitre'

    ing_id = models.AutoField(primary_key=True)
    recipe_id = models.ForeignKey(Recipe, on_delete= models.CASCADE, related_name="ingredients")
    ing_name = models.CharField()
    category = models.CharField(choices=CategoryChoices.choices)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(choices=UnitChoices.choices)
    is_allergen = models.BooleanField(default=False)


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User` and :model:`recipe.Recipe`.
    """
    recipe_id = models.ForeignKey(Recipe, on_delete= models.CASCADE, related_name="comments")
    user_id = models.ForeignKey(User, on_delete= models.CASCADE, related_name="commenter")
    body = models.TextField()
    approver_note = models.CharField()
    approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-created_at"] 
