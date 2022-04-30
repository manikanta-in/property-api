from django.contrib import admin

# Register your models here.

from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ("location", "latittude", "longitude",)

admin.site.register(Property, PropertyAdmin)