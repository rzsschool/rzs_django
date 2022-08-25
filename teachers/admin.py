from django.contrib import admin
from .models import Teacher, Lesson, Category, Rank


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'person',
        'categories',
    )


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'mass')


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ('name', )
