from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField('Title', max_length=255)
    imagePost = models.CharField('Image', max_length=500, blank=True, null=True)
    contentPost = models.TextField('Content')
    dataPost = models.DateTimeField('Data published', default=datetime.now)

    def __str__(self):
        return f'{self.title} - {self.dataPost}.'

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'