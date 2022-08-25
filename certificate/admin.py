from django.contrib import admin
from .models import TypeDoc, Platform, Certificate


@admin.register(TypeDoc)
class TypeDocAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Platform)
class PlatformDocAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        'person',
        # 'name',
        # 'type_doc',
        # 'platform',
        # 'number_of_hours',
        # 'date',
    )
