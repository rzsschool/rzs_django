from django.contrib import admin

from .models import Facility, Testimonial, Alerts
# from .models import Menu
#
#
# @admin.register(Menu)
# class MenuAdmin(admin.ModelAdmin):
#     list_display = (
#         "type_menu",
#     )


@admin.register(Alerts)
class AlertsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "style",
        "is_published",
    )

    class Media:
        css = {
            'all': ('css/admin/alerts.css',)
        }
        js = ('js/admin/alerts.js',)


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "mass",
        "class_name_icon",
        "description",
    )

    class Media:
        js = ('js/admin/facility.js',)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "show_photo",
        "text",
    )
