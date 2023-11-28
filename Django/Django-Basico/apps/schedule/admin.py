from django.contrib import admin
from apps.schedule.models import schedule, schedule_category


class ScheduleAdmin(admin.ModelAdmin):
    ...

admin.site.register(schedule, ScheduleAdmin)
admin.site.register(schedule_category)
