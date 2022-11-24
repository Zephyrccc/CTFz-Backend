from django.db import models


class Challenge(models.Model):
    """题目系统"""
    TYPE_CHOICES = (('docker', 'docker'), ('附件', '附件'))
    STATE_CHOICES = ((True, '开放'), (False, '隐藏'))
    type = models.CharField(choices=TYPE_CHOICES,default='docker',max_length=20, verbose_name='类型')
    title = models.CharField(max_length=128, verbose_name='标题')
    # category
    describe = models.CharField(max_length=128, default='', verbose_name='标题')
    score = models.PositiveIntegerField(default=0, verbose_name='分值')
    state = models.BooleanField(choices=STATE_CHOICES, default=True, verbose_name='状态')
    is_fixed_flag=models.BooleanField(default=False, verbose_name='flag是否固定')
    flag=models.CharField(max_length=128, default='', verbose_name='flag')
    have_attachment=models.BooleanField(default=False, verbose_name='是否有附件')
    mark_total = models.PositiveIntegerField(default=0, verbose_name='总评分')
    mark_count = models.PositiveIntegerField(default=0, verbose_name='评分人数')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = "challenge"
        verbose_name = "题目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ChallengeAttachment(models.Model):
    title = models.CharField(max_length=200, verbose_name='附件名', null=True, blank=True)
    file_path = models.FileField(upload_to='challenge_file/', verbose_name='文件路径', null=True, blank=True)
    challenge = models.OneToOneField(Challenge, on_delete=models.CASCADE, verbose_name='题目', related_name='attachment')

    class Meta:
        db_table = "challenge_attachment"
        verbose_name = "题目附件"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class ChallengeDockerConfig(models.Model):
    name = models.CharField(max_length=256, verbose_name='镜像名', default='')
    port = models.PositiveIntegerField(default=80, verbose_name='内部端口')
    memory_limit = models.PositiveSmallIntegerField(default=128, verbose_name='内存限制')
    cpu_limit = models.DecimalField(max_digits=3, decimal_places=1, default=0.5, verbose_name='CPU限制')
    challenge = models.OneToOneField(Challenge, on_delete=models.CASCADE, verbose_name='题目', related_name='docker_config')

    class Meta:
        db_table = "challenge_docker_config"
        verbose_name = "docker设置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
