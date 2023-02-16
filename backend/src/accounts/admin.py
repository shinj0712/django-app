from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

@admin.register(User)

class AdminUserAdmin(UserAdmin):
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (None, {
            "fields": (
                "username",
                "password"
            ),
        }),
        ("権限設定", {
            "fields": (
                "is_active",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("日時", {
            "fields": (
                "last_login",
            ),
        })
    )
    
    list_display      = ("username", "email", "last_login")
    search_fields     = ("username", "email", "first_name", "last_name", "first_name_kana", "last_name_kana", "first_name_en", "last_name_en")
    filter_horizontal = ("groups", "user_permissions")
