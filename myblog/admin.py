from django.contrib import admin
from .models import post, comment
# Register your models here.
@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_per_page = 10

# Comment model 
@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'comment_date')
    search_fields = ('text',)
    list_per_page = 10