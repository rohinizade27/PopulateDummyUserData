from django.contrib import admin

from .models import User, ActivityPeriod


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id','real_name', 'time_zone')


admin.site.register(User, UserAdmin)


class ActivityPeriodAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time','end_time')


admin.site.register(ActivityPeriod, ActivityPeriodAdmin)
