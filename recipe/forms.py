from recipe.models import Ingredient, Recipe, RecipeIngredient, MealPlan, Comment
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms


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
        model = Recipe
        fields = ['title', 'description', 'prep_time', 'cook_time', 'difficulty', 'serves', 'image', 'status']
        widgets = {
            'description': SummernoteWidget()
        }
    
    def clean_title(self):
        title = self.cleaned_data.get('title')
        print(f'Within form class - {self.instance.pk} pk of recipe')

        if Recipe.objects.filter(title=title).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('A recipe with this title already exists. Please choose a different title.')
        return title


class RecipeIngredientForm(forms.ModelForm):
    """
    Add the ingredients for a recipe
    """
    ingredient = forms.CharField(max_length=200, required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Enter ingredient name'}))

    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity', 'unit']

    def clean_ingredient(self):
        ingredient_name = self.cleaned_data.get('ingredient')

        if ingredient_name:
            ingredient, created = Ingredient.objects.get_or_create(name=ingredient_name)
            return ingredient
        else:
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
        model = Comment
        fields = ['body']

