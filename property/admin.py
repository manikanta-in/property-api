from django.contrib import admin

# Register your models here.

from .models import Property


class PropertyAdmin(admin.ModelAdmin):
    list_display = ("location_name", "latitute", "longtitue",)


admin.site.register(Property, PropertyAdmin)