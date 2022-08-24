from django.contrib import admin
from .models import OtherStaff, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'names')


@admin.register(OtherStaff)
class OtherStaffAdmin(admin.ModelAdmin):
    list_display = ('person',)
