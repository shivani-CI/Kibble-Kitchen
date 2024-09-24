from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import JsonResponse
from .models import Recipe, Ingredient, MealPlan, Comment
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home_view(request):
    """
    Render the home page.
    """
    return render(request, 'recipe/index.html')

class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "recipe/recipe_list.html"
    paginate_by = 8


# def recipe_list(request):
#     recipes = Recipe.objects.all()
#     return render(request, 'recipe/recipe_list.html', {'recipes': recipes})


def get_recipe_detail(request, recipe):
    #TODO -
    recipe = get_object_or_404(Recipe, recipe=recipe)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})

def add_recipe(request, recipe):
    #TODO - 
    recipe = get_object_or_404(Recipe, recipe=recipe)
    return render(request, 'recipe/add_recipe.html', {'recipe': recipe})

def create_meal_plan(request, meal_plan):
    #TODO - 
    meal_plan = get_object_or_404(MealPlan, id=meal_plan)
    return render(request, 'recipe/create_meal_plan.html', {'meal_plan': meal_plan})

def get_meal_plan(request, meal_plan):
    #TODO - 
    meal_plan = get_object_or_404(MealPlan, id=meal_plan)
    return render(request, 'recipe/meal_plan.html', {'meal_plan': meal_plan})




#####################################################################################
def recipe_search(request):
    query = request.GET.get('q')
    if query:
        ingredients = Ingredient.objects.filter(name__icontains=query)
        recipes = Recipe.objects.filter(ingredients__in=ingredients).distinct()
    else:
        recipes = Recipe.objects.all()
    return render(request, 'recipe_search.html', {'recipes': recipes})


def ingredient_list(request):
    query = request.GET.get('q', '')
    if query:
        ingredients = Ingredient.objects.filter(name__icontains=query).values('id', 'name')
    else:
        ingredients = Ingredient.objects.all().values('id', 'name')
    return JsonResponse(list(ingredients), safe=False)


# def add_to_favourites(request, recipe):
#     recipe = get_object_or_404(Recipe, id=recipe)
    
#     # Check if the recipe is already in favourites
#     favourite, created = FavouriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
    
#     if created:
#         messages.success(request, f"{recipe.title} was added to your favourites!")
#     else:
#         messages.info(request, f"{recipe.title} is already in your favourites.")
    
#     return redirect('recipe_detail', recipe=recipe)


# def signup_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to login after successful signup
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})

