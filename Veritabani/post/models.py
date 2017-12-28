from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    # id = models.AutoField(primary_key=True)
    user = models.ForeignKey('auth.User', verbose_name='Yazar', related_name='posts')
    title = models.CharField(max_length=120, verbose_name="Başlık")
    question_Content = models.TextField(verbose_name="Soru İçeriği")
    publishing_date = models.DateTimeField(verbose_name="Yayımlanma Tarihi", auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})
        # return "/post/{}".format(self.id)

    def get_create_url(self):
        return reverse('post:create')

    def get_update_url(self):
        return reverse('post:update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post:delete', kwargs={'id': self.id})

    class Meta:
        ordering = ['-publishing_date', 'id']


class Comment(models.Model):
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200, verbose_name='Ad Soyad')
    content = models.TextField(verbose_name='Cevap')

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
