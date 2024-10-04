""" Module for all django views """
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from django.forms import formset_factory
from django.http import JsonResponse
from django.contrib import messages
from django.db import transaction
from django.views import generic
from .forms import RecipeForm, RecipeIngredientForm, MealPlanForm, CommentForm
from .models import Recipe, Ingredient, RecipeIngredient, MealPlan, Comment
from .utils import get_nutrition_info


def home_view(request):
    """ Return the home page view """
    return render(request, 'recipe/index.html')


class RecipeList(generic.ListView):
    """ Return the browse recipe view"""
    model = Recipe
    queryset = Recipe.objects.filter(status=1)
    template_name = "recipe/browse_recipes.html"
    paginate_by = 6


def get_recipe_nutrition_info(recipe):
    """
    Uncomment the above and comment the below when you want to get actual data
    This is done to avoid monthly API limits
    """
    # recipe_ingredients = [
    #     f'{recipe_ing.quantity}{recipe_ing.unit} {recipe_ing.ingredient.name}'
    #     for recipe_ing in recipe.ingredients_in_recipe.all()]
    # total_nutrition = get_nutrition_info(recipe.title, recipe_ingredients)
    total_nutrition = {
        'calories': 500.56462465465464,
        'protein': 150,
        'fat': 14,
        'carbs': 18,
        'fiber': 7.9
    }
    return total_nutrition


@require_POST
def post_recipe_comment(request, recipe_instance):
    """ Send a post request for a new comment """
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.recipe = recipe_instance
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
    return redirect('get_recipe_detail', recipe_pk=recipe_instance.pk)


def handle_recipe_comment_context(recipe_instance):
    """
    Handle comment context for recipe instances
    """
    comments = recipe_instance.comments_on_recipe.all().order_by('-created_at')
    comment_count = comments.filter(approved=True).count()
    comment_form = CommentForm()
    comment_context = {
        'comments': comments,
        'comment_count': comment_count,
        'comment_form': comment_form
    }
    return comment_context


def get_recipe_detail(request, recipe_pk):
    """
    Display details of a recipe, including comments and
    aggregated nutritional information for the entire recipe
    """
    recipe = get_object_or_404(Recipe, pk=recipe_pk)
    if request.POST:
        return post_recipe_comment(request, recipe)

    if request.user.is_authenticated:
        all_meal_plans = MealPlan.objects.filter(user=request.user)
    else:
        all_meal_plans = []
    total_nutrition = get_recipe_nutrition_info(recipe)
    comment_context = handle_recipe_comment_context(recipe)
    context = {
        'recipe': recipe,
        'all_meal_plans': all_meal_plans,
        **total_nutrition,
        **comment_context
    }
    return render(request, 'recipe/recipe_detail.html', context)


@require_POST
def add_recipe_to_meal_plan(request):
    """ Add a recipe to a meal plan """
    data = json.loads(request.body)
    meal_plan_id = data['meal_plan_id']
    recipe_id = data['recipe_id']

    meal_plan = get_object_or_404(MealPlan, pk=meal_plan_id)
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    if recipe in meal_plan.recipes.all():
        return JsonResponse({'success': False,
                             'message': 'Recipe already in meal plan.'
                             })

    meal_plan.recipes.add(recipe)
    return JsonResponse({'success': True,
                         'message': 'Recipe added to meal plan successfully!'
                         })


@login_required
def create_or_update_recipe(request, recipe_pk=None):
    """
    Take the user inputted recipe and save it to the database
    """
    recipe_ingredient_form_set = formset_factory(RecipeIngredientForm, extra=3)

    # If there is a recipe_pk then update or else create a new recipe
    if recipe_pk:
        recipe = get_object_or_404(Recipe, pk=recipe_pk)
        is_update = True
    else:
        recipe = None
        is_update = False

    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        recipe_ing_form_set = recipe_ingredient_form_set(request.POST)

        if recipe_form.is_valid() and recipe_ing_form_set.is_valid():
            with transaction.atomic():
                recipe = recipe_form.save(commit=False)
                recipe.author = request.user
                recipe.save()

                if is_update:
                    recipe.ingredients.clear()

                for recipe_ing_form in recipe_ing_form_set:
                    ingredient = recipe_ing_form.cleaned_data.get('ingredient')
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
                return redirect('get_recipe_detail', recipe_pk=recipe.pk)
        else:
            if not recipe_form.is_valid():
                form_error = str(recipe_form.errors)
            else:
                form_error = str(recipe_ing_form_set.errors)
            messages.add_message(
                request, messages.ERROR,
                f'Your recipe is not saved! - {form_error}'
            )

    recipe_form = RecipeForm(instance=recipe)
    if is_update:
        initial_ingredients = [
            {'ingredient': recipe.ingredient,
             'quantity': recipe.quantity,
             'unit': recipe.unit}
            for recipe in recipe.ingredients_in_recipe.all()
        ]
        recipe_ing_form_set = recipe_ingredient_form_set(initial=initial_ingredients)
    else:
        recipe_ing_form_set = recipe_ingredient_form_set()
    ingredients = Ingredient.objects.all()
    context = {
        'recipe_form': recipe_form,
        'recipe_ingredient_formset': recipe_ing_form_set,
        'all_ingredients': ingredients,
        'recipe': recipe,
        'is_update': is_update
    }
    return render(request, 'recipe/add_recipe.html', context)


def delete_recipe(request, recipe_pk):
    """
    Delete a recipe
    """
    recipe = get_object_or_404(Recipe, pk=recipe_pk)

    if recipe.author == request.user:
        recipe.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Recipe deleted!')
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own recipe!')

    return redirect('browse_recipes')


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

            return redirect('get_meal_plan', meal_plan_pk=meal_plan.pk)

    meal_plan_form = MealPlanForm()
    context = {
        'meal_plan_form': meal_plan_form
    }
    return render(request, 'recipe/create_meal_plan.html', context)


class MealPlanList(LoginRequiredMixin, generic.ListView):
    """
    Return the browse meal plan view
    """
    template_name = "recipe/browse_meal_plan.html"
    paginate_by = 8

    def get_queryset(self):
        return MealPlan.objects.filter(user=self.request.user)


@login_required
def get_meal_plan(request, meal_plan_pk):
    """
    Get the meal plan details for a particular meal plan
    """
    meal_plan = get_object_or_404(MealPlan, pk=meal_plan_pk, user=request.user)

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

    return redirect('get_recipe_detail', recipe_pk=recipe_pk)


@login_required
def delete_comment(request, recipe_pk, comment_pk):
    """
    Delete existing comment
    """
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

    return redirect('get_recipe_detail', recipe_pk=recipe_pk)
