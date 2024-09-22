from . import views
from django.urls import path

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'), # Show all recipes (e.g., /recipes/)
    path('<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('<int:recipe_id>/add_to_favourites', views.add_to_favourites, name='add_to_favourites'),
    path('favorites/', views.favorite_recipes, name='favorite_recipes'),
]