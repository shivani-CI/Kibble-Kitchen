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
    difficulty = models.CharField(max_length=200, unique=True)
    serves = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)