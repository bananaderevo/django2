from django.contrib import admin

from .models import Logs


class PathAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'timestamp')


admin.site.register(Logs, PathAdmin)
