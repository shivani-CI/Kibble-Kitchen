""" Module for django apps """
from django.apps import AppConfig


class RecipeConfig(AppConfig):
    """ Class for recipe config """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipe'
