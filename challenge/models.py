from django.db import models


class Challenge(models.Model):
    """题目系统"""
    title = models.CharField(max_length=128, verbose_name='标题')
    score = models.PositiveIntegerField(default=0, verbose_name='分值')
    mark_total = models.PositiveIntegerField(default=0, verbose_name='总评分')
    mark_count = models.PositiveIntegerField(default=0, verbose_name='评分人数')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = "challenge"
        verbose_name = "题目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ChallengeFile(models.Model):
    title = models.CharField(max_length=200, verbose_name='文件名',null=True,blank=True)
    file_path = models.FileField(upload_to='challenge_file/', verbose_name='文件路径',null=True,blank=True)
    challenge = models.OneToOneField(Challenge, on_delete=models.CASCADE, verbose_name='题目', related_name='file')
    
    class Meta:
        db_table = "challenge_file"
        verbose_name = "题目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.challenge.title

# class UserProfile(models.Model):
#     SEX_CHOICES = (('男', '男'), ('女', '女'), ('保密', '保密'))
#     user = models.OneToOneField(
#         User, on_delete=models.CASCADE, verbose_name='用户', related_name='profile')
#     sex = models.CharField(choices=SEX_CHOICES, max_length=2,
#                            default='保密', verbose_name='性别')

#     class Meta:
#         db_table = "user_profile"
#         verbose_name = "用户资料"
#         verbose_name_plural = verbose_name

#     def __str__(self):
#         return self.user.username
