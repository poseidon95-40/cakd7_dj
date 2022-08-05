from xml.etree.ElementTree import Comment
from django.db import models
from matplotlib.pyplot import title

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20, blank=True, null=True)
    sub_title = models.CharField(max_length=30, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    content_comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'    