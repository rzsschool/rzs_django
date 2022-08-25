from django.contrib import admin
from .models import News, Categories, ImageOfPost


class ImageOfPostInline(admin.StackedInline):
    model = ImageOfPost
    extra = 3


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date_created',
        'author',
        'categories',
        'is_published',
        'number_of_views',
    )
    readonly_fields = (
        'number_of_views',
    )

    inlines = [ImageOfPostInline]

    # class Media:
    #     css = {
    #         'all': ('css/style.css', )
    #     }


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'show_image',
    )


@admin.register(ImageOfPost)
class ImageOfPostAdmin(admin.ModelAdmin):
    list_display = (
        'news',
        'show_image',
    )
