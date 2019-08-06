from django.contrib import admin

from users import models


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'fname', 'lname', 'is_active', 'is_staff', 'last_login')


admin.site.register(models.UserProfile, UserProfileAdmin)
