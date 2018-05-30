from django.contrib import admin
from .models import Country, Zone, PointOfInterest, Category, Comment

# Register your models here.
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    verbose_name = "Country"
    verbose_name_plural = "Countries"
    search_fields = ['name']

@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    verbose_name = "Zone"
    verbose_name_plural = "Zones"
    search_fields = ['name']

@admin.register(PointOfInterest)
class PointOfInterestAdmin(admin.ModelAdmin):
    verbose_name = "PoI"
    verbose_name_plural = "PoIs"
    search_fields = ['title', 'category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    verbose_name = "Category"
    verbose_name_plural = "Categories"
    search_fields = ['title']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    verbose_name = "Comment"
    verbose_name_plural = "Comments"
    search_fields = ['content']
