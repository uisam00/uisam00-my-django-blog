from django.contrib import admin
from .models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('name', 'created', 'updated')
    list_filter = ('name', 'created', 'updated')
    date_hierarchy = 'created'
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('visualizar_imagem', 'posted', 'created', 'updated')
    list_display = ('title', 'author', 'posted', 'updated', 'status',)
    list_filter = ('status', 'created', 'posted')
    raw_id_fields = ('author',)
    date_hierarchy = 'posted'
    search_fields = ('title', 'subtitle', 'article')
    prepopulated_fields = {'slug': ('title',)}

    def visualizar_imagem(self, obj):
        return obj.view_image

    visualizar_imagem.short_description = "Imagem Cadastrada"
