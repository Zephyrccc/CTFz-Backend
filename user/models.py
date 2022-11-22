from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        abstract = True


class User(AbstractUser):
    """用户系统"""
    username = models.CharField(max_length=15, unique=True, verbose_name='用户名')
    first_name = None
    last_name = None

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    SEX_CHOICES = (('男', '男'), ('女', '女'), ('保密', '保密'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户', related_name='profile')
    sex = models.CharField(choices=SEX_CHOICES, max_length=2,default='保密', verbose_name='性别')

    class Meta:
        db_table = "user_profile"
        verbose_name = "用户资料"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
