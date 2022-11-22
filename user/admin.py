from django.contrib import admin

# Register your models here.
from .models import User, UserProfile


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    # '''设置列表可显示的字段'''
    # fields = ['sex']
    # 只读字段
    # readonly_fields = ['sex']
    # 排除字段
    # exclude = ['members']
    # 是否可删除
    can_delete = False



class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'last_login','is_superuser', 'is_staff', 'is_active']
    inlines = [UserProfileInline]


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'sex']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['user']
        else:
            return []


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
