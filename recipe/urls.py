from recipe import views
from django.urls import path

urlpatterns = [
    path('', views.home_view, name='home'),
    path('browse/', views.RecipeList.as_view(), name='browse_recipes'),
    path('add_recipe/', views.create_or_update_recipe, name='add_recipe'),
    path('edit_recipe/<int:recipe_pk>/', views.create_or_update_recipe, name='edit_recipe'),
    path('delete_recipe/<int:recipe_pk>/', views.delete_recipe, name='delete_recipe'),
    path('<int:recipe_pk>/', views.get_recipe_detail, name='get_recipe_detail'),
    path('<int:recipe_pk>/edit_comment/<int:comment_pk>', views.edit_comment, name='edit_comment'),
    path('<int:recipe_pk>/delete_comment/<int:comment_pk>', views.delete_comment, name='delete_comment'),
    path('create_meal_plan/', views.create_meal_plan, name='create_meal_plan'),
    path('browse_meal_plans/', views.MealPlanList.as_view(), name='browse_meal_plans'),
    path('meal_plan/<int:meal_plan_pk>/', views.get_meal_plan, name='get_meal_plan'),
    path('meal_plan-add_recipe', views.add_recipe_to_meal_plan, name='add_recipe_to_meal_plan')
]
