from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Todo


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Admin configuration for the CustomUser model.
    """
    model = CustomUser
    list_display = ('username', 'email', 'full_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'full_name')
    ordering = ('username', )

    fieldsets = UserAdmin.fieldsets + (('Additional Info', {
        'fields': ('full_name', )
    }), ) # type: ignore

    add_fieldsets = UserAdmin.add_fieldsets + ((None, {
        'fields': ('full_name', )
    }), )


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Todo model.
    """
    list_display = ('title', 'user', 'completed', 'created_at', 'updated_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('-created_at', )
