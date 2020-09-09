from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class News(models.Model):

    title=models.CharField(max_length=150,verbose_name='Title')
    content=models.TextField(verbose_name='Content')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='Nashr sanasi')
    update_at=models.DateTimeField(auto_now=True,verbose_name='Yangilangan nashr sanasi')
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name='Photo',blank=True)
    is_published=models.BooleanField(default=True,verbose_name='Publish')
    category=models.ForeignKey('Category',on_delete=models.PROTECT,null=True,verbose_name='Category')
    author=models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name='Author',on_delete=models.CASCADE,null=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='blog_post',blank=True)
    # subscribe = models.ManyToManyField(User, related_name='subscribe',blank=True)

    def get_absolute_url(self):
        return reverse('post_datail',kwargs={'pk':self.pk})

    def total_likes(self):
        return self.likes.count()

    # def total_subscribe(self):
    #     return self.subscribe.count()

    def my_func(self):
        return 'Hello from model'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Yangilik'
        verbose_name_plural='Yangiliklar'
        ordering=['-created_at']


class Category(models.Model):
    title=models.CharField(max_length=150,db_index=True,verbose_name='Kategoriya nomi')

    def get_absolute_url(self):
        return reverse('category_list',kwargs={'pk':self.pk})
        pass
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Kategoriya'
        verbose_name_plural='Kategori'
        ordering=['title']


class Comment(models.Model):
    post=models.ForeignKey(News,verbose_name='Comment',on_delete=models.CASCADE,null=True, related_name='Comment')
    name=models.CharField(max_length=255)
    body=models.TextField(verbose_name='Matn')
    date=models.DateTimeField(auto_now_add=True,)

    def __str__(self):
        return self.name