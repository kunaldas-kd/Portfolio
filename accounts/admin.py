from django.contrib import admin
from .models import User,Profile,Session,SocialAccount,LoginLogs
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'username', 'email', 'is_active', 'is_verified')
    search_fields = ('username', 'email')
    list_filter=('is_active', 'is_verified')
    

admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Session)
admin.site.register(SocialAccount)
admin.site.register(LoginLogs)
