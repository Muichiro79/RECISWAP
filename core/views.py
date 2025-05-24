from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe
from .forms import RecipeForm  # assuming you have a ModelForm for Recipe


# Assuming you have a form for editing recipes


# Edit Recipe View
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "core/edit_recipe.html", {"form": form})


# Delete Recipe View
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect("recipe_list")
    return render(request, "recipes/confirm_delete.html", {"recipe": recipe})


# List all recipes
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "core/recipe_list.html", {"recipes": recipes})


# View one recipe (detail page)
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, "core/recipe_detail.html", {"recipe": recipe})


# Add new recipe
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("recipe_list")
    else:
        form = RecipeForm()
    return render(request, "core/add_recipe.html", {"form": form})


# Home page (latest 9)
def home(request):
    recipes = Recipe.objects.order_by("-created_at")[:9]
    return render(request, "core/home.html", {"recipes": recipes})


# About page
def about(request):
    return render(request, "core/about.html")
