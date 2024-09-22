from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class Ingredient(models.Model):
    """
    Stores ingredients for recipe related to :model:`auth.User`.
    """
    name = models.CharField()
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return self.name


class Recipe(models.Model):
    """
    Stores a single recipe entry related to :model:`auth.User`. 
    """   
    recipe = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="recipe_book")
    title = models.CharField(max_length=200, unique=True)    
    description = models.TextField()
    ingredient = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    difficulty = models.CharField(max_length=200)
    serves = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='recipes/', blank=True, null=True)
    
    class Meta:
        ordering = ["-created_at"]

    def total_time(self):
        return self.prep_time + self.cook_time

    def __str__(self):
        return f"{self.title}"


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.receipe.title}"


# FavouriteRecipe model added below Recipe model
class FavouriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} favourites {self.recipe.title}'

    class Meta:
        unique_together = ('user', 'recipe')


class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    recipes = models.ManyToManyField(Recipe, related_name='meal_plans')
   
    def __str__(self):
        return f"{self.title} ({self.start_date} - {self.end_date})"


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User` and :model:`recipe.Recipe`.
    """
    recipe = models.ForeignKey(Recipe, on_delete= models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="commenter")
    body = models.TextField()
    approver_note = models.CharField()
    approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"] 
