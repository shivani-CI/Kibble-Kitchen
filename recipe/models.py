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


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`auth.User` and :model:`blog.Post`.
    """
    recipe_id = models.ForeignKey(Recipe, on_delete= models.CASCADE, related_name="comments")
    user_id = models.ForeignKey(User, on_delete= models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)



