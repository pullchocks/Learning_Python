from django.contrib import admin
from .models import Issue

class IssueAdmin(admin.ModelAdmin):
    date_hierarchy = 'opened_on'
    list_filter = ('status', 'owner')
    list_display = ('id', 'name', 'status', 'owner', 'modified_on')
    search_fields = ['summary', 'status']

admin.site.register(Issue, IssueAdmin)