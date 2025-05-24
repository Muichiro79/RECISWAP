# forms.py
from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["name", "ingredients", "instructions", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Recipe name"}),
            "ingredients": forms.Textarea(
                attrs={"placeholder": "List the ingredients"}
            ),
            "instructions": forms.Textarea(attrs={"placeholder": "Describe the steps"}),
        }


# forms.py
