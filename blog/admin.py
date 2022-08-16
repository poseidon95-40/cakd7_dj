from xml.etree.ElementTree import Comment
from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, Category, Tag, Comment

admin.site.register(Post, MarkdownxModelAdmin)
# Register your models here.

class CateoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', )}

admin.site.register(Category, CateoryAdmin)    
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)