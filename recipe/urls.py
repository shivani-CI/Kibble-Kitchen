from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'), # Set the root URL to the home page
    path('browse/', views.RecipeList.as_view(), name='browse_recipes'), # Show all recipes (e.g., /recipes/)
    path('<int:recipe_id>/', views.get_recipe_detail, name='get_recipe_detail'),
    path('<int:recipe_id>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<int:recipe_id>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),  # Handle new ingredient addition via AJAX
    path('create_meal_plan/', views.create_meal_plan, name='create_meal_plan'),
    path('meal_plan/', views.get_meal_plan, name='get_meal_plan')
]
# later
# path('<int:recipe>/add_to_favourites', views.add_to_favourites, name='add_to_favourites'),
# path('favorites/', views.FavouriteRecipe, name='favourite_recipes'),
# path('my_recipe/', views.myrecipe, name='my_recipe'),
# path('my_favourite/', views.myfavourite, name='my_favourite'),