from django.contrib import admin
from .models import Page, ImageOfPage


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'relative_link',
    )


@admin.register(ImageOfPage)
class ImageOfPageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'get_link',
        'data',
        'show_image',
    )
