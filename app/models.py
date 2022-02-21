from django.db import models
from django.forms import CharField, DateTimeField, EmailField, FileField

# Create your models here.

class User(models.Model):
    ''' 用户表 '''
    gender = (('male','男'),('female','女'),)

    username = models.CharField(max_length=128, unique=True)
    password= models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['create_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'


