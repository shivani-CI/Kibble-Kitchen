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
    new_ingredient = forms.CharField(max_length=200, required=False, label="Add new ingredient")  # Add this field for new ingredients

    class Meta:
        model = RecipeIngredient
        fields = ['ing', 'quantity', 'unit']

    def clean(self):
        cleaned_data = super().clean()
        ing = cleaned_data.get("ing")
        new_ingredient = cleaned_data.get("new_ingredient")

        # Ensure user adds either a new ingredient or selects from the dropdown
        if not ing and not new_ingredient:
            raise forms.ValidationError("Please either select an ingredient or add a new one.")
        
        return cleaned_data    
    
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

