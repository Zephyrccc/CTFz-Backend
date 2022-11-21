from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    """用户系统"""
    # identity
    IDENTITY = ((1, '超级管理员'), (100, '管理员'), (1000, '普通用户'))
    identity = models.CharField(choices=IDENTITY, default='普通用户',max_length=20)

    class Meta:
        db_table = "user"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
