from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, SolveInfo


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'is_superuser', 'is_staff', 'is_active', 'sex']
    readonly_fields = ['last_login', 'date_joined']


@admin.register(SolveInfo)
class SolveInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'challenge', 'state', 'time']
