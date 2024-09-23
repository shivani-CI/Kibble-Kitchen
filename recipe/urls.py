from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home_view, name='home'), # Set the root URL to the home page
    path('browse/', views.RecipeList.as_view(), name='browse_recipes'), # Show all recipes (e.g., /recipes/)
    path('<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('<int:recipe>/add_to_favourites', views.add_to_favourites, name='add_to_favourites'),
    path('favorites/', views.FavouriteRecipe, name='favourite_recipes'),
    path('my_recipes/', views.myrecipes, name='my_recipes'),
    path('my_favourites/', views.myfavourites, name='my_favourites'),
    path('add_recipe/', views.addrecipe.as_view(), name='add_recipe'),
    path('meal_plan/', views.mealplan.as_view(), name='meal_plan'),
    path('signup/', views.signup_view, name='signup'),  # Sign-up view
    path('login/', auth_views.loginView.as_view(), name='login'),  # Django built-in login
    path('logout/', auth_views.logoutView.as_view(), name='logout'),  # Django built-in logout
]
