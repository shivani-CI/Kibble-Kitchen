from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import JsonResponse
from .models import Recipe, Ingredient, FavouriteRecipe, MealPlan, Comment
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "recipe/recipe_list.html"
    paginate_by = 8


def home_view(request):
    """
    Render the home page.
    """
    return render(request, 'Index.html')


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})


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


def add_to_favourites(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    
    # Check if the recipe is already in favourites
    favourite, created = FavouriteRecipe.objects.get_or_create(user=request.user, recipe=recipe)
    
    if created:
        messages.success(request, f"{recipe.title} was added to your favourites!")
    else:
        messages.info(request, f"{recipe.title} is already in your favourites.")
    
    return redirect('recipe_detail', recipe_id=recipe.id)


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

