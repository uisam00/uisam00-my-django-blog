from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'posted', 'changed', 'status')
    list_filter = ('status', 'created', 'posted')
    raw_id_fields = ('author',)
    date_hierarchy = 'posted'
    search_fields = ('title', 'article')
    prepopulated_fields = {'slug': ('title',)}
