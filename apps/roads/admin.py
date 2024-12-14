from django.contrib import admin

from apps.roads.models import Roads


class RoadsAdmin(admin.ModelAdmin):
    list_display = ('name', 'search_name', 'created_at')
    ordering = ('created_at',)


admin.site.register(Roads, RoadsAdmin)
