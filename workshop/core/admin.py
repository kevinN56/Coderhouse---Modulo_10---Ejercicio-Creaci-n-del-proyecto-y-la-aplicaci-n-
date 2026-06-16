from django.contrib import admin
from .models import Autor,Post,Tag
# Register your models here.
class PostInline(admin.TabularInline):
    model = Post
    extra = 1


class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    search_fields = ('name', 'email')
    list_filter = ('name',)
    ordering = ('name',)
    inlines = [PostInline]


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'published_date')
    list_filter = ('author', 'tags', 'published_date')
    search_fields = ('title', 'content', 'author__name')
    ordering = ('-published_date',)
    date_hierarchy = 'published_date'
    filter_horizontal = ('tags',)
    list_per_page = 10
    
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)    


admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)