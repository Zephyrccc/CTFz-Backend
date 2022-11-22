from django.contrib import admin

# Register your models here.
from .models import User, UserProfile


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password', 'last_login','is_superuser', 'is_staff', 'is_active']

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile()
            user_profile.user = user
            user_profile.save()
        super().save_model(request, obj, form, change)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'sex']

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['user']
        else:
            return []


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
