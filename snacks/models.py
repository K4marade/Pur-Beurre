from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# class Post(models.Model):
#     """docstring for Post"""
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse('post-detail', kwargs={'pk': self.pk})


class Product(models.Model):
    """docstring for Products"""
    ean = models.CharField(max_length=13)
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    substitute = Column(Integer, ForeignKey('product.id'))   #???

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'pk': self.pk})


class Category(models.Model):
    """docstring for Categories"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})


class Favourite(object):
    """docstring for Favourite"""
    date_added = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('favourite-detail', kwargs={'pk': self.pk})
