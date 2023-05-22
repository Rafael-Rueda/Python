from django.contrib import admin
from . import models

class recipe_categoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(model_or_iterable=models.recipe_category, admin_class=recipe_categoryAdmin)

class RecipeAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Recipe, RecipeAdmin)
