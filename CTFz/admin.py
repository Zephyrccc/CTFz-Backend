# admin.py
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User, Team, Category, Tag, Challenge, SolveInfo, JoinRequest


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'password', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


@admin.register(User)
class UserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'team', 'total_score', 'is_active', 'is_admin')
    list_filter = ('team', 'is_active', 'is_admin')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('用户信息', {'fields': ('avatar', 'sex', 'describe',
         'total_score', 'team', 'is_active',)}),
        ('权限', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')}
         ),
    )
    search_fields = ('username', 'team')
    ordering = ('username',)
    filter_horizontal = ()

# Now register the new UserAdmin...
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'captain', 'declare', 'describe', 'created_time')

    fieldsets = (
        ('团队信息', {'fields': ('name', 'captain', 'declare', 'describe',)}),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['value']


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):

    list_display = ['title', 'environment_type', 'category',
                    'state', 'score', 'attachment', 'show_tag']
    list_filter = ['environment_type']
    list_editable = ['score', 'state', 'category']
    filter_horizontal = ['tag']

    def show_tag(self, obj):
        return [Tag.value for Tag in obj.tag.all()]
    show_tag.short_description = '标签'


@admin.register(SolveInfo)
class SolveInfoAdmin(admin.ModelAdmin):
    list_display = ['user', 'challenge', 'state', 'time']


@admin.register(JoinRequest)
class JoinRequestAdmin(admin.ModelAdmin):
    list_display = ['user', 'team', 'state', 'time']
    fieldsets = (
        ('申请记录', {'fields': ('user', 'team', 'state', )}),
    )
