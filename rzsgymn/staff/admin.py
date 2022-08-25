from django.contrib import admin

from .models import Person, SocialNetworkOfUser, TypeOfSocialNetwork
from certificate.models import Certificate


@admin.register(TypeOfSocialNetwork)
class SocialNetworkOfUserAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'class_name',
    )


@admin.register(SocialNetworkOfUser)
class SocialNetworkOfUserAdmin(admin.ModelAdmin):
    list_display = (
        'person',
        '__str__',
        'link',
    )


class SocialNetworkOfUserInline(admin.StackedInline):
    model = SocialNetworkOfUser
    extra = 1


class CertificateInline(admin.StackedInline):
    model = Certificate
    extra = 1


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        'get_fullname',
        'sex',
        'show_photo',
        'birthday',
        'liberated',
    )

    inlines = [
        SocialNetworkOfUserInline,
        CertificateInline,
    ]
