from django.contrib import admin

from .models import App


class AppAdmin(admin.ModelAdmin):
    list_display = ('key', 'name', 'description')

admin.site.register(App, AppAdmin)