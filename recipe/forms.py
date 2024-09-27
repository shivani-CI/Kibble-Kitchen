from recipe.models import Recipe, RecipeIngredient, MealPlan, Comment
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


class RecipeIngredientForm(forms.ModelForm):
    """
    Add the ingredients for a recipe - also handles saving new ingredients
    """
    new_ingredient = forms.CharField(max_length=200, required=False, label="Add new ingredient")

    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity', 'unit']

    def clean(self):
        cleaned_data = super().clean()
        ingredient = cleaned_data.get('ingredient')
        new_ingredient = cleaned_data.get('new_ingredient')

        # Either select an ingredient or add a new ingredient
        if not ingredient and not new_ingredient:
            raise forms.ValidationError('Please either select an ingredient or add a new one.')
        return cleaned_data


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

