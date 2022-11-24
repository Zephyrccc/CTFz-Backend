from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='分类名')

    class Meta:
        db_table = "challenge_category"
        verbose_name = "题目分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=64, verbose_name='标签名')

    class Meta:
        db_table = "tag"
        verbose_name = "标签列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Challenge(models.Model):
    """题目系统"""
    ENVIRONMENT_TYPE_CHOICES = (('docker', 'docker'), ('file', '静态文件'))
    STATE_CHOICES = ((True, '开放'), (False, '隐藏'))
    BOOLEAN_CHOICES = ((True, '是'), (False, '否'))
    environment_type = models.CharField(choices=ENVIRONMENT_TYPE_CHOICES, default='docker', max_length=20, verbose_name='环境类型')
    title = models.CharField(max_length=128, verbose_name='题目名称')
    category = models.ForeignKey(to=Category, on_delete=models.DO_NOTHING, verbose_name="题目分类")
    tag = models.ManyToManyField(to=Tag, verbose_name='标签')
    describe = models.CharField(max_length=128, null=True, blank=True, verbose_name='描述')
    score = models.PositiveIntegerField(default=1, verbose_name='分值')
    state = models.BooleanField(choices=STATE_CHOICES, default=True, verbose_name='状态')
    is_fixed_flag = models.BooleanField(choices=BOOLEAN_CHOICES, default=False, verbose_name='flag是否固定')
    flag = models.CharField(max_length=128, null=True,blank=True, verbose_name='flag')
    have_attachment = models.BooleanField(choices=BOOLEAN_CHOICES, verbose_name='是否有题目附件')
    mark_total = models.PositiveIntegerField(default=0, verbose_name='总评分')
    mark_count = models.PositiveIntegerField(default=0, verbose_name='评分人数')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = "challenge"
        verbose_name = "题目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Attachment(models.Model):
    file = models.FileField(upload_to='challenge_file/',verbose_name='文件', help_text='若设置有题目附件请填写此项')
    challenge_one = models.OneToOneField(Challenge, on_delete=models.CASCADE, verbose_name='题目', related_name='attachment')

    class Meta:
        db_table = "challenge_attachment"
        verbose_name = "题目附件"
        verbose_name_plural = verbose_name


class DockerConfig(models.Model):
    name = models.CharField(max_length=256, verbose_name='镜像名', help_text='若设置题目类型为docker请填写此项')
    port = models.PositiveIntegerField(default=80, verbose_name='内部端口')
    memory_limit = models.PositiveSmallIntegerField(default=128, help_text='单位为M', verbose_name='内存限制')
    cpu_limit = models.DecimalField(max_digits=3, decimal_places=1, default=0.5, verbose_name='CPU限制')
    challenge_two = models.OneToOneField(Challenge, on_delete=models.CASCADE, related_name='docker_config')

    class Meta:
        db_table = "challenge_docker_config"
        verbose_name = "docker设置"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.challenge_two.title