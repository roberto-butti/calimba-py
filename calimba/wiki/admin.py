from calimba.wiki.models import Page
from django.contrib import admin
from django.utils import timezone


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
    fieldsets = [
        (None,               {'fields': ['slug','name', 'content', 'pub_date']})
#        ('Date information', {'fields': ['date_start', 'date_end']}),
#        ('workflow', {'fields': ['pub_date', 'status'], 'classes': ['collapse']}),

    ]


admin.site.register(Page, PageAdmin)
