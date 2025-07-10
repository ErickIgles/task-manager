from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(BaseUserAdmin):

    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('first_name', 'last_name', 'email')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Informações pessoais'), {'fields': ('first_name', 'last_name')}),
        (('Permissões'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Datas importantes'), {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )