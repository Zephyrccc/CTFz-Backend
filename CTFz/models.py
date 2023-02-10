from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an username')

        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username, password=password)
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    SEX_CHOICES = (('男', '男'), ('女', '女'), ('保密', '保密'))
    BOOLEAN_CHOICES = ((True, '正常'), (False, '封禁'))
    username = models.CharField(
        max_length=30, unique=True, verbose_name='用户名',)
    avatar = models.ImageField(
        upload_to='avatar', default='avatar/defaultAvatar.png', verbose_name='头像')
    sex = models.CharField(choices=SEX_CHOICES, max_length=2,
                           default='保密', verbose_name='性别')
    describe = models.CharField(
        max_length=254, default='这家伙很懒什么也没留下...', verbose_name='个人介绍')
    total_score = models.PositiveIntegerField(default=0, verbose_name='总分')
    team = models.ForeignKey(to='CTFz.Team', null=True, blank=True,
                             related_name='member', on_delete=models.CASCADE, verbose_name='团队')
    solve_info = models.ManyToManyField(
        to='CTFz.Challenge', through='CTFz.SolveInfo', through_fields=('user', 'challenge'))
    is_active = models.BooleanField(
        choices=BOOLEAN_CHOICES, default=True, verbose_name='账号状态')
    is_admin = models.BooleanField(default=False, verbose_name='是否是管理员')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        # The user is identified by their username address
        return self.username

    def get_short_name(self):
        # The user is identified by their username address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.username


class Team(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='名称')
    captain = models.OneToOneField(
        to="CTFz.User", blank=True, on_delete=models.CASCADE, related_name='teamCaptain', verbose_name='队长')
    declare = models.CharField(max_length=32, blank=True, verbose_name='宣言')
    describe = models.CharField(max_length=256, blank=True, verbose_name='简介')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = "team"
        verbose_name = "团队"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='分类名')

    class Meta:
        db_table = "category"
        verbose_name = "题目分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    value = models.CharField(max_length=64, verbose_name='标签名')

    class Meta:
        db_table = "tag"
        verbose_name = "标签列表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.value


class Challenge(models.Model):
    """题目系统"""

    STATE_CHOICES = ((True, '开放'), (False, '隐藏'))
    ENVIRONMENT_TYPE_CHOICES = (('dynamic', '动态'), ('static', '静态'))
    title = models.CharField(max_length=128, verbose_name='题目名称')
    environment_type = models.CharField(
        choices=ENVIRONMENT_TYPE_CHOICES, default='dynamic', max_length=7, verbose_name='环境类型')
    category = models.ForeignKey(
        to='CTFz.Category', on_delete=models.CASCADE, verbose_name="题目分类")
    tag = models.ManyToManyField(to='CTFz.Tag', blank=True, verbose_name='标签')
    describe = models.CharField(max_length=256, blank=True, verbose_name='描述')
    score = models.PositiveIntegerField(default=1, verbose_name='分值')
    state = models.BooleanField(
        choices=STATE_CHOICES, default=True, verbose_name='状态')
    fixed_flag = models.CharField(
        max_length=128, blank=True, help_text='若为静态环境请设置此项', verbose_name='固定的flag值')
    attachment = models.FileField(
        upload_to='attachment', blank=True, help_text='若有附件请设置此项', verbose_name='附件')
    difficulty = models.FloatField(default=1.0, validators=[MaxValueValidator(
        5.0), MinValueValidator(0.0)], verbose_name='难度')
    solve_info = models.ManyToManyField(
        to='CTFz.User', through='CTFz.SolveInfo', through_fields=('challenge', 'user'))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = "challenge"
        verbose_name = "题目"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class SolveInfo(models.Model):
    BOOLEAN_CHOICES = ((True, '成功'), (False, '失败'))
    user = models.ForeignKey(
        to='CTFz.User', on_delete=models.CASCADE, verbose_name='用户')
    challenge = models.ForeignKey(
        to='CTFz.Challenge', on_delete=models.CASCADE, verbose_name='题目')
    state = models.BooleanField(
        choices=BOOLEAN_CHOICES, default=False, verbose_name='解题状态')
    time = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')

    class Meta:
        db_table = "solve_info"
        verbose_name = "解题记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.pk)


class JoinRequest(models.Model):
    user = models.OneToOneField(to="CTFz.User", blank=True, on_delete=models.CASCADE, verbose_name='用户')
    team = models.OneToOneField(to="CTFz.Team", blank=True, on_delete=models.CASCADE, verbose_name='团队')
    time = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    state = models.BooleanField(default=False, verbose_name='操作状态')

    class Meta:
        db_table = "join_request"
        verbose_name = "申请记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.pk)
