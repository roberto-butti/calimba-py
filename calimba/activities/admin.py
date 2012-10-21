from calimba.activities.models import Activity, ActivityStatus
from django.contrib import admin


class ActivityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title']}),
        ('Date information', {'fields': ['date_start', 'date_end']}),
        ('workflow', {'fields': ['pub_date', 'status'], 'classes': ['collapse']}),

    ]


admin.site.register(Activity, ActivityAdmin)
admin.site.register(ActivityStatus)
