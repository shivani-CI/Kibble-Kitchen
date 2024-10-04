""" Module for django forms """
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Ingredient, Recipe, RecipeIngredient, MealPlan, Comment


class RecipeForm(forms.ModelForm):
    """
    Create a new recipe
    """

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit_recipe', 'Submit Recipe'))

    class Meta:
        """ Meta class for recipe forms """
        # pylint: disable=too-few-public-methods
        model = Recipe
        fields = ['title', 'description', 'prep_time', 'cook_time',
                  'difficulty', 'serves', 'image', 'status']
        widgets = {
            'description': SummernoteWidget()
        }

    def clean_title(self):
        """ Overriding base cleaning for form title """
        title = self.cleaned_data.get('title')
        print(f'Within form class - {self.instance.pk} pk of recipe')

        if Recipe.objects.filter(title=title).exclude(pk=self.instance.pk).exists():
            msg = 'A recipe with this title already exists. Please choose a different title.'
            raise forms.ValidationError(msg)
        return title


class RecipeIngredientForm(forms.ModelForm):
    """
    Add the ingredients for a recipe
    """
    ingredient = forms.CharField(max_length=100, required=True,
                                 widget=forms.TextInput(
                                    attrs={'class': 'form-control',
                                    'placeholder': 'Enter ingredient name'}))

    class Meta:
        """ Meta class for recipe ingredient forms """
        # pylint: disable=too-few-public-methods
        model = RecipeIngredient
        fields = ['ingredient', 'quantity', 'unit']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'quantity-input',
            'style': 'max-width: 55px;'}),
        }

    def clean_ingredient(self):
        """ Overriding base cleaning for ingredient field """
        ingredient_name = self.cleaned_data.get('ingredient')

        if ingredient_name:
            ingredient, _ = Ingredient.objects.get_or_create(name=ingredient_name)
            return ingredient
        raise forms.ValidationError('This field is required')


class MealPlanForm(forms.ModelForm):
    """
    Create a meal plan
    """
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    recipes = forms.ModelMultipleChoiceField(queryset=Recipe.objects.all(),
                                             widget=forms.SelectMultiple())

    def __init__(self, *args, **kwargs):
        super(MealPlanForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit_meal_plan', 'Submit Meal Plan'))

    class Meta:
        """ Meta class for meal plan forms """
        # pylint: disable=too-few-public-methods
        model = MealPlan
        fields = ['title', 'start_date', 'end_date', 'recipes']
        widgets = {
            'description': SummernoteWidget()
        }


class CommentForm(forms.ModelForm):
    """
    Create a comment on a recipe
    """

    class Meta:
        """ Meta class for comment forms """
        # pylint: disable=too-few-public-methods
        model = Comment
        fields = ['body']
