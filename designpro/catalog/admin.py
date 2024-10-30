from django.contrib import admin
from .models import Application, CategoryApplic

#admin.site.register(Application)
admin.site.register(CategoryApplic)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_category', 'status')
    list_filter =  ('status', 'category')
