from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.hashers import make_password
# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    list_display = ('id','email','password','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    validate_password = make_password

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email','id')
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)