from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        abstract = True


class UserProfile(AbstractUser, BaseModel):
    """用户系统"""
    username = models.CharField(verbose_name='用户名', max_length=15, unique=True)
    first_name = None
    last_name = None
    date_joined = None

    class Meta:
        db_table = "user"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
