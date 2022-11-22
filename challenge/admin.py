from django.contrib import admin

# Register your models here.
from .models import Challenge,ChallengeFile

class ChallengeAdmin(admin.ModelAdmin):
    list_display=['title','score','mark_total','mark_count','created_time']

# class UserProfileAdmin(admin.ModelAdmin):
#     list_display=['user','sex']

#     def get_readonly_fields(self, request, obj=None):
#         if obj:
#             return ['user']
#         else:
#             return []

admin.site.register(Challenge,ChallengeAdmin)
# admin.site.register(UserProfile,UserProfileAdmin)
