from django.contrib import admin
from challenge.models import Challenge, ChallengeAttachment, ChallengeDockerConfig
# Register your models here.


class ChallengeAttachmentInline(admin.StackedInline):
    model = ChallengeAttachment
    fk_name = 'challenge_one'
    can_delete = False


class ChallengeDockerConfigInline(admin.StackedInline):
    model = ChallengeDockerConfig
    fk_name = 'challenge_two'
    can_delete = False


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ['title', 'environment_type','state','score',  'is_fixed_flag', 'have_attachment']
    readonly_fields = ['mark_total', 'mark_count']
    inlines = [ChallengeAttachmentInline,ChallengeDockerConfigInline]


@admin.register(ChallengeAttachment)
class ChallengeAttachmentAdmin(admin.ModelAdmin):
    list_display = ['file']


@admin.register(ChallengeDockerConfig)
class ChallengeDockerConfigAdmin(admin.ModelAdmin):
    list_display = ['name', 'port', 'memory_limit', 'cpu_limit']
