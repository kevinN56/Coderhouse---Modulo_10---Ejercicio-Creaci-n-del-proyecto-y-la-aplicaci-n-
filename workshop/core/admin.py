from django.contrib import admin
from .models import Autor,Post,Tag
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','published_date')
    list_filter = ('tags',)
admin.site.register(Post,PostAdmin)    
admin.site.register(Autor)
admin.site.register(Tag)