from django.contrib import admin

from .models import Administration, TypeOfAdministrativePosition


@admin.register(TypeOfAdministrativePosition)
class TypeOfAdministrativePositionAdmin(admin.ModelAdmin):
    list_display = (
        'type_position',
    )


@admin.register(Administration)
class AdministrationAdmin(admin.ModelAdmin):
    list_display = (
        'person',
        'position',
    )
