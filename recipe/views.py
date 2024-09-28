from recipe.forms import RecipeForm, RecipeIngredientForm, MealPlanForm, CommentForm
from recipe.models import Recipe, Ingredient, RecipeIngredient, MealPlan, Comment
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator
from django.forms import formset_factory
from django.contrib import messages
from django.db import transaction
from django.views import generic
from django.conf import settings
import json


def home_view(request):
    return render(request, 'recipe/index.html')

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1)
    template_name = "recipe/browse_recipes.html"
    paginate_by = 6


def get_recipe_detail(request, recipe_pk):
    """
    Get the recipe details for a particular recipe
    """
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    comments = recipe.comments_on_recipe.all().order_by('-created_at')
    comment_count = comments.filter(approved=True).count()
    comment_form = CommentForm()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'There was an error submitting your comment. Please try again.'
            )
    
    context = {
        'recipe': recipe,
        'comments': comments,
        'comment_count': comment_count,
        'comment_form': comment_form,
    }
    return render(request, 'recipe/recipe_detail.html', context)

@login_required   
def create_or_update_recipe(request, recipe_pk=None):
    """
    Take the user input-ed recipe and save it to the database
    """
    RecipeIngredientFormSet = formset_factory(RecipeIngredientForm, extra=1)

    # If there is a recipe_pk then update or else create a new recipe
    if recipe_pk:
        recipe = get_object_or_404(Recipe, pk=recipe_pk)
        is_update = True
    else:
        recipe = None
        is_update = False

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        recipe_ing_form_set = RecipeIngredientFormSet(request.POST)

        if recipe_form.is_valid() and recipe_ing_form_set.is_valid():
            with transaction.atomic():
                recipe = recipe_form.save(commit=False)
                recipe.author = request.user
                recipe.save()

                if is_update:
                    recipe.ingredients.clear()

                for recipe_ing_form in recipe_ing_form_set:
                    ingredient = recipe_ing_form.cleaned_data.get('ingredient')
                    if ingredient:
                        RecipeIngredient.objects.create(
                            recipe=recipe,
                            ingredient=ingredient,
                            quantity=recipe_ing_form.cleaned_data.get('quantity'),
                            unit=recipe_ing_form.cleaned_data.get('unit')
                        )
                
                messages.add_message(
                    request, messages.SUCCESS,
                    'Your recipe has been saved!'
                )
                return redirect('browse_recipes')
        else:
            # Print form errors for debugging
            print('Recipe Form Errors:', recipe_form.errors)
            print('Recipe Ingredient Formset Errors:', recipe_ing_form_set.errors)
    
    recipe_form = RecipeForm(instance=recipe)
    if is_update:
        initial_ingredients = [
                {'ingredient': recipe.ingredient,
                 'quantity': recipe.quantity,
                 'unit': recipe.unit}
            for recipe in recipe.ingredients_in_recipe.all()
            ]
        recipe_ing_form_set = RecipeIngredientFormSet(initial=initial_ingredients)
    else:
        recipe_ing_form_set = RecipeIngredientFormSet()
    ingredients = Ingredient.objects.all()
    context = {
        'recipe_form': recipe_form,
        'recipe_ingredient_formset': recipe_ing_form_set,
        'all_ingredients': ingredients,
        'recipe': recipe,
        'is_update': is_update
    }
    return render(request, 'recipe/add_recipe.html', context)

@login_required
def delete_recipe(request, recipe_pk):
    """
    Delete a recipe
    """
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    
    if request.method == 'DELETE':
        recipe.delete()
        return JsonResponse({'success': True, 'message': 'Recipe deleted successfully.'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=400)

@require_POST
def add_ingredient(request):
    """
    Add an ingredient that the user inputs on the web page
    """
    data = json.loads(request.body)
    new_ingredient_name = data.get('new_ingredient').strip()

    if new_ingredient_name:
        ingredient, created = Ingredient.objects.get_or_create(name=new_ingredient_name)

        return JsonResponse({
            'success': True,
            'ingredient_pk': ingredient.pk
        })

    return JsonResponse({'success': False, 'error': 'No ingredient provided.'}, status=400)


@login_required   
def create_meal_plan(request):
    """
    Create a meal plan for a user (a meal plan is a collection of recipes)
    """
    if request.method == 'POST':
        meal_plan_form = MealPlanForm(request.POST)
        
        if meal_plan_form.is_valid():
            with transaction.atomic():
                meal_plan = meal_plan_form.save(commit=False)
                meal_plan.user = request.user
                meal_plan.save()
                meal_plan_form.save_m2m()

            return redirect('create_meal_plan')
    
    meal_plan_form = MealPlanForm()
    context = {
        'meal_plan_form': meal_plan_form
    }
    return render(request, 'recipe/create_meal_plan.html', context)


class MealPlanList(LoginRequiredMixin, generic.ListView):
    template_name = "recipe/browse_meal_plan.html"
    paginate_by = 8

    def get_queryset(self):
        return MealPlan.objects.filter(user=self.request.user)

def get_meal_plan(request, meal_plan_pk):
    """
    Get the meal plan details for a particular meal plan
    """
    meal_plan = get_object_or_404(MealPlan, pk=meal_plan_pk)
    
    context = {
        'meal_plan': meal_plan}
        
    return render(request, 'recipe/meal_plan_detail.html', context)


@login_required
@require_POST
def edit_comment(request, recipe_pk, comment_pk):
    """
    Edit existing comment
    """
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment_form = CommentForm(data=request.POST, instance=comment)

    if comment_form.is_valid() and comment.user == request.user:
        comment = comment_form.save(commit=False)
        comment.recipe = recipe
        comment.approved = False
        comment.save()
        messages.add_message(
            request, messages.SUCCESS,
            'Comment Updated!')
    else:
        messages.add_message(
            request, messages.ERROR,
            'Error updating comment!')

    return HttpResponseRedirect(reverse('get_recipe_detail', args=[recipe_pk]))

@login_required
def delete_comment(request, recipe_pk, comment_pk):
    """
    Delete existing comment
    """
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if comment.user == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('get_recipe_detail', args=[recipe_pk]))

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
        ingredients = Ingredient.objects.filter(name__icontains=query).values('pk', 'name')
    else:
        ingredients = Ingredient.objects.all().values('pk', 'name')
    return JsonResponse(list(ingredients), safe=False)
