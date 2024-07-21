from django.contrib import admin
from . models import *


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'is_student',
                    'is_paid_membership', 'is_paid_conference']


admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
