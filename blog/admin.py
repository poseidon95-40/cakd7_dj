from django.contrib import admin
from .models import Post, Category, Tag

admin.site.register(Post)
# Register your models here.

class CateoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Category, CateoryAdmin)    
admin.site.register(Tag, TagAdmin)