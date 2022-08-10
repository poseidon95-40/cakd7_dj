from distutils.command.upload import upload
from tabnanny import verbose
from unicodedata import category, name
from xml.etree.ElementTree import Comment
from django.db import models
from matplotlib.pyplot import title
from django.contrib.auth.models import User
import os

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name  
    
    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'    
    
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name  
    
    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'    
    
    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):
    title = models.CharField(max_length=20, null=True)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField(blank=True,null=True)
    content_comment = models.TextField(blank=True, null=True)
    head_image = models.ImageField(upload_to = 'blog/images/%Y/%m/%d/', blank=True )
    file_upload = models.FileField(upload_to = 'blog/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    auther = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.auther}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'    

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)  

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]



     