from django.contrib import admin
from .models import post
# Register your models here.
@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 10