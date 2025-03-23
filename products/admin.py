from django.contrib import admin
from .models import Category, Species, Product

# Inline for Species
class SpeciesInline(admin.TabularInline):
    model = Product.species.through  # Use the through model for many-to-many relationships
    extra = 1  # Number of empty forms to display

# Register the Product model with inline editing for Species
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'outlet', 'category', 'stock')
    list_filter = ('category', 'species', 'outlet')
    search_fields = ('name', 'description')
    filter_horizontal = ('species',)
    inlines = [SpeciesInline]  # Add inline editing for Species

# Register the Category and Species models
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)