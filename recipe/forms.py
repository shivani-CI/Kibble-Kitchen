from .models import Recipe, Comment, RecipeIngredient
from django import forms
from django_summernote.widgets import SummernoteWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit_recipe', 'Submit Recipe'))

    class Meta:
        model = Recipe
        fields = ['title', 'description', 'prep_time', 'cook_time', 'difficulty', 'serves', 'status', 'image']
        widgets = {
            'description':SummernoteWidget()
        }


class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ing', 'quantity', 'unit']
    
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

