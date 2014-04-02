from django.contrib import admin
from lead.models import leadform

class leadformadmin(admin.ModelAdmin):
    list_display = ('name', 'organisation', 'city', 'emailId', 'contactno')

admin.site.register(leadform, leadformadmin)
