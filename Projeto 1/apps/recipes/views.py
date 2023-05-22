from django.shortcuts import render
from apps.recipes import models
from django.shortcuts import get_list_or_404


def home(request):
    recipes = models.Recipe.objects.all().order_by('-id').filter(is_published=True)
    return render(request =request, template_name='recipes/pages/home.html', context={'recipes': recipes})

def recipe(request, id):
    get_recipe = models.Recipe.objects.filter(id=id, is_published=True)
    recipe = get_list_or_404(get_recipe)
    title = recipe[0].title

    return render(request=request, template_name='recipes/pages/recipe-page.html', context={"is_detail_page": True, 'recipes': recipe, 'title': title})

def category(request, category_id):
    get_recipe = models.Recipe.objects.order_by('-id').filter(category__id=category_id, is_published=True)
    recipe = get_list_or_404(get_recipe)
    title = recipe[0].category.name

    return render(request=request, template_name='recipes/pages/category.html', context={'recipes': recipe, 'title': title})