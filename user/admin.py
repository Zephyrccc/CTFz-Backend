from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile
from challenge.models import Challenge

class ProfileInline(admin.StackedInline):
    model = Profile
    # '''设置列表可显示的字段'''
    # 只读字段
    # readonly_fields = ['sex']
    # 排除字段
    # exclude = ['members']
    # 是否可删除
    can_delete = False

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'last_login','is_superuser','is_staff', 'is_active']
    readonly_fields = ['last_login', 'date_joined']
    inlines = [ProfileInline]

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    def show_finished_challenge(self, obj):
        challenge_list=[]
        for finished in obj.finished_challenge.all():
            challenge_list.append(finished.title)
        return ','.join(challenge_list)
    list_display = ['user', 'sex','show_finished_challenge']
    show_finished_challenge.short_description='解决的题目'

