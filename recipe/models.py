from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Ingredient(models.Model):
    """
    Stores ingredients for recipe related to :model:`auth.User`.
    """
    ing_id = models.AutoField(primary_key=True)
    ing_name = models.CharField(max_length=200)
        
    def __str__(self):
        return self.ing_name


class Recipe(models.Model):
    """
    Stores a single recipe entry related to :model:`auth.User`. 
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

    recipe_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipe_book")
    title = models.CharField(max_length=200, unique=True)    
    description = models.TextField()
    ingredient = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    difficulty = models.IntegerField(choices=DIFFICULTY_LEVELS)
    serves = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')
    
    class Meta:
        ordering = ["-created_at"]

    def total_time(self):
        return self.prep_time + self.cook_time

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    """
    Stores ingredients for recipe related to :model:`auth.User`.
    """
    UNIT_CHOICES= (
        ('GRAM', 'Gram'),
        ('KILOGRAM', 'Kilogram'),
        ('TEASPOON', 'Teaspoon'),
        ('TABLESPOON', 'Tablespoon'),
        ('OUNCE', 'Ounce'),
        ('LITRE', 'Litre'),
        ('MILLILITRE', 'Millilitre'),
        ('SMALL', 'Small'),
        ('LARGE', 'Large'),
        ('MEDIUM', 'Medium'),
    )
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ing = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=200, choices=UNIT_CHOICES)

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.ing.ing_name} in {self.receipe.title}"


class MealPlan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_title = models.CharField(max_length=200)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(auto_now=True)
    recipe = models.ManyToManyField(Recipe, related_name='meal_plans')
   
    def __str__(self):
        return f"{self.plan_title} - ({self.start_date} - {self.end_date})"


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User` and :model:`recipe.Recipe`.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approver_note = models.CharField(max_length=200)
    approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f'Comment by {self.user} on {self.recipe}'


################################################################################    
# class FavouriteRecipe(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.user.username} favourites {self.recipe.title}'

#     class Meta:
#         unique_together = ('user', 'recipe')


