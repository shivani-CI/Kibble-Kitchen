from recipe import views
from django.contrib.auth import views as auth_views
from django.urls import path


urlpatterns = [
    path('', views.home_view, name='home'),
    path('browse/', views.RecipeList.as_view(), name='browse_recipes'),
    path('<int:recipe_pk>/', views.get_recipe_detail, name='get_recipe_detail'),
    path('<int:recipe_pk>/edit_comment/<int:comment_pk>', views.edit_comment, name='edit_comment'),
    path('<int:recipe_pk>/delete_comment/<int:comment_pk>', views.delete_comment, name='delete_comment'),
    path('add_recipe/', views.create_recipe, name='add_recipe'),
    path('add_ingredient/', views.add_ingredient, name='add_ingredient'),
    path('create_meal_plan/', views.create_meal_plan, name='create_meal_plan'),
    path('meal_plan/', views.get_meal_plan, name='get_meal_plan')
]
